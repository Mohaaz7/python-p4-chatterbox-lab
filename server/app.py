from flask import Flask
from server.models import db


def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    with app.app_context():
        db.create_all()

    return app


# expose app so tests can import it
app = create_app()

if __name__ == "__main__":
    app.run(debug=True, port=5000)
