from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return {
        'mensaje': '¡Flask está ejecutándose!',
        'estado': True,
    }

if __name__ == "__main__":
    app.run(debug=True)
