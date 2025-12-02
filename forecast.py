import os
import argparse
import pandas as pd
from pathlib import Path

def ensure_dir(p):
    Path(p).mkdir(parents=True, exist_ok=True)

def prepare_data(df, store_id, item_id):
    df = df[(df["store_id"] == store_id) & (df["item_id"] == item_id)].copy()
    df["date"] = pd.to_datetime(df["date"])
    df = df.set_index("date").resample("D").sum()[["sales"]]
    df = df.rename(columns={"sales": "y"})
    return df

def arima_forecast(df, periods, output_dir):
    try:
        from statsmodels.tsa.statespace.sarimax import SARIMAX
    except:
        print("statsmodels not installed.")
        return None

    model = SARIMAX(df["y"], order=(1,1,1), seasonal_order=(1,1,1,7),
                    enforce_stationarity=False, enforce_invertibility=False)
    res = model.fit(disp=False)
    fc = res.get_forecast(steps=periods)

    idx = pd.date_range(df.index.max() + pd.Timedelta(days=1), periods=periods)
    forecast = pd.DataFrame({
        "date": idx,
        "yhat_arima": fc.predicted_mean.values
    })

    ensure_dir(output_dir)
    forecast.to_csv(os.path.join(output_dir, "forecast_arima.csv"), index=False)
    print("Saved ARIMA forecast -> outputs/forecast_arima.csv")
    return forecast

def prophet_forecast(df, periods, output_dir):
    try:
        from prophet import Prophet
    except:
        print("Prophet not installed.")
        return None

    df_prophet = df.reset_index().rename(columns={"date": "ds", "y": "y"})
    m = Prophet(daily_seasonality=True)
    m.fit(df_prophet)

    future = m.make_future_dataframe(periods=periods)
    forecast = m.predict(future)

    ensure_dir(output_dir)
    forecast[["ds", "yhat"]].to_csv(os.path.join(output_dir, "forecast_prophet.csv"), index=False)
    print("Saved Prophet forecast -> outputs/forecast_prophet.csv")

    return forecast

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", default="data/retail_sales.csv")
    parser.add_argument("--store", type=int, default=101)
    parser.add_argument("--item", type=int, default=1)
    parser.add_argument("--periods", type=int, default=30)
    args = parser.parse_args()

    df = pd.read_csv(args.input)
    df_ts = prepare_data(df, args.store, args.item)

    ensure_dir("outputs")
    df_ts.to_csv("outputs/input_series.csv")

    arima_forecast(df_ts, args.periods, "outputs")
    prophet_forecast(df_ts, args.periods, "outputs")

if __name__ == "__main__":
    main()
