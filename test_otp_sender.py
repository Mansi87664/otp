import pytest
from unittest.mock import MagicMock, patch
from tkinter import Tk, Entry, Button

# Import the function you want to test
from your_otp_sender_script import send_otp

@pytest.fixture
def tk_app():
    app = Tk()
    yield app
    app.quit()

def test_send_otp(tk_app):
    recipient_phone_entry = Entry(tk_app)
    recipient_phone_entry.insert(0, '+1234567890')

    with patch('twilio.rest.Client.messages.create', MagicMock()) as create_mock:
        send_otp()
        create_mock.assert_called()

    # You can add more assertions here based on your specific requirements

if __name__ == '__main__':
    pytest.main()
