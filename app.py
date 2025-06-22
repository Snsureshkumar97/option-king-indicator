
import streamlit as st
import datetime
from model_utils import predict_strike
from zerodha_api import get_live_data

# Admin Login
ADMIN_USERNAME = "SNVS"
ADMIN_PASSWORD = "Rockydon1@"
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    st.subheader("🔐 Admin Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
            st.session_state.logged_in = True
            st.success("✅ Logged in as Admin")
        else:
            st.error("❌ Incorrect credentials")

# Market hours check
now = datetime.datetime.now().time()
if now < datetime.time(9, 15) or now > datetime.time(15, 30):
    st.warning("⚠️ Market is closed. Try between 9:15 AM – 3:30 PM IST.")
    st.stop()

st.title("📈 Option King Indicator – AI Powered")

# Market selection
symbols = ["NIFTY", "BANKNIFTY", "SENSEX"]
symbol = st.selectbox("Choose Symbol", symbols)

# Get prediction
if st.button("🚀 Get AI Prediction"):
    option_data = get_live_data(symbol)
    if not option_data:
        st.error("Error fetching live data.")
    else:
        prediction = predict_strike(option_data)
        if prediction:
            direction = prediction["direction"]
            strike = prediction["strike"]
            entry = prediction["entry"]
            t1, t2, t3 = prediction["t1"], prediction["t2"], prediction["t3"]
            sl = prediction["sl"]
            lot_sizes = {"NIFTY": 75, "BANKNIFTY": 30, "SENSEX": 20}
            lot = lot_sizes.get(symbol, 50)

            st.success(f"🔮 {direction} @ {strike}")
            st.markdown(f'''
            - **Entry Price**: ₹{entry}  
            - **Target 1**: ₹{t1}  
            - **Target 2**: ₹{t2}  
            - **Target 3**: ₹{t3}  
            - **Stop Loss**: ₹{sl}  
            - **Lot Size**: {lot}  
            - **Max Profit (T3)**: ₹{(t3 - entry) * lot:.2f}  
            - **Max Loss (SL)**: ₹{(entry - sl) * lot:.2f}
            ''')

            st.components.v1.iframe(
                f"https://www.tradingview.com/widgetembed/?symbol=NSE:{symbol}&interval=5&theme=light",
                height=400
            )

if st.session_state.logged_in:
    st.subheader("👑 Admin Panel")
    st.markdown("Use this space for future premium features.")
    if st.button("Logout"):
        st.session_state.logged_in = False
        st.experimental_rerun()
