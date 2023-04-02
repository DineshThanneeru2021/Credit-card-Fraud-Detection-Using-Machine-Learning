"""def send_sms(text,to_no="+919390791487"):
    from twilio.rest import Client
    account_sid ='AC8df3c4d387ee3ec75deb9c77ea3afcfd'
    auth_token = '726827be3cf67aa3581dfb54af338a04'
    client = Client(account_sid, auth_token)
    message = client.messages.create(
      body=text,
      from_="+19804492539",
      to=to_no
    )
    return message.sid"""
