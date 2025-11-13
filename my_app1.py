# app.py  –  Drop-o-Meter™  (works instantly on Streamlit Cloud)

import streamlit as st
import random
from urllib.parse import quote_plus

# -------------------------------------------------
# PAGE CONFIG
# -------------------------------------------------
st.set_page_config(
    page_title="Drop-o-Meter™",
    page_icon="💩",
    layout="centered"
)

# -------------------------------------------------
# HEADER
# -------------------------------------------------
st.title("Drop-o-Meter™")
st.caption("Drop **5 customer reviews** + **your 5 replies** → see how much **% CRAP** you are.")

# -------------------------------------------------
# FILE UPLOADERS
# -------------------------------------------------
col1, col2 = st.columns(2)

with col1:
    reviews = st.file_uploader(
        "Customer Reviews (5 files)",
        accept_multiple_files=True,
        type=["txt", "csv", "md"],
        help="One review per file"
    )

with col2:
    replies = st.file_uploader(
        "Your Replies (5 files)",
        accept_multiple_files=True,
        type=["txt", "csv", "md"],
        help="One reply per file"
    )

# -------------------------------------------------
# ANALYZE BUTTON
# -------------------------------------------------
if st.button("SCAN FOR CRAP", type="primary", use_container_width=True):
    # ---- Validation ----
    if not reviews or not replies:
        st.error("Upload **both** sets of files!")
    elif len(reviews) != 5 or len(replies) != 5:
        st.error("Exactly **5 reviews** + **5 replies**. No more, no less.")
    else:
        with st.spinner("Sniffing for crap..."):
            # ---- FAKE AI (instant) ----
            crap_score = random.randint(12, 91)

            # Random funny feedback lines
            feedback_pool = [
                "Reply #1: Too short → +11% crap",
                "Review #3: Ignored emotion → +8% crap",
                "Used 'sorry' without action → +6% crap",
                "Reply #5: Copy-paste vibes → +10% crap",
                "One reply was actually good → -5% crap",
                "Used 'K' → instant +15% crap",
                "No empathy detected → +9% crap",
                "Perfect reply! → -7% crap"
            ]
            random.shuffle(feedback_pool)
            selected = feedback_pool[:3]

            # ---- METER DISPLAY ----
            bars = "▰" * (crap_score // 10) + "▱" * (10 - crap_score // 10)
            color = "red" if crap_score > 60 else "orange" if crap_score > 30 else "green"
            st.markdown(
                f"### <span style='color:{color};font-size:2.5em'>{bars}</span> **{crap_score}% CRAP**",
                unsafe_allow_html=True
            )

            # ---- FEEDBACK ----
            for line in selected:
                st.markdown(f"- {line}")

            # ---- SHARE BUTTON ----
            tweet_text = f"My support replies are {crap_score}% crap 💩 Try Drop-o-Meter™:"
            tweet_url = f"https://twitter.com/intent/tweet?text={quote_plus(tweet_text)}"
            st.markdown(f"[Tweet Your Crap Score]({tweet_url})", unsafe_allow_html=True)

# -------------------------------------------------
# FOOTER
# -------------------------------------------------
st.markdown("---")
st.caption("Made with ❤️ + Streamlit • No API • Instant results")

