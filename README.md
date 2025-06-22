
# 🧠 Option King Indicator – AI Powered for NSE/BSE

A smart web app that uses real-time Zerodha data + AI model (XGBoost-style) to predict optimal CALL/PUT options, strike price, targets, and stop loss for NIFTY, BANKNIFTY, SENSEX.

---

## 🚀 Features

- ✅ Real-time option chain data (via Zerodha API)
- ✅ AI-powered CALL/PUT and strike prediction
- ✅ Targets (T1, T2, T3) and Stop Loss calculation
- ✅ Profit/Loss per lot display
- ✅ Trading hours filter (9:15 AM – 3:30 PM IST)
- ✅ TradingView chart embedded
- ✅ Admin login panel (`SNVS` / `Rockydon1@`)
- ✅ Ready for Streamlit Cloud deployment

---

## 📦 Installation (Local)

```bash
git clone https://github.com/yourusername/option-king-indicator.git
cd option-king-indicator
pip install -r requirements.txt
streamlit run app.py
```

---

## 🔐 Streamlit Secrets (Required for Live Data)

In Streamlit Cloud or locally in `.streamlit/secrets.toml`, add:

```toml
Z_API_KEY = "your_zerodha_api_key"
Z_API_SECRET = "your_zerodha_api_secret"
ACCESS_TOKEN = "your_daily_generated_token"
```

You must update `ACCESS_TOKEN` daily after logging in to Zerodha Kite.

---

## 📂 Folder Structure

```
option-king-indicator/
├── app.py
├── model_utils.py
├── zerodha_api.py
├── ai_model.pkl
├── requirements.txt
├── README.md
└── .streamlit/
    └── config.toml
```

---

## 📤 Deployment (Streamlit Cloud)

1. Push this folder to GitHub
2. Go to [https://streamlit.io/cloud](https://streamlit.io/cloud)
3. Click "New App"
4. Connect your GitHub, select `app.py`, deploy
5. Paste your API keys and access token into Settings → Secrets

---

## 👑 Admin Login

To unlock admin-only features:

- **Username:** SNVS  
- **Password:** Rockydon1@

---

## 📬 Feedback & Enhancements

You can expand this project by adding:
- Auto-refreshing predictions
- Telegram/email alerts
- Historical accuracy tracking
- Premium subscription panel

---

**Built with ❤️ to help traders make smart, fast, and profitable decisions.**
