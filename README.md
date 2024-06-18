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
