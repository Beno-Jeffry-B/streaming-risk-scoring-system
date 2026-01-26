# model.py
import numpy as np
from sklearn.linear_model import SGDClassifier
from sklearn.preprocessing import StandardScaler

class OnlineRiskModel:
    """
    Incremental risk model that adapts continuously
    as new transaction events arrive.
    """
    def __init__(self):
        self.scaler = StandardScaler()
        self.model = SGDClassifier(loss="log_loss")
        self.initialized = False

    def score_and_update(self, amount, velocity):
        X = np.array([[amount, velocity]])

        # synthetic supervision signal (proxy label)
        y = np.array([1 if amount > 3000 and velocity > 7 else 0])

        if not self.initialized:
            self.scaler.partial_fit(X)
            X_scaled = self.scaler.transform(X)
            self.model.partial_fit(X_scaled, y, classes=[0, 1])
            self.initialized = True
            return 0.0

        X_scaled = self.scaler.transform(X)
        prob = self.model.predict_proba(X_scaled)[0][1]
        self.model.partial_fit(X_scaled, y)

        return round(float(prob), 3)
