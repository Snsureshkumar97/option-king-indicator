
import joblib
import numpy as np

model = joblib.load("ai_model.pkl")

def extract_features(option_data):
    return np.array([
        option_data["oi_change"],
        option_data["volume"],
        option_data["iv"],
        option_data["rsi"],
        option_data["atr"],
        option_data["days_to_expiry"]
    ]).reshape(1, -1)

def predict_strike(option_data):
    features = extract_features(option_data)
    pred = model.predict(features)[0]
    direction = "CALL" if pred == 1 else "PUT"
    strike = option_data["atm_strike"]
    entry = option_data["ltp"]
    t1 = round(entry + 10, 2)
    t2 = round(entry + 20, 2)
    t3 = round(entry + 30, 2)
    sl = round(entry - 15, 2)
    return {
        "direction": direction,
        "strike": strike,
        "entry": entry,
        "t1": t1,
        "t2": t2,
        "t3": t3,
        "sl": sl
    }
