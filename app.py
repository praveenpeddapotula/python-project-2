from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, World!"

if __name__ == "__main__":
    # The application runs on port 8000 (this can be customized)
    app.run(host="0.0.0.0", port=8000)
