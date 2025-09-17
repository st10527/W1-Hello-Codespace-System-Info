#!/usr/bin/env python3
"""
System Information Monitor
Displays CPU usage, memory usage, and disk usage using psutil
"""

import psutil


def main():
    """Display system information including CPU, memory, and disk usage."""
    print("=== System Information Monitor ===")
    print()
    
    # CPU Usage
    cpu_percent = psutil.cpu_percent(interval=1)
    cpu_count = psutil.cpu_count()
    print(f"CPU Usage: {cpu_percent}%")
    print(f"CPU Cores: {cpu_count}")
    print()
    
    # Memory Usage
    memory = psutil.virtual_memory()
    memory_total_gb = memory.total / (1024**3)
    memory_used_gb = memory.used / (1024**3)
    memory_available_gb = memory.available / (1024**3)
    
    print(f"Memory Total: {memory_total_gb:.2f} GB")
    print(f"Memory Used: {memory_used_gb:.2f} GB ({memory.percent}%)")
    print(f"Memory Available: {memory_available_gb:.2f} GB")
    print()
    
    # Disk Usage
    disk_usage = psutil.disk_usage('/')
    disk_total_gb = disk_usage.total / (1024**3)
    disk_used_gb = disk_usage.used / (1024**3)
    disk_free_gb = disk_usage.free / (1024**3)
    disk_percent = (disk_usage.used / disk_usage.total) * 100
    
    print(f"Disk Total: {disk_total_gb:.2f} GB")
    print(f"Disk Used: {disk_used_gb:.2f} GB ({disk_percent:.1f}%)")
    print(f"Disk Free: {disk_free_gb:.2f} GB")


if __name__ == "__main__":
    main()