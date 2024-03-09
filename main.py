from flask import Flask, render_template, url_for

app = Flask(__name__, static_url_path='/static')

@app.route("/")
def home():
    return render_template("index.html",url_for=url_for)  

@app.route("/conversation")
def conversation():
    return render_template("converstion.html") 

@app.route('/mcq')
def mcq():
    return render_template('mcq.html')

@app.route('/oral')
def oral():
    return render_template('oral.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')


if __name__ == "__main__":
    app.run(debug=True)