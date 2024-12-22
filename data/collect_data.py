import os
import numpy as np
import csv

class DataCollector:
    def __init__(self, save_path="data/performance_data.csv"):
        self.save_path = save_path
        if not os.path.exists(os.path.dirname(save_path)):
            os.makedirs(os.path.dirname(save_path))
    
    def collect_performance_data(self, state, ipc, memory_usage, core_type, action, reward):
        """
        Collects the performance metrics of the CPU cores and writes to CSV.
        Args:
            state (list): The current state of the system (e.g., CPU metrics like IPC).
            ipc (float): Instructions per cycle metric.
            memory_usage (float): Memory usage at the current state.
            core_type (int): 0 for low-complexity core, 1 for high-complexity core.
            action (int): Action taken (core switch decision).
            reward (float): Reward received from the action.
        """
        with open(self.save_path, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([state, ipc, memory_usage, core_type, action, reward])

    def read_performance_data(self):
        """
        Reads the collected data from the CSV file.
        """
        data = []
        if os.path.exists(self.save_path):
            with open(self.save_path, 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    data.append(row)
        return data
