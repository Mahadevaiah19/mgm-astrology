import streamlit as st
from datetime import datetime
import pytz
from kerykeion import AstrologicalSubject, Report

st.set_page_config(page_title="Maha Guru Ji Method", layout="wide")

st.title("Maha Guru Ji Method - MGM Astrology 🌟")
st.subheader("Unique Score-Based Guidance | Marriage Porutham | Reverse Partner Timing")
st.markdown("""
Welcome! This is the Maha Guru Ji Method — a one-of-a-kind astrology tool.  
Start by entering birth details to see planetary positions and a basic daily score.  
More features (good muhurta, Porutham matching, reverse partner finder) coming soon!
""")

# User input section
with st.form("birth_details"):
    col1, col2 = st.columns(2)
    with col1:
        name = st.text_input("Name", value="Mahadevaiah")
        dob = st.date_input("Date of Birth", value=datetime(1990, 1, 1))
    with col2:
        time_input = st.time_input("Birth Time (approx)", value=datetime.strptime("12:00", "%H:%M").time())
        place = st.text_input("Birth Place / City", value="Phoenix, Arizona")

    submitted = st.form_submit_button("Generate Chart & Score")

if submitted:
    try:
        # Combine date + time
        birth_naive = datetime.combine(dob, time_input)
        
        # Use Phoenix timezone by default (MST/Arizona no DST)
        tz = pytz.timezone("America/Phoenix")
        birth_dt = tz.localize(birth_naive)

        # Coordinates (Phoenix default; we can add geopy later if needed)
        lat = 33.4484
        lng = -112.0740

        st.info(f"Calculating for {name} born {birth_dt.strftime('%Y-%m-%d %H:%M %Z')} at {place} ({lat}, {lng})")

        # Create Kerykeion subject (natal chart)
        subject = AstrologicalSubject(
            name,
            birth_dt.year, birth_dt.month, birth_dt.day,
            birth_dt.hour, birth_dt.minute,
            lat=lat,
            lng=lng,
            tz_str="America/Phoenix",
            online=False  # Use built-in ephemeris (no internet needed)
        )

        # Get text report
        report = Report(subject)
        report_text = report.get_report()

        st.subheader("Planetary Positions & Basic Report")
        st.text_area("Report", report_text, height=300)

        # Placeholder for your MGM score (expand this later)
        score = 68.0  # dummy value
        insight = """
        Basic MGM Score: Moderate (expand with Subathuvam, Akshaya Lagna Pathadi, Tithi Sunyam rules).
        Real-world example: Avoided major decisions during challenging transits → better outcomes.
        """

        st.metric("MGM Daily Astrology Score", f"{score:.0f}/100", delta=None)
        st.write(insight)

    except Exception as e:
        st.error(f"Something went wrong: {str(e)}\n\nTry adjusting time or check inputs.")
