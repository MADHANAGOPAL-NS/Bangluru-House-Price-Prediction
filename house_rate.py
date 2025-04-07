import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import pickle
import numpy as np
from PIL import Image

# Load the trained model
pickle_in = open(r"C:\Users\MADHANAGOPAL N S\Desktop\House Price Prediction\Bengaluru-House-Price-Prediction-main\new_model.pkl", 'rb')
classifier = pickle.load(pickle_in)

def Welcome():
    return 'WELCOME ALL!'

def predict_price(location, sqft, bath, bhk):
    """Predict the house price based on user input.
    ---
    parameters:  
      - name: location
        in: query
        type: text
        required: true
      - name: sqft
        in: query
        type: number
        required: true
      - name: bath
        in: query
        type: number
        required: true
      - name: bhk
        in: query
        type: number
        required: true
    responses:
        200:
            description: The output values
    """
    x = np.zeros(4)
    x[0] = float(sqft)
    x[1] = float(bath)
    x[2] = float(bhk)
    # Note: location is not encoded in this model (add if one-hot encoding is used)

    return classifier.predict([x])[0]

def main():
    st.title("Bangalore House Rate Prediction")

    html_temp = """
    <h2 style="color:black;text-align:left;">Streamlit House Prediction ML App</h2>
    """
    st.markdown(html_temp, unsafe_allow_html=True)

    st.subheader('Please enter the required details:')

    # Dropdown with placeholder-style default option
    location = st.selectbox(
        "Location",
        [
            "Select Location",
            "Electronic City Phase II",
            "Chikka Tirupathi",
            "Uttarahalli",
            "Lingadheeranahalli",
            "Kothanur"
        ]
    )

    sqft = st.text_input("Sq-ft area", "")
    bath = st.text_input("Number of Bathrooms", "")
    bhk = st.text_input("Number of BHK", "")

    result = ""

    if st.button("House Price in Lakhs"):
        if location == "Select Location":
            st.warning("⚠️ Please select a valid location.")
        elif sqft and bath and bhk:
            try:
                result = predict_price(location, sqft, bath, bhk)
                result = np.round(result, 2)
                st.success(f'✅ The estimated price of the house is ₹ {result} Lakhs')
            except ValueError:
                st.error("❌ Please enter valid numeric values for sqft, bath, and bhk.")
        else:
            st.warning("⚠️ Please enter all fields!")

    if st.button("About"):
        st.text("Please find the code at:")
        st.markdown("[GitHub Repo](https://github.com/Shrinaaaath/Bengaluru-House-Price-Prediction)")

if __name__ == '__main__':
    main()
