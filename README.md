📈 Retail Sales Forecasting (ARIMA + Prophet)

End-to-end time-series forecasting pipeline built using Python, ARIMA, and Prophet, designed to predict retail item-level demand.
The project includes data processing, forecasting models, evaluation setup, and Power BI integration guidance.

🔍 Project Overview

Retail businesses rely heavily on accurate sales forecasts to plan inventory, pricing, and supply chain operations.
This project builds a complete forecasting workflow:

✔ Generates a clean time-series dataset
✔ Builds forecasting models (ARIMA, Prophet)
✔ Produces future predictions for store–item combinations
✔ Outputs forecast CSV files for further analytics / Power BI dashboards

🧱 Project Structure
retail_forecasting/
│
├── data/
│   └── retail_sales.csv               # Input time-series dataset
│
├── outputs/
│   ├── input_series.csv               # Clean formatted series used for modeling
│   ├── forecast_arima.csv             # ARIMA forecast output
│   └── forecast_prophet.csv           # Prophet forecast output
│
├── forecasts.py                       # Main forecasting script (ARIMA + Prophet)
├── requirements.txt                   # Python dependencies
├── README.md                          # Project documentation
└── .gitignore

⚙️ Tech Stack
Languages

Python

Libraries

pandas

statsmodels (ARIMA)

Prophet

matplotlib

numpy

Tools

Git / GitHub

Power BI (for dashboarding consumption)

📊 Models Used
1️⃣ ARIMA (AutoRegressive Integrated Moving Average)

Used for classical statistical forecasting.
Generates 30-day ahead predictions.

2️⃣ Prophet (Facebook/Meta Prophet)

Handles trend, seasonality, and holiday effects.
Useful for business time-series with strong weekly/annual patterns.

🚀 How to Run the Project
1. Clone the repo
git clone https://github.com/Harshaullikashi/retail_forecasting.git
cd retail_forecasting

2. Create virtual environment
python -m venv venv
source venv/bin/activate        # Mac/Linux
.\venv\Scripts\activate         # Windows

3. Install dependencies
pip install -r requirements.txt

4. Run forecast
python forecast.py --input data/retail_sales.csv --store 101 --item 1 --periods 30


Outputs will be written to:

outputs/forecast_arima.csv
outputs/forecast_prophet.csv

📂 Example Output (Preview)
Forecast Stats
ARIMA forecast:
 - Horizon: 30 days
 - Mean prediction: ~136.8
 - Range: 82 → 164

Prophet forecast:
 - Coverage: 1116 rows (fitted + forecast)
 - Mean prediction: ~104.4

📈 Visualization (Optional)

Generate a visualization comparing actual vs forecast:

python plot_forecast.py       # (if added)


Expected output:

📊 Power BI Integration

The output CSV files (forecast_arima.csv, forecast_prophet.csv) can be imported into Power BI to build:

Forecast dashboards

Store-level performance monitoring

Trend & seasonality visuals

Forecast vs Actual KPI reports 




