def send_sms(text,to_no="+91000000000"):
    from twilio.rest import Client
    account_sid ='#account_id'
    auth_token = '#auth_token'
    client = Client(account_sid, auth_token)
    message = client.messages.create(
      body=text,
      from_="+19804492539",
      to=to_no
    )
    return message.sid
