import unittest
from system.cpu_simulation import CPUSimulation

class TestCPUSimulation(unittest.TestCase):
    def setUp(self):
        self.cpu_sim = CPUSimulation()

    def test_reset(self):
        # Test if the reset method initializes the state correctly
        state = self.cpu_sim.reset()
        self.assertIn('ipc', state)
        self.assertIn('memory_usage', state)
        self.assertTrue(0.5 <= state['ipc'] <= 2.0)
        self.assertTrue(100 <= state['memory_usage'] <= 500)

    def test_step(self):
        # Test the step function with an action
        action = 0  # Switch to in-order core
        next_state, reward, done = self.cpu_sim.step(action)
        self.assertIn('ipc', next_state)
        self.assertIn('memory_usage', next_state)
        self.assertIsInstance(reward, float)
        self.assertFalse(done)

if __name__ == '__main__':
    unittest.main()
