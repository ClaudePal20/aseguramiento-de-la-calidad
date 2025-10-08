import requests
import time

URL = "http://localhost:5000/books"
start = time.time()
end = start + 3600  # 1 hora
count = 0

while time.time() < end:
    requests.get(URL)
    count += 1
    time.sleep(0.5)

print("Total de peticiones en 1 hora:", count)
