import tkinter as tk
from tkinter import messagebox
from twilio.rest import Client
import random

# Your Twilio Account SID and Auth Token
account_sid = 'AC0b6708bfcda7be67569f1b7a95d175bb'
auth_token = 'RL7V3ZHR74A89WWK96T4YLNY'

# Function to send OTP via SMS
def send_otp():
    # Create a Twilio client
    client = Client(account_sid, auth_token)

    # Recipient's phone number (in E.164 format, e.g., +1234567890)
    to_phone_number = recipient_phone_entry.get()

    # Generate a random 6-digit OTP
    otp = ''.join([str(random.randint(0, 9)) for _ in range(6)])

    # Send the OTP via SMS
    message = client.messages.create(
        to=8766422290,
        from_='+15054658331',
        body=f'Your OTP is: {otp}'
    )

    # Show a confirmation message
    messagebox.showinfo("OTP Sent", f"OTP sent to {to_phone_number}: {otp}")

# Create a Tkinter window
window = tk.Tk()
window.title("OTP Sender via SMS")

# Create and place widgets
label = tk.Label(window, text="Enter Recipient's Phone Number:")
label.pack()

recipient_phone_entry = tk.Entry(window)
recipient_phone_entry.pack()

send_button = tk.Button(window, text="Send OTP", command=send_otp)
send_button.pack()

# Start the Tkinter main loop
window.mainloop()
