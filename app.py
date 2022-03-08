import streamlit as st
import random
import time
from twilio.rest import Client
st.text_input("Your name++", key="name")

# You can access the value at any point with:
name=st.session_state.name
client = Client("ACe1cd9a2445658516046b7aa3ea29594b","5bf7b085a913e038ad56963d3cf69a79")


def msg(m):
        message=client.messages.create(body=m,from_="whatsapp:+14155238886",to="whatsapp:+916303247774")
i=0

if name=="dtt":
    while True:
        r1 = random.randint(0, 10)
        for i in range(1):
            i=i+1
        st.write(r1*100)
        msg(r1)

        print(r1)
        time.sleep(5)
    # print("dtt")

    
