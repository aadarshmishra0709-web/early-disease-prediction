import streamlit as st
import pandas as pd
import joblib


# --------------------------------------------------
# Load model and symptom features
# --------------------------------------------------

model = joblib.load("models/disease_model.pkl")
features = joblib.load("models/feature_names.pkl")


# --------------------------------------------------
# Page configuration
# --------------------------------------------------

st.set_page_config(
    page_title="Early Disease Prediction",
    page_icon="🩺",
    layout="wide"
)


# --------------------------------------------------
# Custom CSS
# --------------------------------------------------

st.markdown("""
<style>

    /* Main background */
    .stApp {
        background-color: #0f172a;
    }

    /* Main title */
    .main-title {
        font-size: 48px;
        font-weight: 700;
        text-align: center;
        margin-bottom: 5px;
        color: #f8fafc;
    }

    /* Subtitle */
    .subtitle {
        text-align: center;
        font-size: 18px;
        color: #94a3b8;
        margin-bottom: 35px;
    }

    /* Section headings */
    .section-title {
        font-size: 25px;
        font-weight: 600;
        color: #f8fafc;
        margin-top: 15px;
        margin-bottom: 15px;
    }

    /* Result card */
    .result-card {
        background: linear-gradient(
            135deg,
            #172554,
            #1e3a8a
        );
        padding: 30px;
        border-radius: 18px;
        text-align: center;
        margin-top: 25px;
        border: 1px solid #334155;
    }

    .result-label {
        color: #93c5fd;
        font-size: 16px;
        margin-bottom: 8px;
    }

    .result-disease {
        color: white;
        font-size: 32px;
        font-weight: 700;
    }

    /* Information card */
    .info-card {
        background-color: #1e293b;
        padding: 22px;
        border-radius: 15px;
        border: 1px solid #334155;
        margin-top: 20px;
    }

    .info-title {
        color: #f8fafc;
        font-size: 20px;
        font-weight: 600;
    }

    .info-text {
        color: #cbd5e1;
        font-size: 15px;
        line-height: 1.6;
    }

    /* Footer */
    .footer {
        text-align: center;
        color: #64748b;
        font-size: 13px;
        margin-top: 40px;
        padding: 20px;
    }

</style>
""", unsafe_allow_html=True)


# --------------------------------------------------
# Header
# --------------------------------------------------

st.markdown(
    '<div class="main-title">🩺 Early Disease Prediction</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Machine Learning-Based Symptom Analysis System'
    '</div>',
    unsafe_allow_html=True
)


# --------------------------------------------------
# About section
# --------------------------------------------------

st.markdown(
    '<div class="info-card">'
    '<div class="info-title">🔬 About the System</div>'
    '<div class="info-text">'
    'This system uses a machine learning model trained on symptom-based '
    'health data to predict a possible disease from the symptoms selected '
    'by the user.'
    '</div>'
    '</div>',
    unsafe_allow_html=True
)


# --------------------------------------------------
# Symptom selection
# --------------------------------------------------

st.markdown(
    '<div class="section-title">🔍 Select Your Symptoms</div>',
    unsafe_allow_html=True
)

selected_symptoms = st.multiselect(
    "Search and select the symptoms you are experiencing:",
    options=features,
    placeholder="Start typing to search symptoms..."
)


# --------------------------------------------------
# Selected symptom count
# --------------------------------------------------

if selected_symptoms:

    st.caption(
        f"✅ {len(selected_symptoms)} symptom(s) selected"
    )


# --------------------------------------------------
# Buttons
# --------------------------------------------------

col1, col2, col3 = st.columns([1, 1, 2])

with col1:

    predict_button = st.button(
        "🔍 Predict Disease",
        use_container_width=True
    )

with col2:

    clear_button = st.button(
        "🔄 Clear",
        use_container_width=True
    )


# Clear selection
if clear_button:

    st.rerun()


# --------------------------------------------------
# Prediction
# --------------------------------------------------

if predict_button:

    if not selected_symptoms:

        st.warning(
            "⚠️ Please select at least one symptom before predicting."
        )

    else:

        # Create input vector
        input_data = pd.DataFrame(
            0,
            index=[0],
            columns=features
        )

        # Set selected symptoms to 1
        for symptom in selected_symptoms:

            input_data[symptom] = 1

        # Prediction
        prediction = model.predict(input_data)[0]

        # Probability
        probabilities = model.predict_proba(input_data)[0]

        max_probability = probabilities.max() * 100

        # --------------------------------------------------
        # Result
        # --------------------------------------------------

        st.markdown(
            '<div class="result-card">'
            '<div class="result-label">Predicted Disease</div>'
            f'<div class="result-disease">🩺 {prediction}</div>'
            '</div>',
            unsafe_allow_html=True
        )

        # --------------------------------------------------
        # Confidence
        # --------------------------------------------------

        st.subheader("Model Confidence")

        st.progress(
            min(max_probability / 100, 1.0)
        )

        st.write(
            f"**{max_probability:.2f}%**"
        )

        st.caption(
            "This is a model-estimated probability based on the "
            "training dataset. It should not be interpreted as the "
            "probability that a person actually has the disease."
        )


# --------------------------------------------------
# Disclaimer
# --------------------------------------------------

st.divider()

st.warning(
    "⚠️ Medical Disclaimer: This application is an educational "
    "machine-learning project and is not a medical diagnostic tool. "
    "Predictions should not replace evaluation or advice from a "
    "qualified healthcare professional."
)


# --------------------------------------------------
# Footer
# --------------------------------------------------

st.markdown(
    '<div class="footer">'
    'Early Disease Prediction System • Machine Learning Project'
    '</div>',
    unsafe_allow_html=True
)