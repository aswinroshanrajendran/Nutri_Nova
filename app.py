import streamlit as st
import pandas as pd
import joblib
import base64

# Load the trained pipeline/model
MODEL_PATH = r"F:/Aswin/01 epita/Interview Prep/ESPAUK/New food innovation pvt/Project/notebooks/final_random_forest_model.pkl"
pipeline = joblib.load(MODEL_PATH)

# Logo and Background image paths
logo_path = "F:/Aswin/01 epita/Interview Prep/ESPAUK/New food innovation pvt/Project/app/generated-image.png"
background_path = "F:/Aswin/01 epita/Interview Prep/ESPAUK/New food innovation pvt/Project/app/7892917.jpg"

# Set background from local file
def set_bg_from_local(image_path):
    with open(image_path, "rb") as img_file:
        b64_string = base64.b64encode(img_file.read()).decode()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/png;base64,{b64_string}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
        }}
        .stButton>button {{
            border-radius: 12px;
            padding: 0.6em 2em;
            font-size: 1.1em;
            transition: all 0.3s ease;
            background-color: #4CAF50;
            color: white;
        }}
        .stButton>button:hover {{
            background-color: #45a049;
            transform: scale(1.05);
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Nutri-score mapping
SCORE_MAP = {
    1: ('A', '#2ecc71'),
    2: ('B', '#7bed8d'),
    3: ('C', '#f1c40f'),
    4: ('D', '#e67e22'),
    5: ('E', '#e74c3c'),
}

HEALTH_TIPS = {
    'A': "Great choice! Low in sugar, fat, and salt. Suitable for most diets.",
    'B': "Good choice! Moderately healthy, but watch intake if you have dietary restrictions.",
    'C': "Average score. Consider moderation, especially if you have health concerns.",
    'D': "Warning: High in sugar, fat, or salt. People with heart conditions or diabetes should avoid frequent consumption.",
    'E': "High risk: Very high sugar, fat, or salt. Avoid if you have heart disease, diabetes, or other related conditions.",
}

def app_header():
    st.markdown(
    f"""
    <div style='text-align: center;'>
        <img src="data:image/png;base64,{base64.b64encode(open(logo_path, "rb").read()).decode()}" width="200"/>
    </div>
    """,
    unsafe_allow_html=True
)

    st.title("🔬 NutriNova")
    st.markdown(
        """
        This app predicts the **Nutri-Score (A to E)** of a food product based on its nutritional content per 100g.

        The Nutri-Score is a front-of-pack label that helps you quickly understand how healthy a food item is.
        Enter the nutritional values below, and get the predicted score with tailored health advice.
        """
    )
    st.markdown("---")

def get_user_inputs():
    st.subheader("Enter Nutritional Values (per 100g)")
    energy = st.number_input("Energy (kJ)", min_value=0.0, max_value=5000.0, value=400.0, step=1.0)
    fat = st.number_input("Fat (g)", min_value=0.0, max_value=100.0, value=4.2, step=0.1)
    sugars = st.number_input("Sugars (g)", min_value=0.0, max_value=100.0, value=8.5, step=0.1)
    fiber = st.number_input("Fiber (g)", min_value=0.0, max_value=100.0, value=2.0, step=0.1)
    proteins = st.number_input("Proteins (g)", min_value=0.0, max_value=100.0, value=3.5, step=0.1)
    salt = st.number_input("Salt (g)", min_value=0.0, max_value=20.0, value=0.3, step=0.01)
    
    return {
        'energy_100g': energy,
        'fat_100g': fat,
        'sugars_100g': sugars,
        'fiber_100g': fiber,
        'proteins_100g': proteins,
        'salt_100g': salt
    }

def predict_nutriscore(nutrition_data):
    df = pd.DataFrame([nutrition_data])
    pred_numeric = pipeline.predict(df)[0]
    letter, color = SCORE_MAP.get(pred_numeric, ('Unknown', '#000000'))
    tip = HEALTH_TIPS.get(letter, "No advice available.")
    return letter, color, tip

def display_result(letter, color, tip):
    st.markdown("### Predicted Nutri-Score")
    st.markdown(
        f"""
        <div style="
            background-color: {color};
            color: white;
            padding: 15px;
            width: 120px;
            font-size: 48px;
            font-weight: 700;
            text-align: center;
            border-radius: 12px;
            margin-bottom: 10px;
        ">{letter}</div>
        """,
        unsafe_allow_html=True,
    )
    st.subheader("Health Advice")
    st.info(tip)

def main():
    st.set_page_config(page_title="NutriNova", layout="centered")

    set_bg_from_local(background_path)
    app_header()

    user_input = get_user_inputs()

    if st.button("Predict Nutri-Score"):
        letter, color, tip = predict_nutriscore(user_input)
        display_result(letter, color, tip)

    st.markdown("---")
    st.markdown(
        "<small>Created by Aswin | NutriScore is a simple, color-coded nutrition label to help consumers make healthier food choices.</small>",
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()
