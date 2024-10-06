# Тут має бути твій код
import pandas as pd
import matplotlib.pyplot as plt

df = pandas.read_csv("titanic_csv")
print(df.info())
print(df.isnull())
print(df.head(10))
