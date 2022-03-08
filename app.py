import streamlit as st
import random
import time
st.text_input("Your name", key="name")

# You can access the value at any point with:
name=st.session_state.name

i=0
if name=="dtt":
    while True:
        r1 = random.randint(0, 10)
        for i in range(1):
            i=i+1
        st.write(r1*1000000000)
        print(r1)
        time.sleep(5)
    # print("dtt")

    
