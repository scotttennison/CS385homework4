from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>CS385 Homework 4 - CI/CD Pipeline</h1><p>Deployed with GitHub Actions and AWS!</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)