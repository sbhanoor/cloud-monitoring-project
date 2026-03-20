#!/bin/bash

echo "System Monitoring Script"
echo "-------------------------"

echo "CPU Usage:"
top -bn1 | grep "Cpu(s)"

echo "Memory Usage:"
free -h

echo "Disk Usage:"
df -h

echo "Monitoring Completed"
