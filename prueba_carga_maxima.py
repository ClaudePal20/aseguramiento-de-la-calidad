import requests
import concurrent.futures
import time

URL = "http://localhost:5000/books"

def get_books():
    start = time.time()
    r = requests.get(URL)
    elapsed = time.time() - start
    return elapsed, r.status_code

for users in [10, 50, 100, 200, 500]:
    start = time.time()
    with concurrent.futures.ThreadPoolExecutor(max_workers=users) as executor:
        results = list(executor.map(get_books, range(users)))
    avg_time = sum(r[0] for r in results) / len(results)
    errors = len([r for r in results if r[1] != 200])
    print(f"Usuarios: {users} | Tiempo promedio: {avg_time:.3f}s | Errores: {errors}")
