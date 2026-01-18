import numpy as np
from sklearn.linear_model import PassiveAggressiveRegressor
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
model = PassiveAggressiveRegressor(max_iter=1, tol=None)

trained = False


def train_and_predict(amount, velocity):
    global trained

    X = np.array([[amount, velocity]])

    raw_score = 0.6 * amount + 0.4 * velocity
    y = np.array([min(raw_score / 50, 100)])

    if not trained:
        scaler.partial_fit(X)
        X_scaled = scaler.transform(X)
        model.partial_fit(X_scaled, y)
        trained = True
        prediction = y[0]
    else:
        X_scaled = scaler.transform(X)
        prediction = model.predict(X_scaled)[0]
        model.partial_fit(X_scaled, y)

    # Clamp output
    prediction = max(0, min(prediction, 100))
    return round(float(prediction), 2)
