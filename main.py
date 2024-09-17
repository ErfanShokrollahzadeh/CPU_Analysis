import psutil

# Function to retrieve and return the current CPU usage, memory usage, disk usage, and network activity
def get_cpu_usage():
    # Get the CPU usage percentage over an interval of 1 second
    cpu_usage = psutil.cpu_percent(interval=1)
    
    # Get the system's virtual memory usage in percentage
    memory_info = psutil.virtual_memory()
    memory_usage = memory_info.percent
    
    # Get the disk usage of the root directory in percentage
    disk_info = psutil.disk_usage('/')
    disk_usage = disk_info.percent
    
    # Get the number of bytes sent and received over the network
    net_info = psutil.net_io_counters()
    net_sent = net_info.bytes_sent
    net_recv = net_info.bytes_recv
    
    # Return a dictionary containing all the gathered information
    return {
        "cpu_usage": cpu_usage,
        "memory_usage": memory_usage,
        "disk_usage": disk_usage,
        "net_sent": net_sent,
        "net_recv": net_recv
    }

# Print the returned dictionary to the console
print(get_cpu_usage())
