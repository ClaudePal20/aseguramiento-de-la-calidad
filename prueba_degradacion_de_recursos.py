import psutil, time, requests

URL = "http://localhost:5000/books"

for i in range(100):
    requests.get(URL)
    cpu = psutil.cpu_percent()
    mem = psutil.virtual_memory().percent
    print(f"Iteración {i} | CPU: {cpu}% | Memoria: {mem}%")
    time.sleep(1)
