from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to Hero Vired Flask CI/CD Assignment!"

@app.route("/health")
def health():
    return {
        "status": "UP",
        "application": "Flask CI/CD",
        "version": "1.0"
    }

if __name__ == "__main__":
    app.run(debug=True)