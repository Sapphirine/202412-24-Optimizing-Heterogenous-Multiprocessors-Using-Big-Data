def calculate_ipc(state):
    """
    Calculates the Instructions Per Cycle (IPC) metric.
    Args:
        state (dict): The current state of the system.
    Returns:
        float: IPC value.
    """
    return state['ipc']


def calculate_memory_efficiency(state):
    """
    Calculates memory efficiency as a metric based on current memory usage.
    Args:
        state (dict): The current state of the system.
    Returns:
        float: Memory efficiency value.
    """
    memory_usage = state['memory_usage']
    return 500 / memory_usage  
