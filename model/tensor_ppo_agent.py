import tensorflow as tf
from tensorflow.keras import layers

class PPOAgent:
    def __init__(self, policy_network, value_network, lr=0.0003, gamma=0.99, epsilon=0.2):
        self.policy_network = policy_network
        self.value_network = value_network
        self.optimizer = tf.keras.optimizers.Adam(learning_rate=lr)
        self.gamma = gamma  # Discount factor
        self.epsilon = epsilon  # PPO clipping range

    def select_action(self, state):
        """
        Selects an action based on the policy network (TensorFlow).
        """
        state_tensor = tf.convert_to_tensor([state], dtype=tf.float32)
        action_probs = self.policy_network(state_tensor)
        action = tf.random.categorical(action_probs, 1)
        return action.numpy()[0, 0], tf.reduce_sum(action_probs)

    def update(self, states, actions, log_probs, rewards, values):
        """
        Updates the policy and value networks using TensorFlow's gradient updates.
        """
        with tf.GradientTape() as tape:
            # Calculate advantage and losses for PPO
            advantage = self.compute_advantage(rewards, values)
            policy_loss, value_loss = self.compute_losses(states, actions, log_probs, advantage)

            # Perform gradient descent
            gradients = tape.gradient(policy_loss + value_loss, self.policy_network.trainable_variables + self.value_network.trainable_variables)
            self.optimizer.apply_gradients(zip(gradients, self.policy_network.trainable_variables + self.value_network.trainable_variables))

