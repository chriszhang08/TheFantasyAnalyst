from flask import Flask, request
# import Main

app = Flask(__name__)

@app.route('/')
def index():
    return 'chris' # render_template('index.html')

@app.route('/analyze/', methods = ['POST'])
def analyze():
    data = request.form
    return data # render_template('index.html')


if __name__ == '__main__':
    app.run(port=80)
