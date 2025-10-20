
import numpy as np
import pickle
import pandas as pd
import streamlit as st

# Load the trained model
import pickle
loaded_model = pickle.load(open('C:/Users/USER/Downloads/ML laptop price prediction/Gedeon_laptop_price_prediction.pkl', 'rb'))
def laptop_price_prediction(Brand,processor_speed, RAM_size, storage_capacity,Screen_Size,Weight):
    # Create a dataframe for the model
    new_laptop = pd.DataFrame([{
        'Brand':Brand,
        'Processor_Speed':Processor_Speed,
        'RAM_Size':RAM_Size,
        'Storage_Capacity':Storage_Capacity,
        'Screen_Size':Screen_Size,
        'Weight':Weight,
    }])
    
    # Predict the price
    predicted_price = loaded_model.predict(new_laptop)
    return predicted_price[0]

def main():
    st.title('GEDEON lAPTOP PRICE PREDICTION SYSTEM') #System naming

    # Input fields
    Brand = st.text_input('Enter the Brand')
    Processor_Speed = st.text_input('Enter the Processor_Speed')
    RAM_Size = st.text_input('Enter RAM_Size')
    Storage_Capacity = st.text_input('Enter Storage_Capacity')
    Screen_Size = st.text_input('Enter Screen_Size')
    Weight = st.text_input('Enter Weight')

    if st.button('Predict Price'):
        # Convert inputs to numeric types
        try:
            Brand = int(Brand)
            Processor_Speed = float(Processor_Speed)
            RAM_Size = int(RAM_Size)
            Storage_Capacity = int(Storage_Capacity)
            Screen_Size = float(Screen_Size)
            Weight = float(Weight)
            
            # Get prediction
            price = laptop_price_prediction(Brand,Processor_Speed, RAM_Size, Storage_Capacity,Screen_Size,Weight)
            st.success(f'The predicted price for the laptop is: ${price:.2f}')
        except ValueError:
            st.error("Please enter valid numeric values for Processor_Speed, RAM_Size, Storage_Capacity, Screen_Size and Weight.")
if __name__=='__main__':
    main()