import psutil


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


print(get_cpu_usage())
