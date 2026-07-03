# ML model training & loading logic
import lightgbm as lgb
import pandas as pd

def train_model(X_train, y_train):
    model = lgb.LGBMClassifier(n_estimators=200, learning_rate=0.05)
    model.fit(X_train, y_train)
    model.save_model("model.txt")
    return model

def load_model():
    return lgb.Booster(model_file="model.txt")
