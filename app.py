from flask import Flask, jsonify, request
import time

app = Flask(__name__)

books = [
    {"id": 1, "title": "Cien años de soledad", "author": "Gabriel García Márquez"},
    {"id": 2, "title": "El Principito", "author": "Antoine de Saint-Exupéry"},
    {"id": 3, "title": "1984", "author": "George Orwell"}
]

@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books), 200

@app.route('/books/search', methods=['GET'])
def search_book():
    query = request.args.get('q', '')
    results = [b for b in books if query.lower() in b['title'].lower()]
    return jsonify(results), 200

@app.route('/books', methods=['POST'])
def add_book():
    data = request.get_json()
    data["id"] = len(books) + 1
    books.append(data)
    time.sleep(0.5)  # Simulamos un pequeño retraso
    return jsonify({"message": "Book added"}), 201

if __name__ == "__main__":
    app.run(debug=True)
