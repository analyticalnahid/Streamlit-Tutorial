import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import matplotlib.pyplot as plt

# dataframe
data = pd.DataFrame(np.random.randn(100,3), columns= ['a','b','c'])

# showing Altair Chart
chart = alt.Chart(data).mark_circle().encode(x='a', y='b', tooltip=['a','b'])
st.altair_chart(chart, use_container_width=True)

# showing graphviz Chart
st.graphviz_chart("""
digraph{
    watch -> like
    like -> share
    share -> subscribe
}
""")

# showing map
st.map()

# showing matplotlib graph
st.set_option('deprecation.showPyplotGlobalUse', False)
plt.scatter(data['a'], data['b'])
plt.title("Scatter")
plt.xlabel("X Label")
plt.ylabel("Y Label")
st.pyplot()

# showing different chart
st.line_chart(data)
st.area_chart(data)
st.bar_chart(data)

# showing media (image, audio, video)
st.image("write.PNG")
st.audio()
st.video()