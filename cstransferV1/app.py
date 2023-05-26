from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/index.html')
def index1():
    return render_template('index.html')

@app.route('/FAQ.html')
def FAQ():
    return render_template('FAQ.html')

@app.route('/about.html')
def about():
    return render_template('about.html')

@app.route('/players.html')
def players():
    return render_template('players.html')

@app.route('/teams.html')
def teams():
    return render_template('teams.html')

@app.route('/hello/<name>')
def hello(name):
    return render_template('page.html', name=name)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')