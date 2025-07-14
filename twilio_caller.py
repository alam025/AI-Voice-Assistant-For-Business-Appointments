from twilio.rest import Client

# Use your actual Twilio details
TWILIO_SID = "ACc95f137ef64292ea5bb68d673025bcd5"
TWILIO_AUTH_TOKEN = "6e97a6273ea68849b8170bef5cf2fe3e"
TWILIO_PHONE = "+16193299849"  # Your Twilio number (no spaces!)
TO_PHONE = "+916397685405"     # Your number (must be verified in trial mode)

# Your FastAPI public ngrok URL (copied from ngrok terminal)
TWIML_URL = "https://23fb-2405-201-6826-5813-bd90-38a0-6968-2427.ngrok-free.app/voice"

def make_call():
    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    call = client.calls.create(
        to=TO_PHONE,
        from_=TWILIO_PHONE,
        url=TWIML_URL
    )

    print("✅ Call initiated! SID:", call.sid)

if __name__ == "__main__":
    make_call()
