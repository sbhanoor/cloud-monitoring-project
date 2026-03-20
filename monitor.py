import os

print("System Monitoring Script")
print("------------------------")

print("\nCPU Usage:")
os.system("top -bn1 | grep 'Cpu(s)'")

print("\nMemory Usage:")
os.system("free -h")

print("\nDisk Usage:")
os.system("df -h")

print("\nMonitoring Completed")
