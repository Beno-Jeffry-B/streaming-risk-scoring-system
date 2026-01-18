import random
from datetime import datetime

def generate_data():
    return {
        "timestamp": datetime.now(),
        "transaction_amount": round(random.uniform(100, 5000), 2),
        "transaction_velocity": round(random.uniform(1, 10), 2),
    }
