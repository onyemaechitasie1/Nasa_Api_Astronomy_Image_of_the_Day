import streamlit as st
import requests

st.set_page_config(layout="wide")

# Preparing API key and API url
url = ("https://api.nasa.gov/planetary/apod?"
       "api_key=Sn9EyruOLU7jIfn71LSXb6Dm2D6urlVisQrAntxa")

# Get the request data as directory
response1 = requests.get(url)
content1 = response1.json()

# Extract the image title, url and explanation
title = content1["title"]
date = content1["date"]
image_url = content1["url"]
explanation = content1["explanation"]

# Download the image
image_filepath = "img.png"
response2 = requests.get(image_url)
content2 = response2.content
with open (image_filepath, "wb") as file:
    file.write(content2)

# Calling streamlit
st.title(title)
st.image(image_filepath)
st.write(explanation)
st.write("DATE:", date)