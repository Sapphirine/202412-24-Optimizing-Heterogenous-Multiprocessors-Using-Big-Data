class Config:
    def __init__(self):
        # PPO Hyperparameters
        self.learning_rate = 0.0003
        self.gamma = 0.99  # Discount factor
        self.epsilon = 0.2  # Clipping range for PPO

        # Neural Network Architecture
        self.state_size = 2  # Size of input (IPC and memory usage)
        self.action_size = 2  # Number of actions (switch to in-order or out-of-order)
        self.hidden_size = 128  # Number of neurons in hidden layers

        # Training settings
        self.num_episodes = 1000  # Total number of training episodes
        self.max_steps = 100  # Max steps per episode

        # System settings
        self.save_path = "data/performance_data.csv"  # Path to save performance data

        # Visualization settings
        self.plot_save_path = "plots/performance_plot.png"

    def get(self, param):
        """
        Retrieves the value of a configuration parameter.
        Args:
            param (str): The name of the parameter to retrieve.
        Returns:
            value: The value of the parameter.
        """
        return getattr(self, param, None)
