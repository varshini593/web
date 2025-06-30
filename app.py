from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/internet')
def internet():
    return render_template('internet.html')

@app.route('/food')
def food():
    return render_template('food.html')

@app.route('/health')
def health():
    return render_template('health.html')

if __name__ == '__main__':
    app.run(debug=True)
