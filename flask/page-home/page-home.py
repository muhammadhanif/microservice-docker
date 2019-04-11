from flask import Flask, render_template
import socket

app = Flask(__name__)

@app.route("/")
def home():
    page = "Home"
    hostname = socket.gethostname()

    return render_template('page-home.html', page = page, hostname = hostname)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
