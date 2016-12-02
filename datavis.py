import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import ggplot

weather_df = pd.DataFrame()

weather_df = weather_df.from_csv("data_raw.csv")

weather_by_state = pd.DataFrame()

weather_by_state["State"] = weather_df["State"].unique()

print(weather_df[(weather_df.Month==4) & (weather_df.Day==29)])
