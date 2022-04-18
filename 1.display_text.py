import streamlit as st

# set title
st.title("Title")

# set header
st.header("Header")

# set subheader
st.subheader("Sub Header")

# set text
st.text("It is text")

# creating markdow (Markdown Cheatsheet)
st.markdown(""" # h1 tag
## h2 tag
### h3 tag
:moon:<br>
:sunglasses:  
""", True)

# showing latex expression
st.latex(r''' a + ar + a r^2 + \sum''')

# it is powerful function, it can do almost everythings
st.write(sum)