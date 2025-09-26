import pytest
from app import app, db
from server.models import Message

class TestMessage:
    def setup_method(self):
        with app.app_context():
            db.drop_all()
            db.create_all()
            msg = Message(username="Liza", body="Hello 👋")
            db.session.add(msg)
            db.session.commit()

    def test_message_body(self):
        with app.app_context():
            msg = Message.query.filter_by(username="Liza").first()
            assert msg.body == "Hello 👋"
