import unittest
from model.ppo_agent import PPOAgent
from model.neural_network import PolicyNetwork, ValueNetwork
from system.core_switching import make_core_switch_decision

class TestCoreSwitching(unittest.TestCase):
    def setUp(self):
        # Initialize policy and value networks for PPO agent
        self.policy_network = PolicyNetwork(state_size=2, action_size=2)
        self.value_network = ValueNetwork(state_size=2)
        self.ppo_agent = PPOAgent(self.policy_network, self.value_network)

    def test_core_switching_decision(self):
        # Test the core-switching decision function
        state = {'ipc': 1.0, 'memory_usage': 300}
        action = make_core_switch_decision(state, self.ppo_agent)
        self.assertIn(action, [0, 1])  # Action should be 0 (in-order) or 1 (out-of-order)

if __name__ == '__main__':
    unittest.main()
