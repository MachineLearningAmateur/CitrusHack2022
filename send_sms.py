from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException


#   phoneNumber
#   className
class Send():

    def __init__(self):
        pass

    def send(self, name : str, phoneNumber : str, msg : str):
        account_sid = "ACc071e2a0b229fcf43b96553040cc5633"
        auth_token  = "65e2ff2ced9a5332eee9632e362912f7"

        client = Client(account_sid, auth_token)

        #validation_request = client.validation_requests.create(friendly_name=name, phone_number=f"+1{phoneNumber}") #only available for non-trial twilio accounts
        message = client.messages.create(to = f"+1{phoneNumber}", from_ ="+19124206054", body = msg)

        print(message.sid)