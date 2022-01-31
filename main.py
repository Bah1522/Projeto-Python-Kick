import os
import pandas as pd
from fpdf import FPDF
import matplotlib.pyplot as plt

pdf = FPDF("P", "mm", "A4")
pdf.add_page()
pdf.set_font("Times", "", 16)

dadosMunicipio = pd.read_excel(r'Dados-covid-19-municipios.xlsx')
totalObitos = dadosMunicipio["Mun_Total de óbitos"]
totalDeCasos = dadosMunicipio["Mun_Total de casos"]

pdf.add_page()
pdf.set_font('Times', '', 15)
pdf.image(name='covid-19.png', x=83, y=220, w=50)
pdf.set_margins(10, 40, 0)
texto = 'No final de dezembro de 2019 o mundo se deparou com um novo desafio, uma nova realidade que viria ser nos anos seguintes. A sociedade se deparou com um virús mortal chamado coronavírus, foi denominada oficialmente como COVID-19, sigla em inglês para coronavirus disease 2019 . É um vírus que causa doença respiratória pelo agente coronavírus, com casos recentes registrados em várias partes do mundo.. Em casos extremos, pode levar a óbito. ' "A Covid-19 é uma infecção respiratória aguda causada pelo coronavírus SARS-CoV-2, potencialmente grave, de elevada transmissibilidade e de distribuição global." "O SARS-CoV-2 é um betacoronavírus descoberto em amostras de lavado broncoalveolar obtidas de pacientes com pneumonia de causa desconhecida na cidade de Wuhan, província de Hubei, China, em dezembro de 2019. Pertence ao subgênero Sarbecovírus da família Coronaviridae e é o sétimo coronavírus conhecido a infectar seres humanos." "Os coronavírus são uma grande família de vírus comuns em muitas espécies diferentes de animais, incluindo o homem, camelos, gado, gatos e morcegos. Raramente os coronavírus de animais podem infectar pessoas e depois se espalhar entre seres humanos como já ocorreu com o MERS-CoV e o SARS-CoV-2. Até o momento, não foi definido o reservatório silvestre do SARS-CoV-2." "A transmissão se dá pelo contato com gotículas de uma pessoa infectada, seja por meio da tosse, do espirro ou mesmo da fala. Uma pessoa saudável pode respirar as gotículas infectadas e assim se infectar ou, depois de tocar superfícies infectadas, levar suas mãos aos seus olhos, nariz e boca, se contaminando. (Veja aqui o tempo de sobrevida do coronavírus em algumas superfícies.)""É importante saber que uma pessoa infectada pode levar até 14 dias para apresentar sintomas. Mesmo sem os sintomas, essa pessoa pode transmitir a doença."
pdf.multi_cell(w=0, h=8, txt=texto, align="C")

plt.plot(totalObitos)
plt.xlabel('Grafico Óbitos por dia no estado de sp')
plt.savefig("exemplo1.png")
plt.close()
pdf.image(x=20, y=110, w=180, h=80, name='exemplo1.png')

plt.plot(totalDeCasos)
plt.xlabel('Grafico total de casos no estado de sp')
plt.savefig("exemplo2.png")
plt.close()
pdf.image(x=20, y=210, w=180, h=80, name='exemplo2.png')


pdf.output("covid.pdf")

os.system("pause")