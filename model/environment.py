import random

class Environment:
    def __init__(self, num_states):
        self.num_states = num_states
        self.current_state = self.reset()

    def reset(self):
        """
        Resets the environment to the initial state.
        """
        self.current_state = [random.random() for _ in range(self.num_states)]  # Random state initialization
        return self.current_state

    def step(self, action):
        """
        Executes the action and returns the next state, reward, and done flag.
        """
        next_state = [random.random() for _ in range(self.num_states)]  # New random state
        reward = self._get_reward(action)
        done = False  # Continuous problem, no terminal state
        return next_state, reward, done

    def _get_reward(self, action):
        """
        Calculates the reward based on the action taken. For demonstration purposes, the reward is randomized.
        """
        return random.uniform(0, 1) if action == 0 else random.uniform(-1, 0)  # Randomized reward for action
