Series = []
OptionUser = int(input("Quantas séries deseja cadastrar? "))
for i in range(OptionUser):
    nomeSerie = input(f"\033[032mSerie #{i+1}: ")
    Series.append(nomeSerie)
from PySimpleGUI import popup_animated
for j in range(OptionUser):
    print(f"\033[034mSerie #{j + 1}: {Series[j]}")




