import logging

# Configure logger
logging.basicConfig(
    filename='logs/training.log', 
    level=logging.INFO, 
    format='%(asctime)s - %(levelname)s - %(message)s',
)

def log_event(event):
    """
    Logs an event with an info level.
    Args:
        event (str): The event message to log.
    """
    logging.info(event)

def log_error(error_message):
    """
    Logs an error event.
    Args:
        error_message (str): The error message to log.
    """
    logging.error(error_message)

def log_performance(episode, total_reward):
    """
    Logs the performance of the agent in each episode.
    Args:
        episode (int): The episode number.
        total_reward (float): The total reward obtained in the episode.
    """
    logging.info(f"Episode {episode} - Total Reward: {total_reward}")
