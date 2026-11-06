
import pandas as pd

datos = pd.read_csv("datos/ventas/demanda.csv")
print(len(datos))

fichas = datos.groupby(["store", "item"])["sales"].agg(["mean", "std"])
print(fichas.head())
