import requests
import concurrent.futures
import time

URL = "http://localhost:5000/books"

def get_books():
    return requests.get(URL).status_code

# Carga normal
for users in [10, 50, 200, 500]:
    start = time.time()
    with concurrent.futures.ThreadPoolExecutor(max_workers=users) as executor:
        list(executor.map(get_books, range(users)))
    print(f"Spike a {users} usuarios: {time.time() - start:.2f}s")
