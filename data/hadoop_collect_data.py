from pyhdfs import HdfsClient

class DataCollector:
    def __init__(self, hdfs_path="hdfs://localhost:9000/data/performance_data.csv"):
        self.hdfs_path = hdfs_path
        self.hdfs_client = HdfsClient(hosts='localhost:9870')  

    def collect_performance_data(self, state, ipc, memory_usage, core_type, action, reward):
        """
        Collects the performance metrics of the CPU cores and writes to HDFS.
        """
        record = f"{state},{ipc},{memory_usage},{core_type},{action},{reward}\n"
        
        with self.hdfs_client.write(self.hdfs_path, append=True) as f:
            f.write(record.encode())

    def read_performance_data(self):
        """
        Reads the collected data from the HDFS.
        """
        with self.hdfs_client.open(self.hdfs_path) as f:
            data = f.read().decode('utf-8').splitlines()
        return data
