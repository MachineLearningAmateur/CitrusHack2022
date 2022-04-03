from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException
from authentication import account_sid
from authentication import auth_token

class Send():

    def __init__(self):
        pass

    def send(self, name : str, phoneNumber : str, msg : str):
  
        client = Client(account_sid, auth_token)

        #validation_request = client.validation_requests.create(friendly_name=name, phone_number=f"+1{phoneNumber}") #only available for non-trial twilio accounts
        message = client.messages.create(to = f"+1{phoneNumber}", from_ ="+19124206054", body = msg)

        print(message.sid)