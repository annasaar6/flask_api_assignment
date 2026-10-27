# Import required Flask modules
from flask import Flask, request, jsonify

# Create Flask application
app = Flask(__name__)


# ----------------------------
# Helper Function
# Demonstrates functions
# ----------------------------
def calculate_sum(numbers):
    """
    Returns the sum of a list of numbers.
    """
    return sum(numbers)


# ----------------------------
# GET Endpoint
# /hello?name=John
# ----------------------------
@app.get("/hello")
def hello():
    # Get optional query parameter
    name = request.args.get("name")

    # Demonstrates if/else control flow
    if name:
        message = f"Hello, {name}!"
    else:
        message = "Hello, World!"

    return jsonify({
        "message": message,
        "status": "success"
    })


# ----------------------------
# POST Endpoint
# /sum
# ----------------------------
@app.post("/sum")
def add_numbers():

    # Get JSON data from request
    data = request.get_json()

    # Error Handling
    if not data:
        return jsonify({
            "error": "No JSON data provided"
        }), 400

    # Check required field exists
    if "numbers" not in data:
        return jsonify({
            "error": "Missing 'numbers' field"
        }), 400

    numbers = data["numbers"]

    # Ensure numbers is a list
    if not isinstance(numbers, list):
        return jsonify({
            "error": "'numbers' must be a list"
        }), 400

    # Ensure all items are numeric
    if not all(isinstance(num, (int, float)) for num in numbers):
        return jsonify({
            "error": "All list items must be numbers"
        }), 400

    total = calculate_sum(numbers)

    return jsonify({
        "numbers": numbers,
        "sum": total,
        "status": "success"
    })


# Run local server on port 5000
if __name__ == "__main__":
    app.run(debug=True, port=5000)