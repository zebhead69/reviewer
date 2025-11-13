# app.py — PRO UI VERSION (HUGGING FACE)
import streamlit as st
import requests
import json
import time

# --- CONFIG ---
st.set_page_config(page_title="ReplyGenius", page_icon="💬", layout="centered")

# --- CUSTOM CSS (MAKES IT LOOK £1M) ---
st.markdown("""
<style>
    .main {background-color: #f8f9fa; padding: 2rem; border-radius: 15px;}
    .stButton>button {background: #ff4b4b; color: white; border-radius: 12px; padding: 0.6rem 1.2rem; font-weight: bold;}
    .stTextArea>div>textarea {border-radius: 12px; border: 2px solid #e0e0e0;}
    .reply-box {background: #fff3cd; padding: 1rem; border-radius: 12px; border-left: 5px solid #ff4b4b; margin: 1rem 0;}
    .copy-btn {background: #28a745; color: white; border: none; padding: 0.5rem 1rem; border-radius: 8px; cursor: pointer;}
    .header {text-align: center; margin-bottom: 2rem;}
    .tag {background: #ff4b4b; color: white; padding: 0.3rem 0.8rem; border-radius: 20px; font-size: 0.8rem; display: inline-block;}
</style>
""", unsafe_allow_html=True)

# --- HEADER ---
st.markdown("<div class='header'>", unsafe_allow_html=True)
st.markdown("<h1>💬 ReplyGenius</h1>", unsafe_allow_html=True)
st.markdown("<p><strong>AI that writes perfect review replies in 3 seconds</strong></p>", unsafe_allow_html=True)
st.markdown("<span class='tag'>Saves 2 hours/week</span> <span class='tag'>£29/mo</span>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# --- INPUTS ---
col1, col2 = st.columns([3, 1])
with col1:
    review = st.text_area("📝 Paste the customer review:", height=120, placeholder="e.g. The pizza was cold but staff were nice...")
with col2:
    tone = st.selectbox("🎭 Tone", ["Warm & Grateful", "Professional & Empathetic", "Playful & Fun", "Confident & Assertive", ])
    business_name = st.text_input("🏪 Business Name", "The Codfather")

# --- GENERATE BUTTON ---
if st.button("🚀 Generate Perfect Reply", type="primary"):
    if not review.strip():
        st.error("Please paste a review first!")
    else:
        with st.spinner("🤖 Crafting your reply..."):
            API_URL = "https://api-inference.huggingface.co/models/microsoft/DialoGPT-medium"
            headers = {"Content-Type": "application/json"}
            
            prompt = f"""
            You are a world-class community manager for {business_name}.
            Write a polite, unique, human-sounding reply to this review using British-English.
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
                reply = "API is warming up. Try again in 30s! (Free tier)"

        # --- RESULT BOX ---
        st.markdown(f"<div class='reply-box'><strong>✨ Your Perfect Reply:</strong><br>{reply}</div>", unsafe_allow_html=True)
        
        # --- COPY BUTTON ---
        if st.button("📋 Copy to Clipboard", key="copy"):
            st.code(reply, language=None)
            st.success("Copied!")
