import pytest
from app import app, db
from server.models import Message

class TestApp:
    def setup_method(self):
        # create a clean test database
        with app.app_context():
            db.drop_all()
            db.create_all()
            # seed some data
            msg = Message(username="Liza", body="Hello 👋")
            db.session.add(msg)
            db.session.commit()

    def test_message_exists(self):
        with app.app_context():
            m = Message.query.all()
            assert any(message.body == "Hello 👋" and message.username == "Liza" for message in m)
