import pandas as pd
import numpy as np

dates = pd.date_range("2019-01-01", "2021-12-31")
np.random.seed(42)
sales = 1000 + 40*np.sin(np.arange(len(dates))/20) + np.random.normal(0,70,len(dates))

df = pd.DataFrame({
    "date": dates,
    "store_id": np.random.choice([101,102,103], len(dates)),
    "item_id": np.random.choice([1,2,3,4], len(dates)),
    "sales": sales
})

df.to_csv("data/retail_sales.csv", index=False)
print("Created data/retail_sales.csv")
