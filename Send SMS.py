print('This is a SMS System')

# Account SID : ACa0c16b8afe7c59e8e357ff700ae16063
# AuTH Token : 074852da5e0cb95ce2704bab8ff185f7
# Phone: +13264446157
from twilio.rest import Client
account_sid = 'ACa0c16b8afe7c59e8e357ff700ae16063'
auth_token = '074852da5e0cb95ce2704bab8ff185f7'
client = Client(account_sid, auth_token)

message = client.messages.create(
    messaging_service_sid='MG169659d71b007598b3c8de843ffbae8d',
    body='Good evening Hridoy!',
    to='+8801723845401'
)

print(message.sid)
print("SMS Done!")

