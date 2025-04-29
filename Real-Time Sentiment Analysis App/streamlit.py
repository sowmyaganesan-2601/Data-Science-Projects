# app.py

import streamlit as st
import pickle
import string

# Load model and vectorizer
model = pickle.load(open('sentiment_model.pkl', 'rb'))
tfidf = pickle.load(open('tfidf_vectorizer.pkl', 'rb'))

# Clean text function
def clean_text(text):
    text = text.lower()
    no_numbers = ''.join([char for char in text if not char.isdigit()])
    no_punct = ''.join([char for char in no_numbers if char not in string.punctuation])
    return no_punct

# Streamlit page config
st.set_page_config(
    page_title="Sentiment Analyzer",
    page_icon="🧠",
    layout="centered",
  
)


# Sidebar
st.sidebar.title("⚙️ Settings")
st.sidebar.markdown("Customize your analysis below.")

# About section
with st.expander("ℹ️ About this App"):
    st.markdown("""
    This **Real-Time Sentiment Analyzer** uses Machine Learning to predict the sentiment 
    (Positive, Negative, or Neutral) of the text you input.

    **Technologies Used:**  
    - Python 🐍  
    - Streamlit 🌟  
    - Scikit-learn 🔥
    """)

# Main app layout
st.title("🧠 Real-Time Sentiment Analyzer")
st.write("Analyze the sentiment of your text instantly!")

# Text input
user_input = st.text_area("✍️ Enter your text here:")

# Analyze Button
if st.button("🔍 Analyze Sentiment"):
    if user_input.strip() == "":
        st.warning("⚠️ Please enter some text first.")
    else:
        with st.spinner('Analyzing... Hang tight! ⏳'):
            cleaned_input = clean_text(user_input)
            vectorized_input = tfidf.transform([cleaned_input])
            prediction = model.predict(vectorized_input)
            confidence = model.predict_proba(vectorized_input)

        # Show result
        if prediction[0] == 'positive':
            st.success("✅ Positive Sentiment Detected!")
        elif prediction[0] == 'negative':
            st.error("❌ Negative Sentiment Detected!")
        else:
            st.info("ℹ️ Neutral Sentiment Detected!")

        st.markdown(f"**Confidence Level:** `{confidence.max()*100:.2f}%`")

# Footer
st.markdown("---")
st.caption("© 2025 Real-Time Sentiment Analyzer | Built with Python & Streamlit")

