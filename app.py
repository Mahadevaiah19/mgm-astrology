import streamlit as st
from datetime import datetime
import pytz
import re  # for simple parsing

st.set_page_config(
    page_title="Maha Guru Ji Method - MGM Astrology",
    page_icon="🪐",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS (mystical/dark theme)
st.markdown("""
    <style>
    .stApp { background-color: #0e1117; color: #e0e0ff; }
    .stButton>button { background-color: #6a1b9a; color: white; border-radius: 8px; }
    .stTextInput>div>div>input, .stTextArea>div>div>textarea { background-color: #1e1e2e; color: #e0e0ff; }
    h1, h2, h3 { color: #bb86fc; }
    .stExpander { background-color: #1e1e2e; border: 1px solid #6a1b9a; }
    </style>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.title("Maha Guru Ji Method 🪐")
    st.markdown("**MGM Astrology** – Your Custom Guidance System")
    st.markdown("Phoenix, AZ | Wisdom + Real-World Logic")

    page = st.radio(
        "Select Section",
        ["Daily MGM Score & Manual Chart Input",
         "Marriage Porutham Matching",
         "Reverse Partner Birth Finder",
         "MGM Rules & Examples"]
    )

# Main content
if page == "Daily MGM Score & Manual Chart Input":
    st.title("Daily MGM Score & Guidance 🌟")
    st.markdown("Paste your planetary positions below (from any chart tool like AstroSage or JHora). MGM will use them for scoring & insights.")

    with st.form("input_form"):
        col1, col2 = st.columns([3, 2])

        with col1:
            name = st.text_input("Your Name", "Mahadevaiah")

        with col2:
            current_date = st.date_input("Date for Analysis (today or future)", datetime.now().date())

        st.markdown("**Paste Planetary Positions Here** (one per line, flexible format)")
        positions_text = st.text_area(
            "Example format:\nSun: Aries 15°\nMoon: Taurus 22°30'\nMars: Gemini 8°\n... (R for retrograde if needed)",
            height=200,
            help="Copy from your Vedic chart. Include Ascendant/Lagna, Rahu/Ketu too. We'll parse it automatically."
        )

        submit = st.form_submit_button("Analyze with MGM ✨", type="primary", use_container_width=True)

    if submit and positions_text.strip():
        with st.spinner("Processing your chart..."):
            # Simple parser (improve later as needed)
            planet_data = {}
            lines = positions_text.strip().split("\n")
            for line in lines:
                line = line.strip()
                if not line:
                    continue
                # Flexible match: Planet: Sign Degrees (R)?
                match = re.match(r"^(.*?):\s*(\w+)\s*([\d°']+)?\s*(R)?$", line, re.IGNORECASE)
                if match:
                    planet = match.group(1).strip().title()
                    sign = match.group(2).strip().title()
                    deg = match.group(3).strip() if match.group(3) else ""
                    retro = " (R)" if match.group(4) else ""
                    planet_data[planet] = f"{sign} {deg}{retro}"

            if not planet_data:
                st.warning("Couldn't parse positions. Try format like 'Sun: Aries 15°' per line.")
            else:
                st.success(f"Chart loaded for **{name}** – Analysis for {current_date}")

                # Display parsed chart
                with st.expander("Your Parsed Positions", expanded=True):
                    for p, pos in planet_data.items():
                        st.markdown(f"**{p}**: {pos}")

                # Placeholder MGM score based on manual input (expand daily)
                score = 75  # dummy
                if "Jupiter" in planet_data and "Pisces" in planet_data["Jupiter"]:
                    score += 15  # example rule stub

                level = "Strong" if score >= 80 else "Moderate" if score >= 60 else "Challenging"

                col_score, col_level = st.columns(2)
                col_score.metric("MGM Score", f"{score}/100", delta="Benefic Support")
                col_level.metric("Overall", level)

                with st.expander("Guidance & Example", expanded=True):
                    st.markdown("""
                    **Interpretation Stub**  
                    Positions indicate moderate flow. Jupiter influence suggests protection in decisions.  

                    **Real-World Example**  
                    Client with similar Jupiter placement waited one day for better transit → successful outcome in legal matter (2025 case).
                    """)

                st.info("Next steps: Add your custom rules here (Subathuvam check, Tithi Sunyam, Akshaya Lagna logic). We can improve parsing too!")

    else:
        st.info("Paste your positions and click Analyze to start.")

# Other pages placeholders
elif page == "Marriage Porutham Matching":
    st.title("Marriage Porutham Matching 💍")
    st.write("Coming soon: Input boy/girl positions → compute Porutham score")

elif page == "Reverse Partner Birth Finder":
    st.title("Reverse Partner Finder 🔮")
    st.write("Coming soon: Suggest ideal birth windows based on your chart")

elif page == "MGM Method Rules & Examples":
    st.title("MGM Rules & Real Examples 📜")
    st.write("Add your logic explanations and stories here – update anytime.")

st.markdown("---")
st.caption("Maha Guru Ji Method | © 2026 | Building Unique Astrology Tools")
