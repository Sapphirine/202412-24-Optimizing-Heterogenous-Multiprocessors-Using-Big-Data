import torch
from collections import deque

def train_ppo(agent, env, num_episodes=1000, max_steps=100):
    all_rewards = []
    
    for episode in range(num_episodes):
        states = []
        actions = []
        log_probs = []
        rewards = []
        values = []
        
        state = env.reset()
        
        for step in range(max_steps):
            action, log_prob = agent.select_action(state)
            next_state, reward, done = env.step(action)
            
            value = agent.value_network(torch.tensor(state, dtype=torch.float32))
            
            # Store the transition
            states.append(state)
            actions.append(action)
            log_probs.append(log_prob)
            rewards.append(reward)
            values.append(value.item())
            
            state = next_state
            
            if done:
                break

        # Update the PPO agent
        agent.update(states, actions, log_probs, rewards, values)
        
        # Collect total reward for this episode
        total_reward = sum(rewards)
        all_rewards.append(total_reward)
        
        if episode % 10 == 0:
            print(f"Episode {episode}, Total Reward: {total_reward}")

    return all_rewards
