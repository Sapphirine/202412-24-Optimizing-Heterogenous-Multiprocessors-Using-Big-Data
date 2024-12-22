import numpy as np

class Splash2Loader:
    def __init__(self, benchmark_dir="data/splash2_benchmarks/"):
        self.benchmark_dir = benchmark_dir

    def load_benchmark(self, benchmark_name):
        """
        Loads the requested benchmark data.
        Args:
            benchmark_name (str): Name of the Splash2 benchmark (e.g., "fft", "lu", "radix").
        Returns:
            np.array: Loaded benchmark data as a NumPy array.
        """
        file_path = f"{self.benchmark_dir}/{benchmark_name}.npy"
        try:
            benchmark_data = np.load(file_path)
            return benchmark_data
        except FileNotFoundError:
            print(f"Benchmark {benchmark_name} not found in directory {self.benchmark_dir}")
            return None

    def list_available_benchmarks(self):
        """
        Lists all available benchmarks in the directory.
        """
        import os
        return [f.replace('.npy', '') for f in os.listdir(self.benchmark_dir) if f.endswith('.npy')]

