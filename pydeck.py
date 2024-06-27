import streamlit as st
import pandas as pd
import numpy as np

# Map Making App
st.title("Map Making App")

# Add a slider to the sidebar:
add_selectbox = st.sidebar.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0)
)

# Create a map:
map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.map(map_data)

# Add some text:
st.write("Here's a map of New York!")

# Run the Streamlit app: Use the streamlit run command in your terminal
# streamlit run [filename]
