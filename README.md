System Resource Monitor
This Python script uses the psutil library to monitor system resources such as CPU usage, memory usage, disk usage, and network activity.

import psutil

The script starts by importing the psutil library, which provides an interface for retrieving information on running processes and
system utilization (CPU, memory, disks, network, sensors) in Python.

def get_cpu_usage():

This function retrieves and returns the current CPU usage, memory usage, disk usage, and network activity.

cpu_usage = psutil.cpu_percent(interval=1)

This line gets the CPU usage percentage over an interval of 1 second.

memory_info = psutil.virtual_memory()
memory_usage = memory_info.percent

These lines get the system's virtual memory usage in percentage.

disk_info = psutil.disk_usage('/')
disk_usage = disk_info.percent

These lines get the disk usage of the root directory in percentage.

net_info = psutil.net_io_counters()
net_sent = net_info.bytes_sent
net_recv = net_info.bytes_recv

These lines get the number of bytes sent and received over the network.

return {
    "cpu_usage": cpu_usage,
    "memory_usage": memory_usage,
    "disk_usage": disk_usage,
    "net_sent": net_sent,
    "net_recv": net_recv
}

The function returns a dictionary containing all the gathered information.

print(get_cpu_usage())

Finally, the script prints the returned dictionary to the console.

Usage
To run the script, simply execute the main.py file in your Python environment. The output will be printed to the console.

Setup Instructions
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
4. Run the script:
   ```
   python main.py
   ```

Requirements
- Python 3.9 or higher
- psutil library

Project Description
This project is a system resource monitor that uses the psutil library to gather information about CPU usage, memory usage, disk usage, and network activity. The script provides a simple way to monitor these system resources and can be used for performance monitoring and analysis.

Technologies Used
- Python
- psutil library
