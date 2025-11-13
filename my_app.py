# app.py – Drop-o-Meter™ (PASTE-ONLY, 1 EXAMPLE OK)

import streamlit as st
import random
from urllib.parse import quote_plus

st.set_page_config(page_title="Drop-o-Meter™", page_icon="💩", layout="centered")

st.title("Drop-o-Meter™")
st.caption("Paste **1–5** customer reviews + your replies → see how **% CRAP** you are.")

# --- INPUT BOXES ---
reviews = []
replies = []

for i in range(5):
    col1, col2 = st.columns(2)
    with col1:
        rev = st.text_area(f"Customer Review #{i+1}", height=80, key=f"rev{i}")
        if rev.strip():
            reviews.append(rev.strip())
    with col2:
        rep = st.text_area(f"Your Reply #{i+1}", height=80, key=f"rep{i}")
        if rep.strip():
            replies.append(rep.strip())

# --- ANALYZE ---
if st.button("SCAN FOR CRAP", type="primary", use_container_width=True):
    if not reviews or not replies:
        st.error("Paste at least **1 review + 1 reply**!")
    elif len(reviews) != len(replies):
        st.error("Same number of reviews and replies!")
    else:
        with st.spinner("Detecting crap..."):
            # Fake AI score
            crap_score = random.randint(15, 89)

            # Funny feedback
            feedback = [
                "Used 'sorry' with no fix → +10% crap",
                "Reply too short → +7% crap",
                "Ignored the emotion → +12% crap",
                "Copy-paste reply → +9% crap",
                "Actually helpful! → -8% crap",
                "Used 'K' → +18% crap"
            ]
            random.shuffle(feedback)
            shown = feedback[:min(3, len(reviews))]

            # METER
            bars = "▰" * (crap_score // 10) + "▱" * (10 - crap_score // 10)
            color = "red" if crap_score > 60 else "orange" if crap_score > 30 else "green"
            st.markdown(f"### <span style='color:{color};font-size:2.5em'>{bars}</span> **{crap_score}% CRAP**", unsafe_allow_html=True)

            for line in shown:
                st.markdown(f"- {line}")

            # SHARE
            st.markdown(f"[Tweet: My replies are {crap_score}% crap 💩](https://twitter.com/intent/tweet?text={quote_plus(f'My replies are {crap_score}% crap 💩 Try Drop-o-Meter™:')})", unsafe_allow_html=True)

st.markdown("---")
st.caption("No files • No login • Instant roast • Made with ❤️ + Streamlit")

# app.py  –  Drop-o-Meter™  (works instantly on Streamlit Cloud)
