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
     #logic to convert units
    if key in conversions:
        conversion = conversions[key]
        # if the conversion factor exists, use it to convert the value
        return value * conversion
    else:
        return "Conversion not supported" #return a message if the conversion is not suported


st.title("Unit Converter")# set the title of the web app
# user input:numerical value to convert
value = st.number_input("Enter the value:",main_value=1.0, steps=1.0)
#dropdown to select unit to convert from
unit_from = st.selectbox("Convert from:", ["meters", "kilometers", "grams", "kilograms"])
#dropdown to select unit to convert tp
unit_to = st.selectbox("Convert to:", ["meters", "kilometers", "grams", "kilograms"])

# button to trigger the conversion
if st.button("Convert"):
    result = convert_units(value, unit_from, unit_to) #  call the conversion function
    st.write(f"Converted Value: {result}") #display the  result

# Footer
st.markdown("<div class='footer'>© 2025 Unit Converter | Developed by Rabia Waheed</div>",