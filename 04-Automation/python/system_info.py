import platform
import os
import shutil

print("=" * 45)
print("       SAMCLOUD SYSTEM INFORMATION")
print("=" * 45)

print("Operating System:", platform.system())
print("OS Release:", platform.release())
print("Architecture:", platform.machine())
print("Python Version:", platform.python_version())
print("Processor:", platform.processor() or "Not reported")

total, used, free = shutil.disk_usage("/")

print("\nDisk Information:")
print(f"Total: {total // (1024**3)} GB")
print(f"Used:  {used // (1024**3)} GB")
print(f"Free:  {free // (1024**3)} GB")

print("\nCPU Count:", os.cpu_count())

print("\nSystem information check completed.")
