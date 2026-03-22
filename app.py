import streamlit as st
from datetime import datetime
import pytz

st.set_page_config(page_title="Maha Guru Ji Method", layout="wide")

st.title("Maha Guru Ji Method - MGM Astrology 🌟")
st.subheader("Unique Score-Based Guidance | Marriage Porutham | Reverse Partner Timing")
st.markdown("""
Welcome to the Maha Guru Ji Method!  
Enter birth details for basic overview + MGM score (custom logic coming soon).  
Full planetary chart with kerykeion will return after fixing deployment.
""")

with st.form("birth_details"):
    col1, col2 = st.columns(2)
    with col1:
        name = st.text_input("Name", value="Mahadevaiah")
        dob = st.date_input("Date of Birth", value=datetime(1990, 1, 1))
    with col2:
        time_input = st.time_input("Birth Time (approx)", value=datetime.strptime("12:00", "%H:%M").time())
        place = st.text_input("Birth Place / City", value="Phoenix, Arizona")

    submitted = st.form_submit_button("Generate Overview & Score")

if submitted:
    birth_naive = datetime.combine(dob, time_input)
    tz = pytz.timezone("America/Phoenix")
    birth_dt = tz.localize(birth_naive)

    lat, lng = 33.4484, -112.0740

    st.success(f"Details saved for {name} — born {birth_dt.strftime('%Y-%m-%d %H:%M %Z')} at {place}")

    # Placeholder MGM score & insight
    score = 72.0
    insight = """
    MGM Score: Good potential today.  
    (Stub: Add Subathuvam check, Akshaya Lagna Pathadi progression, Tithi Sunyam avoidance here.)
    Real example: User waited for better alignment before major decision → positive outcome.
    """

    st.metric("MGM Daily Astrology Score", f"{score:.0f}/100")
    st.write(insight)

    st.info("Next: Porutham matching + reverse partner date finder features.")
