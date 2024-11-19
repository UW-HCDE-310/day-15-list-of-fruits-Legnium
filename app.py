from flask import Flask, render_template

app = Flask(__name__)
@app.route("/")
def index():
    fruits = [
        {"name": "apples", "quantity": 3},
            {"name": "oranges", "quantity": 2},
            {"name": "strawberries", "quantity": 6}
    ]
    appended_fruit = []
    for fruit in fruits:
        # Check if the name starts with 'o' and quantity is less than 3
        if fruit['name'][0] == 'o' and fruit['quantity'] < 3:
            appended_fruit.append(fruit)

    return render_template("index.html", fruits=appended_fruit)
