import streamlit as st
import plotly.express as px
from backend import get_data

IMAGES_PATH  = "images"
SKY_CONDITION_IMAGES= {"Clear" : f"{IMAGES_PATH}/clear.png",
                       "Clouds" : f"{IMAGES_PATH}/cloud.png",
                       "Rain" : f"{IMAGES_PATH}/rain.png",
                       "Snow" : f"{IMAGES_PATH}/snow.png"}

st.title("Weather Forecast for the next Days")

place = st.text_input("Place")
days = st.slider("Forecast Days", min_value=1, max_value=5, 
                 help="Select the number of forecasted days")
option = st.selectbox("Select data to view", 
                      ("Temperature", "Sky"))

st.subheader(f"{option} for the next {days} days in {place.title()}")

if place:
    data = get_data(place, days)

    if not any(data):
        st.error("That place does not exist.")

    elif option == "Temperature":
        temperatures = [dict["main"]["temp"] for dict in data]
        temperatures = [t / 10 for t in temperatures]
        dates = [dict["dt_txt"] for dict in data]
        figure = px.line(x=dates, y=temperatures, labels={"x": "Date", "y": "Temperature (C)"})

        st.plotly_chart(figure)

    elif option == "Sky" and any(data):
        sky_conditions = filtered_data = [dict["weather"][0]["main"] for dict in data]
        image_paths = [SKY_CONDITION_IMAGES[condition] for condition in sky_conditions]

        st.image(image_paths, width=115)