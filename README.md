# Real-Time Transaction Risk Scoring (Streaming ML)

## Overview
This project is a **real-time streaming machine learning application** built using **Streamlit** and **scikit-learn**.  
It simulates continuous transaction data and uses an **online learning model** to generate **live transaction risk scores**.

The model is trained incrementally using `partial_fit`, allowing it to **learn and adapt in real time** without batch retraining.

---

## Live Demo
🔗 https://streaming-risk-scoring-system.streamlit.app/

---

## What This Project Does
- Simulates streaming transaction data
- Trains an ML model incrementally on each incoming event
- Predicts a transaction risk score (0–100) in real time
- Displays live data and predictions on an interactive dashboard

---

## Risk Score Meaning
The model outputs a **risk score between 0 and 100**:

- **0–30** → Low Risk  
- **30–70** → Medium Risk  
- **70–100** → High Risk  

These scores are generated from synthetic data to demonstrate real-time online learning behavior.

---

## How It Works
1. Transaction data is generated continuously (amount and velocity).
2. Each data point is processed immediately.
3. Features are scaled incrementally.
4. The model predicts a risk score.
5. The model updates itself using the same data point.
6. Results are visualized live in Streamlit.

---

## Tech Stack
- Python
- Streamlit
- scikit-learn (PassiveAggressiveRegressor)
- Pandas, NumPy

---

## Project Structure
```
streaming-risk-scoring-system/
├── app.py              # Streamlit dashboard
├── data_generator.py   # Streaming data generator
├── model.py            # Online ML model
├── requirements.txt
└── README.md
```





## Installation

Follow these steps to install and run the Streaming Risk Scoring System:

1. Clone the repository:
   ```bash
   git clone https://github.com/Beno-Jeffry-B/streaming-risk-scoring-system.git
   cd streaming-risk-scoring-system
   ```

2. Install dependencies (Python example):
   ```bash
   pip install -r requirements.txt
   ```

3. Set up environment variables as needed in a `.env` file.

4. Start the service:
   ```bash
   python app.py
   ```

5. Access the API endpoints using your preferred HTTP client or integrate with your application.

## Requirements

- Python 3.8 or above.
- pip for Python package management.
- Optional: Docker for containerized deployment.
- Supported OS: Linux, macOS, or Windows.

Some dependencies may require additional system libraries. Refer to `requirements.txt` for more details.

## Contributing

Your contributions are welcome! To contribute:

- Fork the repository and create a new branch for your feature or bugfix.
- Write clear code and add relevant tests.
- Update documentation where necessary.
- Ensure your code passes all checks and tests.
- Open a pull request with a clear description of your changes.

Please follow the coding standards and guidelines outlined in the CONTRIBUTING.md file. For major changes, open an issue to discuss your ideas first.

---

## License

This project is licensed under the MIT License. See the LICENSE file for details.

---

## Contact

For questions or support, please open an issue or contact the repository maintainer via the project's GitHub page.
