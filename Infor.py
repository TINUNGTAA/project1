import platform
import psutil

#computer network name

print(f"computer network name: {platform.node()}")

#machine type

print(f"machine type: {platform.machine()}")

#processor type

print(f"processor type: {platform.platform()}")

#CPU Infor
print(f"CPU: {[platform.processor()]}")


#operating system
print(f"operating system: {platform.system()}")

#operating system release
print(f"opereating system release: {platform.release()}")

#operating system version
print(f"operating system version: {platform.version()}")

#memory infor
memory= psutil.virtual_memory()
# converting to GB
total_memory= memory.total/(1024**3) 
# converting to GB
available_memory =memory.available/(1024**3) 


#Disk Information
disk= psutil.disk_usage('/')
total_disk= disk.total/(1024**3)
available_disk= disk.free/ (1024**3)


print(f"Total memory: {total_memory} GB")
print(f"Available memory: {available_memory} GB")
print(f"Total Disk: {total_disk} GB")
print(f"Available Disk:{available_disk} GB")