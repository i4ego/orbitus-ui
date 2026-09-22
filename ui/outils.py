import psutil
import platform

def getHardware():
    uname = platform.uname()
    cpu = psutil.cpu_percent()
    ram = psutil.virtual_memory()
    net = psutil.net_io_counters()
    return {
        "os" : f"{uname.system} {uname.release} {uname.machine}",
        "cpu" : f"{cpu}% / 100%",
        "ram" : f"{round(ram.used/1024/1024/1024, 2)} GB / {round(ram.total/1024/1024/1024)} GB",
        "net" : f"{round(net.bytes_sent/1024/1024/1024 + net.bytes_recv/1024/1024/1024, 2)} GB"
    }

print(getHardware())