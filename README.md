## 📈 Retail Sales Forecasting

**ARIMA + Prophet + Power BI Dashboard**

**A complete end-to-end retail demand forecasting solution using Python and Power BI.**
This project demonstrates data processing, time-series modeling (ARIMA & Prophet), visualization, and dashboard design suitable for **Data Analyst / BI Engineer / ML Engineer** portfolios.

---

---

## 🧠 Project Overview

This project builds an automated forecasting system for **daily retail sales**. It covers:

- **Data cleaning & preparation**
- **Time-series forecasting** using ARIMA and Facebook Prophet
- **Python automation** for inputs → forecasts → outputs
- **Power BI dashboard** to analyze actual vs predicted performance
- **KPI cards & visuals** for business insights

---

## 📂 Project Structure

```text
retail_forecasting/
│
├── data/
│   └── retail_sales.csv         # Raw input data (store, item, date, sales)
│
├── outputs/
│   ├── input_series.csv         # Clean extracted series
│   ├── forecast_arima.csv       # ARIMA predictions
│   └── forecast_prophet.csv     # Prophet predictions
│
├── images/
│   └── forecast_chart.png       # Forecast / dashboard preview image
│
├── plots/
│   └── forecast_vs_actual.png   # Matplotlib comparison plot
│
├── forecast.py                  # Main forecasting script
├── plots_generate.py            # Script to generate comparison plots
├── summary.py                   # Helper/summary script (optional)
├── harsha_theme.json            # Custom Power BI theme
└── README.md                    # (You are here)
```

<<<<<<< HEAD
⚙️ How the Pipeline Works

1️⃣ Data Extraction
=======
---
>>>>>>> eb8c892 (Add detailed project README)

## ⚙️ How the Pipeline Works

### 1️⃣ Data Extraction & Preparation
From the master retail dataset, the script filters the following columns:

- **store**
- **item**
- **date**
- **sales**

It then prepares a clean, continuous time series suitable for ARIMA and Prophet modeling and saves it as:

- `outputs/input_series.csv`

2️⃣ ARIMA Forecasting

Auto-configures ARIMA parameters

Trains model

Generates future predictions

Outputs saved to:

outputs/forecast_arima.csv

3️⃣ Prophet Forecasting

Handles seasonality and trend

Generates 30-day forecast

Outputs saved to:

outputs/forecast_prophet.csv

4️⃣ Power BI Dashboard

Actual Sales trend

ARIMA Forecast trend

KPIs:

Total Sales

7-Day Moving Average

Combined Actual vs Forecast chart

Custom theme applied (harsha_theme.json)

Dashboard Preview

🚀 How to Run the Forecast Script

1️⃣ Activate the virtual environment
.\venv\Scripts\activate

2️⃣ Run the forecasting pipeline
python forecast.py --input data/retail_sales.csv --store 101 --item 1 --periods 30

Output files generated:

forecast_arima.csv

forecast_prophet.csv

input_series.csv

📊 Power BI Dashboard Instructions
Import forecast outputs

Open Power BI Desktop

Load:

outputs/input_series.csv

outputs/forecast_arima.csv

outputs/forecast_prophet.csv

Apply custom theme

View → Browse for themes → harsha_theme.json

Build Visuals

KPI Cards:

Avg Sales (7 Days)

Total Sales

Line charts:

Actual sales by date

Actual vs ARIMA forecast

All visuals arranged in the Overview dashboard page.

🧪 Tech Stack

Component	Tools Used
Language	Python, DAX
Modeling	ARIMA (statsmodels), Prophet
Visualization	Power BI
Data Handling	pandas, numpy
Version Control	Git & GitHub

🎯 Key Learnings / Outcomes

How to build a production-style forecasting script

Working with ARIMA + Prophet for time-series

Preparing BI-ready datasets

Designing clean Power BI dashboards

Automating analytics workflows

