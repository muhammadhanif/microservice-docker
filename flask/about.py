from flask import Flask
import socket

app = Flask(__name__)

@app.route("/about")
def about():
    html = "<b>Page:</b> {page}<br/>" \
           "<b>Served by:</b> {hostname} container" \
           "<p>Go to <a href='/'>home</a><br />" \
	   "Go to <a href='/product'>product</a><br />"
    return html.format(page="About", hostname=socket.gethostname())

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
