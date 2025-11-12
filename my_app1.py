import streamlit as st
import requests
import json

st.set_page_config(page_title="ReplyGenius", page_icon="💬")

st.title("💬 ReplyGenius – Never Write a Review Reply Again")
st.write("Paste any Google/Yell/TripAdvisor review. Get a perfect reply in 3s.")

review = st.text_area("Paste the review here:", height=150)

tone = st.selectbox("Tone", ["Warm & Grateful", "Professional & Apologetic", "Playful & Fun"])
business_name = st.text_input("Your Business Name", "The Codfather Fish & Chips")

if st.button("Generate Perfect Reply"):
    with st.spinner("Crafting..."):
        # Hugging Face API (FREE, no key)
        API_URL = "https://api-inference.huggingface.co/models/microsoft/DialoGPT-medium"
        headers = {"Content-Type": "application/json"}
        
        prompt = f"""
        You are a world-class community manager for {business_name}.
        Write a polite, unique, human-sounding reply to this review.
        Use the customer's name if mentioned. Reference 1-2 specific details.
        Tone: {tone}
        
        REVIEW: "{review}"
        
        REPLY (under 100 words):
        """
        
        payload = {
            "inputs": prompt,
            "parameters": {
                "max_new_tokens": 150,
                "temperature": 0.7,
                "return_full_text": False
            }
        }
        
        response = requests.post(API_URL, headers=headers, json=payload)
        
        if response.status_code == 200:
            reply = response.json()[0]["generated_text"].strip()
        else:
            reply = "Sorry, API is warming up. Try again in 30s! (Free tier limit)"
    
    st.success("Done!")
    st.markdown(f"**Your Perfect Reply:**\n\n{reply}")
    st.code(reply, language=None)  # Easy copy
