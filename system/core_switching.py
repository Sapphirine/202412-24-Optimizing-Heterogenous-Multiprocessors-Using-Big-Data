def make_core_switch_decision(state, ppo_agent):
    """
    Make core-switching decision based on the current state and PPO model.
    Args:
        state (dict): Current state of the system (e.g., IPC, memory usage).
        ppo_agent (PPOAgent): Trained PPO agent to make the decision.
    Returns:
        action (int): Action selected by PPO (0 for in-order core, 1 for out-of-order core).
    """
    # Flatten state to a vector for the agent
    state_vector = [state['ipc'], state['memory_usage']]
    action, _ = ppo_agent.select_action(state_vector)
    return action
