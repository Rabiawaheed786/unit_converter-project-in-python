import streamlit as st

# function to convert units based on predefined  conversion factors or fprmulas
def convert_units(value, unit_from, unit_to):
    conversions = {
        "meters_kilometers": 0.001,  # 1 meter = 0.001 kilometer
        "kilometers_meters": 1000,    # 1 kilometer = 1000 meters
        "grams_kilograms": 0.001,      # 1 gram = 0.001 kilogram
        "kilograms_grams": 1000        # 1 kilogram = 1000 grams
    }

    key = f"{unit_from}_{unit_to}"  # Generate a key based on the input and output units

    if key in conversions:
        conversion = conversions[key]
        # if the conversion factor exists, use it to convert the value
        return value * conversion
    else:
        return "Conversion not supported"

# Streamlit UI code
st.title("Unit Converter")# set the title of the web app
# user input:numerical value to convert
value = st.number_input("Enter the value:")
#dropdown to select unit to convert from
unit_from = st.selectbox("Convert from:", ["meters", "kilometers", "grams", "kilograms"])
unit_to = st.selectbox("Convert to:", ["meters", "kilometers", "grams", "kilograms"])

if st.button("Convert"):
    result = convert_units(value, unit_from, unit_to)
    st.write(f"Converted Value: {result}")

