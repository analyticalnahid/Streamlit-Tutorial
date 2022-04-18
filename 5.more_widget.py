import streamlit as st
import pandas as pd
import time
import matplotlib.pyplot as plt

plt.style.use("ggplot")

# data
data = {
    "num": [x for x in range(1,11)],
    "square": [x*x for x in range(1,11)],
    "twice": [x*2 for x in range(1,11)],
    "thrice": [x*3 for x in range(1,11)],
}

# dataframe
df = pd.DataFrame(data)

# sidebar
rd = st.sidebar.radio("Navigation", ["Home","About Us"])

# home page
if rd == "Home":
    try:
        col = st.sidebar.multiselect("Select",df.columns)
        st.set_option('deprecation.showPyplotGlobalUse', False)
        plt.plot(df["num"], df[col])
        plt.xlabel("X Label")
        plt.ylabel("Y Label")
        st.pyplot()
    except:
        pass

# about us
if rd == "About Us":
    progress = st.progress(0)
    for i in range(100):
        time.sleep(0.01)
        progress.progress(i+1)

    st.balloons()

    st.error("Error")
    st.info("Information")
    st.warning("Warning")
    st.success("Success")
    st.exception(RuntimeError("Exception"))