import requests
import json
import time

URL = "http://localhost:5000/books"

for i in range(10000):
    data = {"title": f"Libro {i}", "author": "Autor X"}
    r = requests.post(URL, json=data)
    if (i+1) % 1000 == 0:
        print(f"{i+1} libros añadidos")

start = time.time()
r = requests.get(URL)
print("Tiempo de respuesta con 10k libros:", time.time() - start, "s")
