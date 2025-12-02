import matplotlib
matplotlib.use("Agg")

import pandas as pd
import matplotlib.pyplot as plt
import os

os.makedirs('plots', exist_ok=True)

# Load prepared series and ARIMA forecast
actual = pd.read_csv('outputs/input_series.csv', parse_dates=['date']).set_index('date')
arima_fc = pd.read_csv('outputs/forecast_arima.csv', parse_dates=['date']).set_index('date')

# Plot last 120 days of actual and show ARIMA forecast horizon
ax = actual['y'].tail(120).plot(figsize=(10,4), title="Actual (last 120 days) and ARIMA Forecast")
# align forecast on the same axis (will plot into future)
arima_fc['yhat_arima'].plot(ax=ax, style='--', label='ARIMA Forecast')

ax.set_ylabel("Sales")
plt.legend()
plt.tight_layout()

outpath = 'plots/forecast_vs_actual.png'
plt.savefig(outpath, dpi=150)
print("Saved:", outpath)
