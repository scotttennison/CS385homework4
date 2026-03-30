from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CS385 Homework 4</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: 'Segoe UI', sans-serif;
            background: linear-gradient(135deg, #1a1a2e, #16213e, #0f3460);
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            color: white;
        }
        .container {
            text-align: center;
            padding: 40px;
            background: rgba(255,255,255,0.05);
            border-radius: 20px;
            border: 1px solid rgba(255,255,255,0.1);
            backdrop-filter: blur(10px);
            max-width: 700px;
            width: 90%;
        }
        .badge {
            background: #e94560;
            color: white;
            padding: 6px 16px;
            border-radius: 20px;
            font-size: 0.85rem;
            display: inline-block;
            margin-bottom: 20px;
            letter-spacing: 1px;
        }
        h1 {
            font-size: 2.5rem;
            margin-bottom: 10px;
            background: linear-gradient(90deg, #e94560, #0f3460);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        p {
            color: rgba(255,255,255,0.6);
            margin-bottom: 30px;
            font-size: 1rem;
        }
        .cards {
            display: flex;
            gap: 15px;
            justify-content: center;
            flex-wrap: wrap;
            margin-top: 20px;
        }
        .card {
            background: rgba(255,255,255,0.08);
            border-radius: 12px;
            padding: 20px;
            width: 150px;
            border: 1px solid rgba(255,255,255,0.1);
            transition: transform 0.2s;
        }
        .card:hover { transform: translateY(-5px); }
        .card .icon { font-size: 2rem; margin-bottom: 8px; }
        .card .label { font-size: 0.85rem; color: rgba(255,255,255,0.7); }
        .status {
            margin-top: 30px;
            display: inline-flex;
            align-items: center;
            gap: 8px;
            background: rgba(0,255,100,0.1);
            border: 1px solid rgba(0,255,100,0.3);
            padding: 8px 20px;
            border-radius: 20px;
            font-size: 0.9rem;
            color: #00ff64;
        }
        .dot {
            width: 8px;
            height: 8px;
            background: #00ff64;
            border-radius: 50%;
            animation: pulse 1.5s infinite;
        }
        @keyframes pulse {
            0%, 100% { opacity: 1; }
            50% { opacity: 0.3; }
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="badge">CS385 HOMEWORK 4</div>
        <h1>CI/CD Pipeline</h1>
        <p>Automated deployment using GitHub Actions, Terraform & AWS</p>
        <div class="cards">
            <div class="card">
                <div class="icon">⚙️</div>
                <div class="label">GitHub Actions</div>
            </div>
            <div class="card">
                <div class="icon">🏗️</div>
                <div class="label">Terraform IaC</div>
            </div>
            <div class="card">
                <div class="icon">☁️</div>
                <div class="label">AWS EC2</div>
            </div>
            <div class="card">
                <div class="icon">🐍</div>
                <div class="label">Python Flask</div>
            </div>
        </div>
        <div class="status">
            <div class="dot"></div>
            Deployed & Running on AWS
        </div>
    </div>
</body>
</html>
"""

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)