import pandas
from chefboost import Chefboost 

df = pandas.read_csv("dados.csv")

config = {"algorithm": "C4.5"}
config = {'enableGBM': True, 'epochs': 7, 'learning_rate': 1}

model = Chefboost.fit(df, config = config, target_label = "Decision")

Chefboost.save_model(model, "model.pkl")

print(df)