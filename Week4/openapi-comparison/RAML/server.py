from flask import Flask, jsonify, request

app = Flask(__name__)
app.json.sort_keys = False

# Dữ liệu giả lập
books = [
    {
        "id": "1",
        "title": "Clean Code",
        "author": "Robert C. Martin",
        "publishedYear": 2008,
        "genre": "Software Engineering"
    }
]

@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books)

@app.route('/books', methods=['POST'])
def create_book():
    data = request.json
    new_book = {
        "id": str(len(books) + 1),
        "title": data.get('title'),
        "author": data.get('author'),
        "publishedYear": data.get('publishedYear'),
        "genre": data.get('genre')
    }
    books.append(new_book)
    return jsonify(new_book), 201

@app.route('/books/<id>', methods=['GET'])
def get_book(id):
    book = next((b for b in books if b['id'] == id), None)
    if book:
        return jsonify(book)
    return jsonify({"error": "Book not found"}), 404

@app.route('/books/<id>', methods=['PUT'])
def update_book(id):
    book = next((b for b in books if b['id'] == id), None)
    if not book:
        return jsonify({"error": "Book not found"}), 404
    
    data = request.json
    book.update({
        "title": data.get('title', book['title']),
        "author": data.get('author', book['author']),
        "publishedYear": data.get('publishedYear', book['publishedYear']),
        "genre": data.get('genre', book['genre'])
    })
    return jsonify(book)

@app.route('/books/<id>', methods=['DELETE'])
def delete_book(id):
    global books
    book = next((b for b in books if b['id'] == id), None)
    if not book:
        return jsonify({"error": "Book not found"}), 404
    
    books = [b for b in books if b['id'] != id]
    return '', 204

if __name__ == '__main__':
    print("RAML Test Server đang chạy tại http://localhost:5000")
    app.run(port=5000, debug=True)
