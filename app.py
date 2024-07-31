from flask import Flask
from routes.home_bp import home_bp


app = Flask(__name__)

app.register_blueprint(home_bp, url_prefix='/')


if __name__ == "__main__":
    app.run(port=5000, debug=True)