# 202412-24-Optimizing-Heterogenous-Multiprocessors-Using-Big-Data
To develop a machine learning model to predict fine-grained core switching in CMPs using Big Data tools, as well as to optimize system performance by applying Proximal Policy Optimization to dynamically allocate resources between in-order and out-of-order cores.

project-root/
│
├── data/
│   ├── collect_data.py          # Scripts for data collection and preprocessing
│   ├── load_splash2_benchmarks.py # Loads and manages datasets from Splash2 benchmarks
│   └── data_pipeline.py          # Handles the flow of data from benchmarks to training
│
├── model/
│   ├── ppo_agent.py             # Reinforcement Learning PPO agent definition
│   ├── neural_network.py        # Defines the architecture of the neural network (actor and critic)
│   ├── environment.py           # Simulation environment (interaction between agent and CMP)
│   └── training_loop.py         # Core training loop for PPO model
│
├── system/
│   ├── cpu_simulation.py        # Simulates in-order and out-of-order CPU architectures
│   ├── core_switching.py        # Core switching decision-making logic
│   ├── performance_metrics.py   # Evaluates instruction per cycle (IPC) and other key metrics
│   └── feedback_loop.py         # Implements the performance feedback loop for model optimization
│
├── utils/
│   ├── config.py                # Configuration file for hyperparameters, system specs, etc.
│   ├── logger.py                # Logging system to track training progress and performance
│   └── visualization.py         # Functions for visualizing results (charts, graphs)
│
├── tests/
│   ├── test_ppo_agent.py        # Unit tests for PPO agent functionality
│   ├── test_cpu_simulation.py   # Unit tests for CPU simulation
│   └── test_core_switching.py   # Tests core-switching decisions based on model output
│
└── main.py                      # Main entry point for the project execution (training, testing, etc.)

