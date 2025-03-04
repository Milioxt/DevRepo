from flask import Flask

app = Flask(__name__)
@app.route('/') # home or root of website
def index():
    return '<html><head><title>HELLOWORLD </title></head><body><h1>HELLO WORLD</h1></body></html>'

@app.route("/about") #info about this site
def about():
    return '<html><head><title>About this page</title></head><body>Everything about this website. Back to <a href="/">Hello word</a></body></html>'

if __name__ == '__main__':
    app.run(debug=True)