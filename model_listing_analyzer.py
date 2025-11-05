import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
import joblib, os

MODEL_PATH = "data/models/listing_movement.pkl"

def train_model(history_csv="data/listings_history.csv"):
    df = pd.read_csv(history_csv)
    X = df[["initial_pump_%", "max_drawdown_%"]]
    y = df["final_change_%"]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    model = RandomForestRegressor(n_estimators=100)
    model.fit(X_train, y_train)
    joblib.dump(model, MODEL_PATH)
    print(f"✅ Модель збережена: {MODEL_PATH}")

def predict_future_move(pump, drop):
    if not os.path.exists(MODEL_PATH): return None
    model = joblib.load(MODEL_PATH)
    return model.predict([[pump, drop]])[0]
