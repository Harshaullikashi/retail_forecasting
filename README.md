🚀 Retail Sales Forecasting (ARIMA + Prophet)

An end-to-end time series forecasting pipeline built using Python, ARIMA, and Prophet, designed to predict store-item retail demand.
Includes data preprocessing, model pipelines, forecast generation, and Power BI integration support.

📘 Project Overview

Retail organisations rely heavily on accurate demand forecasting for:

Inventory planning

Supply chain optimization

Sales & revenue projections

Reducing stockouts and overstock

This project builds an automated forecasting solution that:

Prepares input time-series data

Trains ARIMA and Prophet models

Generates clean forecast outputs

Enables easy integration with BI dashboards (Power BI)

retail_forecasting

│
├── data/
│   └── retail_sales.csv             # Input dataset
│
├── outputs/
│   ├── input_series.csv             # Cleaned time series
│   ├── forecast_arima.csv           # ARIMA forecast results
│   └── forecast_prophet.csv         # Prophet forecast results
│
├── forecast.py                      # Main forecasting pipeline
├── requirements.txt                 # Project dependencies
├── README.md                        # Documentation
└── .gitignore

⚙️ Tech Stack
Languages

Python

Libraries

pandas

numpy

statsmodels (ARIMA)

Prophet

matplotlib

Tools

GitHub

Power BI (optional visualization layer)

📊 Models Used

🔹 ARIMA

Classical statistical forecasting model used for short-term predictions.
Forecast horizon: 30 days.

🔹 Prophet

Advanced forecasting library by Meta that handles:

Trend

Seasonality

Holiday patterns

Generates full in-sample + future predictions.

📥 How to Run the Project

1. Clone the Repository
 git clone https://github.com/Harshaullikashi/retail_forecasting.git
 cd retail_forecasting

2. Create a Virtual Environment
   python -m venv venv
.\venv\Scripts\activate       # Windows
# or
source venv/bin/activate      # Mac/Linux

3. Install Requirements
   pip install -r requirements.txt
4. Run Forecast Script
   python forecast.py --input data/retail_sales.csv --store 101 --item 1 --periods 30
   
📊 Power BI Integration

The output forecast files can be directly imported into Power BI to build:

Trend dashboards

Forecast vs Actual comparisons

Store-level performance reports

Seasonal & monthly forecasting visuals







