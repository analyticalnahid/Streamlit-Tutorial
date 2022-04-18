import streamlit as st

# button
if st.button("Click") == True:
    st.write("It's clicked")
else:
    st.write("Not clicked")    

# text input
name = st.text_input("Name")
st.write(name)

# text box
address = st.text_area("Address")
st.write(address)

# date picker
st.date_input("enter date")

# time picker
st.time_input("enter time")

# checkbox
if st.checkbox("Accept Terms & Condition", value = False) == True:
    st.write("Thank you!")
else:
    st.write("Please accept box")    

# radio button
st.radio("Colors", ['r','g','b'], index= 1)

# dropdown menu
st.selectbox("Colors", ['r','g','b'], index= 0)

# multi select
st.multiselect("Colors", ['r','g','b'])

# slider
st.slider("Range", min_value= 10, max_value= 100, step = 5)

# increment/decrement
st.number_input("Top & Down", min_value= 10.0, max_value= 100.0, step = 5.0)

# upload file
image = st.file_uploader("Upload file")
st.write(image)