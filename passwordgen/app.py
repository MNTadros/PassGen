from flask import Flask, render_template, request
import random
import string

app = Flask(__name__)

# Function to generate a random password
def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

@app.route('/', methods=['GET', 'POST'])
def home():
    quantity = 12  # Default value
    password = ''
    if request.method == 'POST':
        quantity = int(request.form.get('quantity', 12))  # Get quantity from form, default to 12
        password = generate_password(length=quantity)
    return render_template('index.html', password=password, quantity=quantity)

if __name__ == '__main__':
    app.run(debug=True)
