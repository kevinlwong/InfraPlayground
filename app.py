
from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "Hello from EC2! This is Kevin's new message speaking!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
