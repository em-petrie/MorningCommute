import sched, time 

from twilio.rest import Client
from twilio_credentials import cellphone, twilio_account, twilio_token, twilio_number

from secrets import sr_number, train_code, bus_code


sched = sched.scheduler(time.time, time.sleep)

# transperth var
srnumber = sr_number
train = train_code
bus = bus_code

# send text message to infoline
def send_prompt(srnumber, bus, train):
    account = twilio_account
    token = twilio_token
    client = Client(account, token)

    client.messages.create(to = cellphone,
        from_ = twilio_number,
        body = (srnumber, train, bus)
        )

# send check balance prompt for tuesdays
sched.every().tuesday.at("08:20").do(send_prompt, srnumber)
# check train timetable for tuesdays
sched.every().tuesday.at("8:24").do(send_prompt, train)
# check bus timetable for tuesdays
sched.every().tuesday.at("8:22").do(send_prompt, bus)

# add friday schedule here

# test weekends here

# do test 
sched.every().day.at().do(send_prompt, train)

# update 
while True:
    sched.run_pending()
    time.sleep(2)

