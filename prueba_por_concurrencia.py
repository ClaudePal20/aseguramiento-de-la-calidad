import requests
import concurrent.futures
import random

URL = "http://localhost:5000/books"

def task():
    if random.random() < 0.3:
        requests.post(URL, json={"title": "Nuevo", "author": "Test"})
    else:
        requests.get(URL)

with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
    list(executor.map(lambda _: task(), range(500)))
