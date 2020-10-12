from twilio.rest import Client

account_sid = 'AC3ff4eb2cb93e5ddb3d07b64e03c1cb54'
auth_token = '1b7b829979e9f1ad9d482be3f90d7f6e'
client = Client(account_sid, auth_token)

message = client.messages.create(
    from_='+12056914156',
    body='I am learning how to send the messages through python!',
    to='+918050106439'
)

print(message.sid)
