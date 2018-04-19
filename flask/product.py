from flask import Flask
import socket

app = Flask(__name__)

@app.route("/product")
def product():
    html = "<b>Page:</b> {page}<br/>" \
           "<b>Served by:</b> {hostname} container" \
           "<p>Go to <a href='/'>home</a><br />" \
	   "Go to <a href='/about'>about</a><br />"
    return html.format(page="Product", hostname=socket.gethostname())

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
