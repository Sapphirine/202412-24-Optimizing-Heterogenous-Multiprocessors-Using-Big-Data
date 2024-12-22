from model.ppo_agent import PPOAgent
from model.neural_network import PolicyNetwork, ValueNetwork
from system.cpu_simulation import CPUSimulation
from system.feedback_loop import feedback_loop
from data.data_pipeline import DataPipeline
from utils.logger import log_event, log_performance
from utils.visualization import plot_total_rewards
from utils.config import Config

def main():
    # Load configurations
    config = Config()
    
    # Initialize CPU simulation environment
    cpu_sim = CPUSimulation()

    # Initialize data pipeline
    data_pipeline = DataPipeline()

    # Initialize PPO agent with policy and value networks
    policy_network = PolicyNetwork(state_size=config.state_size, action_size=config.action_size)
    value_network = ValueNetwork(state_size=config.state_size)
    ppo_agent = PPOAgent(policy_network, value_network, lr=config.learning_rate, gamma=config.gamma, epsilon=config.epsilon)

    # Log start of training
    log_event("Starting PPO training for core switching optimization...")

    total_rewards = []  # To track rewards over episodes
    
    # Run episodes
    for episode in range(config.num_episodes):
        # Reset environment at the start of each episode
        state = cpu_sim.reset()

        episode_rewards = 0  # Track rewards for this episode
        
        for step in range(config.max_steps):
            # Make core switching decision using PPO agent
            action = make_core_switch_decision(state, ppo_agent)

            # Step through the simulation
            next_state, reward, done = cpu_sim.step(action)

            # Collect performance metrics (IPC, memory usage, etc.)
            ipc = next_state['ipc']
            memory_usage = next_state['memory_usage']
            data_pipeline.collect_performance_metrics(
                state=state, ipc=ipc, memory_usage=memory_usage, core_type=action, action=action, reward=reward
            )

            # Accumulate rewards
            episode_rewards += reward
            
            # Move to next state
            state = next_state
            
            # Break if done (in case of terminal states, though here we simulate continuously)
            if done:
                break

        # Store total rewards for this episode
        total_rewards.append(episode_rewards)

        # Log performance every 10 episodes
        if episode % 10 == 0:
            log_performance(episode, episode_rewards)
            print(f"Episode {episode}, Total Reward: {episode_rewards}")
    
    # Log end of training
    log_event("Training completed.")

    # Plot total rewards over episodes
    plot_total_rewards(total_rewards, plot_save_path=config.plot_save_path)

    print("Training completed. Rewards plotted.")

if __name__ == "__main__":
    main()
