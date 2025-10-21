from flask import Flask, jsonify, request, redirect, render_template
app = Flask(__name__)
# Sample data: a list of fruits
fruits = [
    {"id": 1, "name": "Apple"},
    {"id": 2, "name": "Banana"},
    {"id": 3, "name": "Cherry"},
]

@app.route('/')
def index():
    return redirect('/fruits')
    return render_template('index.html', fruits=fruits)

# Get the list of fruits
@app.route('/fruits', methods=['GET'])
def get_fruits():
    return jsonify(fruits)

# Add a new fruit
# eg curl -X POST http://127.0.0.1:5001/fruits -H "Content-Type: application/json" -d "{\"name\": \"Orange\"}"
@app.route('/fruits', methods=['POST'])
def add_fruit():
    new_fruit = request.get_json()
    new_fruit['id'] = len(fruits) + 1
    fruits.append(new_fruit)
    return jsonify(new_fruit), 201

# Update an existing fruit
# eg curl -X PUT http://127.0.0.1:5001/fruits/1 -H "Content-Type: application/json" -d "{\"name\": \"Green Apple\"}" 
@app.route('/fruits/<int:fruit_id>', methods=['PUT'])
def update_fruit(fruit_id):
    fruit = next((fruit for fruit in fruits if fruit['id'] == fruit_id), None)
    if fruit is None:
        return jsonify({'error': 'Fruit not found'}), 404
    
    updated_data = request.get_json()
    fruit.update(updated_data)
    return jsonify(fruit)

# Delete a fruit
@app.route('/fruits/<int:fruit_id>', methods=['DELETE'])
def delete_fruit(fruit_id):
    global fruits
    fruits = [fruit for fruit in fruits if fruit['id'] != fruit_id]
    return jsonify({'message': 'Fruit deleted'}), 204
if __name__ == '__main__':
    app.run(debug=True)