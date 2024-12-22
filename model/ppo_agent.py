import torch
import torch.nn as nn
import torch.optim as optim
from torch.distributions import Categorical

class PPOAgent:
    def __init__(self, policy_network, value_network, lr=0.0003, gamma=0.99, epsilon=0.2):
        self.policy_network = policy_network
        self.value_network = value_network
        self.optimizer = optim.Adam(list(self.policy_network.parameters()) + list(self.value_network.parameters()), lr=lr)
        self.gamma = gamma  # Discount factor
        self.epsilon = epsilon  # Clipping range for PPO

    def select_action(self, state):
        """
        Selects an action based on the policy network.
        """
        state = torch.tensor(state, dtype=torch.float32)
        action_probs = self.policy_network(state)
        action_dist = Categorical(action_probs)
        action = action_dist.sample()
        return action.item(), action_dist.log_prob(action)

    def compute_advantage(self, rewards, values):
        """
        Computes the advantage based on the rewards and values.
        """
        advantage = []
        discounted_reward = 0
        for reward, value in zip(reversed(rewards), reversed(values)):
            discounted_reward = reward + self.gamma * discounted_reward - value
            advantage.insert(0, discounted_reward)
        return torch.tensor(advantage, dtype=torch.float32)

    def update(self, states, actions, log_probs, rewards, values):
        """
        Updates the policy and value networks using PPO.
        """
        advantages = self.compute_advantage(rewards, values)
        
        for state, action, log_prob, advantage, value in zip(states, actions, log_probs, advantages, values):
            state = torch.tensor(state, dtype=torch.float32)
            
            # Policy loss
            new_action_probs = self.policy_network(state)
            new_action_dist = Categorical(new_action_probs)
            new_log_prob = new_action_dist.log_prob(torch.tensor(action))
            ratio = torch.exp(new_log_prob - log_prob)
            
            surr1 = ratio * advantage
            surr2 = torch.clamp(ratio, 1 - self.epsilon, 1 + self.epsilon) * advantage
            policy_loss = -torch.min(surr1, surr2).mean()

            # Value loss
            value_loss = (self.value_network(state) - value).pow(2).mean()

            # Total loss
            loss = policy_loss + value_loss
            
            # Backpropagation
            self.optimizer.zero_grad()
            loss.backward()
            self.optimizer.step()
