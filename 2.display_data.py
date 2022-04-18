import streamlit as st
import pandas as pd
import time
import numpy as np

# creating nd array
arr = [1,2,3,4,5,6]
np_arr = np.array(arr)
nd = np_arr.reshape((2,3))

# creating dictionary
dict = {
    "name": ["Md Yousuf, Nahidul Islam"],
    "age": [19,20],
    "hobby": ["programming, coding"]
}

# reading csv
data = pd.read_csv("play_tennis.csv")

# showing csv
st.dataframe(data, width= 300, height= 200)
# showing array
st.dataframe(nd)
# showing dictionary
st.write(dict)
st.table(data)
st.json(dict)

#caching
@st.cache
def ret_time(a):
    time.sleep(5)
    return time.time()
if st.checkbox("1"):
    st.write(ret_time(1))

if st.checkbox("2"):
    st.write(ret_time(2))        