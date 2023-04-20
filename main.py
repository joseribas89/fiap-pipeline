from flask import Flask

app = Flask(__name__)

@app.route('/fap')
def fap():
    return 'FAP'

if __name__ == '__main__':
    app.run()
