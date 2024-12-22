import random

class CPUSimulation:
    def __init__(self):
        self.core_types = ["in-order", "out-of-order"]
        self.current_core = random.choice(self.core_types)  # Start with a random core type
        self.state = self.reset()

    def reset(self):
        """
        Resets the CPU simulation to an initial state.
        """
        self.state = {"ipc": random.uniform(0.5, 2.0), "memory_usage": random.uniform(100, 500)}  # IPC and memory usage as performance metrics
        return self.state

    def step(self, action):
        """
        Simulates the effect of a core switch (action) on the CPU state.
        Args:
            action (int): 0 for switching to low-complexity core, 1 for high-complexity core.
        Returns:
            next_state (dict): Updated performance metrics.
            reward (float): Reward based on the efficiency of the core switch.
            done (bool): Whether the simulation has ended.
        """

        self.current_core = self.core_types[action]
        next_state = self._simulate_performance(self.current_core)
        reward = self._calculate_reward(next_state)
        done = False  # Continuous simulation, no terminal state
        return next_state, reward, done

    def _simulate_performance(self, core_type):
        """
        Simulates the performance of the current core type.
        Args:
            core_type (str): "in-order" or "out-of-order".
        Returns:
            state (dict): Simulated performance metrics for the current core.
        """
        if core_type == "in-order":
            ipc = random.uniform(0.5, 1.2)  # Low-complexity core IPC
            memory_usage = random.uniform(100, 300)
        else:
            ipc = random.uniform(1.0, 2.0)  # High-complexity core IPC
            memory_usage = random.uniform(300, 500)
        return {"ipc": ipc, "memory_usage": memory_usage}

    def _calculate_reward(self, state):
        """
        Calculates the reward based on performance (higher IPC, lower memory usage is rewarded).
        Args:
            state (dict): Current CPU performance metrics.
        Returns:
            reward (float): Reward value.
        """
        ipc = state["ipc"]
        memory_usage = state["memory_usage"]
        reward = ipc - (memory_usage / 500)  # Reward favors high IPC and low memory usage
        return reward
