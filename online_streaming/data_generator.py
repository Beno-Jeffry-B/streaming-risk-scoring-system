import random
from datetime import datetime


def generate_data():
    return {
        "timestamp": datetime.now(),
        "amount": round(random.uniform(100, 5000), 2),
        "velocity": round(random.uniform(1, 10), 2),
    }
