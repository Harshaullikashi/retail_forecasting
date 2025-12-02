import pandas as pd, os
print("Files in outputs:", os.listdir('outputs'))
act = pd.read_csv('outputs/input_series.csv', parse_dates=['date']).set_index('date')
ar = pd.read_csv('outputs/forecast_arima.csv', parse_dates=['date']).set_index('date')
pr = pd.read_csv('outputs/forecast_prophet.csv', parse_dates=['ds']).set_index('ds')
print("Actual range:", act.index.min().date(), "→", act.index.max().date(), "rows:", len(act))
print("ARIMA range:", ar.index.min().date(), "→", ar.index.max().date(), "rows:", len(ar))
print("Prophet range:", pr.index.min().date(), "→", pr.index.max().date(), "rows:", len(pr))
print("\nARIMA sample stats (yhat_arima):")
print(ar['yhat_arima'].describe().round(2))
print("\nProphet sample stats (yhat):")
print(pr['yhat'].describe().round(2))
common = act.index.intersection(ar.index)
if len(common)>0:
    y_true = act.loc[common,'y']
    y_pred = ar.loc[common,'yhat_arima']
    mae = (y_true - y_pred).abs().mean()
    rmse = ((y_true - y_pred)**2).mean()**0.5
    print(f"\nOverlap MAE: {mae:.3f}, RMSE: {rmse:.3f}")
else:
    print("\nNo overlap between actuals and ARIMA forecast — run a notebook backtest for holdout metrics.")
