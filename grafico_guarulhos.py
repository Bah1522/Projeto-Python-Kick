import pandas as pd
import matplotlib.pyplot as plt

planilha = pd.read_excel("casos_obitos_guarulhos.xlsx")

plt.title("Percentual de Casos vs Óbitos de Guarulhos, 30. Jan. 2022")

plt.pie(planilha["Casos/Óbitos"], labels = planilha["Total_casos = 66560"], autopct="%1.2f%%")

plt.show()