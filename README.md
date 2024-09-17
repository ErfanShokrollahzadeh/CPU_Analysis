# System Resource Monitor

This Python script uses the psutil library to monitor system resources such as CPU usage, memory usage, disk usage, and network activity.

## Table of Contents
- [Description](#description)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Description

The script starts by importing the psutil library, which provides an interface for retrieving information on running processes and system utilization (CPU, memory, disks, network, sensors) in Python.

```python
import psutil
```

This function retrieves and returns the current CPU usage, memory usage, disk usage, and network activity.

```python
def get_cpu_usage():
    cpu_usage = psutil.cpu_percent(interval=1)
    memory_info = psutil.virtual_memory()
    memory_usage = memory_info.percent
    disk_info = psutil.disk_usage('/')
    disk_usage = disk_info.percent
    net_info = psutil.net_io_counters()
    net_sent = net_info.bytes_sent
    net_recv = net_info.bytes_recv
    return {
        "cpu_usage": cpu_usage,
        "memory_usage": memory_usage,
        "disk_usage": disk_usage,
        "net_sent": net_sent,
        "net_recv": net_recv
    }
```

Finally, the script prints the returned dictionary to the console.

```python
print(get_cpu_usage())
```

## Prerequisites

- Python 3.9 or higher
- psutil library

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/ErfanShokrollahzadeh/CPU_Analysis.git
   cd CPU_Analysis
   ```
2. Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate   # On Windows use `venv\Scripts\activate`
   ```
3. Install the dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

To run the script, simply execute the main.py file in your Python environment. The output will be printed to the console.

```bash
python main.py
```

## Contributing

We welcome contributions to this project! If you would like to contribute, please follow these guidelines:

1. Fork the repository and create your branch from `master`.
2. If you have added code that should be tested, add tests.
3. Ensure the test suite passes.
4. Make sure your code lints.
5. Create a pull request and describe the changes you have made.

## License

This project is licensed under the MIT License.
