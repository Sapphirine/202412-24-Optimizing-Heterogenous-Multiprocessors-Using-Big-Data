import matplotlib.pyplot as plt

def plot_total_rewards(total_rewards, plot_save_path="plots/performance_plot.png"):
    """
    Plots total rewards over episodes and saves the plot to a file.
    Args:
        total_rewards (list): List of total rewards per episode.
        plot_save_path (str): The file path to save the plot.
    """
    plt.figure(figsize=(10, 6))
    plt.plot(total_rewards, label="Total Rewards")
    plt.title("Total Rewards per Episode")
    plt.xlabel("Episode")
    plt.ylabel("Total Reward")
    plt.legend()
    plt.grid(True)
    
    # Save the plot
    plt.savefig(plot_save_path)
    plt.show()

def plot_ipc_vs_memory(ipc_list, memory_list, plot_save_path="plots/ipc_vs_memory.png"):
    """
    Plots IPC vs memory usage over episodes.
    Args:
        ipc_list (list): List of IPC values.
        memory_list (list): List of memory usage values.
        plot_save_path (str): The file path to save the plot.
    """
    plt.figure(figsize=(10, 6))
    plt.plot(ipc_list, label="IPC", color='blue')
    plt.plot(memory_list, label="Memory Usage", color='red')
    plt.title("IPC vs Memory Usage")
    plt.xlabel("Step")
    plt.ylabel("Value")
    plt.legend()
    plt.grid(True)
    
    # Save the plot
    plt.savefig(plot_save_path)
    plt.show()
