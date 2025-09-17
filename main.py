import psutil

def main():
    print("Week 1 – System Info Monitor")
    print(f"CPU Usage: {psutil.cpu_percent(interval=1)}%")
    print(f"Memory Usage: {psutil.virtual_memory().percent}%")
    print(f"Disk Usage: {psutil.disk_usage('/').percent}%")

if __name__ == "__main__":
    main()
