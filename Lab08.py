# Intermediate Python – Lab 8 – Lew Piper III
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Part I
with open("all_alpha_19.csv") as file:
    df = pd.read_csv(file, header='infer')

fuels = ["Gasoline", "Diesel"]
fuel = df.query("Stnd=='T3B125'").query("Fuel in @fuels")

cols = ['Model', 'Displ', 'Fuel', 'City MPG', 'Hwy MPG', 'Cmb MPG',
        'Greenhouse Gas Score']
new_df = fuel[cols].reset_index(drop=True)

new_df = new_df.astype({"City MPG": float, "Hwy MPG": float, "Cmb MPG": float})


def mpg_to_kml(mpg):
    return mpg * 0.42514


new_df = new_df.assign(CityKML=lambda x: mpg_to_kml(x["City MPG"]),
                       HwyKML=lambda x: mpg_to_kml(x["Hwy MPG"]),
                       CmbKML=lambda x: mpg_to_kml(x["Cmb MPG"]))

new_df.to_csv("car_data.csv")

# Part II
with open("car_data.csv") as file:
    df = pd.read_csv(file, header='infer', index_col=0)

df.plot(kind='scatter', x="Displ", y="City MPG", color='r')
plt.show()

c = ["r" if row['Fuel'] == "Gasoline" else "g" for i, row in df.iterrows()]
s = [int(row['Greenhouse Gas Score'])*10 for i, row in df.iterrows()]

df.plot(kind='scatter', x="Displ", y="City MPG", color=c, s=s, alpha=.5)
plt.show()
