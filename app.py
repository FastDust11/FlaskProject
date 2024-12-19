from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

books = [
    {"id": 1, "title": "Władca Pierścieni", "author": "J.R.R. Tolkien"},
    {"id": 2, "title": "Harry Potter", "author": "J.K. Rowling"},
]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/books', methods=['GET'])
def get_books():
    return jsonify(books)

@app.route('/api/books', methods=['POST'])
def add_book():
    data = request.get_json()
    new_book = {
        "id": len(books) + 1,
        "title": data.get("title"),
        "author": data.get("author"),
    }
    books.append(new_book)
    return jsonify(new_book), 201

if __name__ == '__main__':
    app.run(debug=True)
