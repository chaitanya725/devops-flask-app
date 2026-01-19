from flask import Flask
from datetime import datetime
import socket

app = Flask(__name__)

@app.route("/")
def home():
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    hostname = socket.gethostname()

    return f"""
    <h1>Hello from DevOps 🚀</h1>
    <p><strong>Server Time:</strong> {current_time}</p>
    <p><strong>Hostname:</strong> {hostname}</p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

