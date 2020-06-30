from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    content = [
        'section:1',
        'section:2',
        'section:3',
    ]
    return render_template('index.html', title='home', pragraphs=content)

if __name__ == "__main__":
    app.run(debug=True)
