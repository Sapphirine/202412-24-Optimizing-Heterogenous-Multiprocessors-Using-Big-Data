import unittest
import torch
from model.ppo_agent import PPOAgent
from model.neural_network import PolicyNetwork, ValueNetwork

class TestPPOAgent(unittest.TestCase):
    def setUp(self):
        # Initialize the policy and value networks for testing
        self.policy_network = PolicyNetwork(state_size=2, action_size=2)
        self.value_network = ValueNetwork(state_size=2)
        self.ppo_agent = PPOAgent(self.policy_network, self.value_network)

    def test_select_action(self):
        # Test action selection
        state = [1.0, 0.5]  # Example state (IPC, memory usage)
        action, log_prob = self.ppo_agent.select_action(state)
        self.assertIn(action, [0, 1])  # Action should be 0 or 1
        self.assertTrue(isinstance(log_prob, torch.Tensor))

    def test_update(self):
        # Test the update function of the PPO agent
        states = [[1.0, 0.5], [0.8, 0.6]]
        actions = [0, 1]
        log_probs = [torch.tensor(0.8), torch.tensor(0.6)]
        rewards = [1, 1]
        values = [0.9, 0.7]

        # Test the update (No exception should occur)
        try:
            self.ppo_agent.update(states, actions, log_probs, rewards, values)
        except Exception as e:
            self.fail(f"Update failed with exception: {e}")

if __name__ == '__main__':
    unittest.main()
