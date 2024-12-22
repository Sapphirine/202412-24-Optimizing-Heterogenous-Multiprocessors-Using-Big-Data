from pyspark.sql import SparkSession

class DataPipeline:
    def __init__(self):
        # Initialize Spark session
        self.spark = SparkSession.builder \
            .appName("CoreSwitchingOptimization") \
            .master("local[*]") \
            .getOrCreate()

    def preprocess_data(self, raw_data):
        """
        Preprocesses the raw benchmark data using Apache Spark.
        Example preprocessing: normalization using distributed Spark transformations.
        """
        df = self.spark.createDataFrame(raw_data, schema=["state", "ipc", "memory_usage"])

        normalized_df = df.withColumn("normalized_ipc", (df["ipc"] - df["ipc"].mean()) / df["ipc"].stddev()) \
                          .withColumn("normalized_memory_usage", (df["memory_usage"] - df["memory_usage"].mean()) / df["memory_usage"].stddev())

        return normalized_df

    def load_collected_data_spark(self):
        """
        Loads the performance data into a Spark DataFrame for distributed processing.
        """
        hdfs_path = "hdfs://localhost:9000/data/performance_data.csv"
        return self.spark.read.csv(hdfs_path, header=True, inferSchema=True)

    def transform_and_process(self):
        """
        Loads, transforms, and processes large datasets using Spark.
        """
        df = self.load_collected_data_spark()
        stats = df.groupBy("core_type").agg({"ipc": "avg", "memory_usage": "avg"})
        stats.show()
