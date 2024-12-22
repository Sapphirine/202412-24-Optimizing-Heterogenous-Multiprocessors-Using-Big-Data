from load_splash2_benchmarks import Splash2Loader
from collect_data import DataCollector
import numpy as np

class DataPipeline:
    def __init__(self):
        self.splash2_loader = Splash2Loader()
        self.data_collector = DataCollector()

    def preprocess_data(self, raw_data):
        """
        Preprocesses the raw benchmark data to make it suitable for training.
        For example, normalizing the data or extracting relevant features.
        """
        processed_data = (raw_data - np.mean(raw_data)) / np.std(raw_data)
        return processed_data

    def load_and_preprocess_benchmark(self, benchmark_name):
        """
        Loads a Splash2 benchmark, preprocesses it, and returns the processed data.
        """
        raw_data = self.splash2_loader.load_benchmark(benchmark_name)
        if raw_data is not None:
            return self.preprocess_data(raw_data)
        return None

    def collect_performance_metrics(self, state, ipc, memory_usage, core_type, action, reward):
        """
        Collects and stores the performance metrics using the DataCollector.
        """
        self.data_collector.collect_performance_data(state, ipc, memory_usage, core_type, action, reward)

    def load_collected_data(self):
        """
        Loads the collected performance data from the DataCollector.
        """
        return self.data_collector.read_performance_data()

