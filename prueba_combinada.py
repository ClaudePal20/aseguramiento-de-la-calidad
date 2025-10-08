import requests
import concurrent.futures
import random
import time

URL = "http://localhost:5000/books"

def mixed_task():
    r = random.random()
    if r < 0.1:
        requests.post(URL, json={"title": "Libro Random", "author": "Mix"})
    elif r < 0.8:
        requests.get(URL)
    else:
        requests.get(URL + "/search?q=libro")

for step in range(5):
    users = (step + 1) * 50
    start = time.time()
    with concurrent.futures.ThreadPoolExecutor(max_workers=users) as executor:
        list(executor.map(lambda _: mixed_task(), range(500)))
    print(f"Etapa {step+1} - Usuarios: {users}, Tiempo: {time.time()-start:.2f}s")
