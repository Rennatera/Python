# importar a base de dados
# visualizar a base de dados
# Faturamento por loja
# quantidade de produtos vendidos por loja
# ticket médio por produto em casa loja
# envia email com o relatório

import pandas as pd
import win32com.client as win32

tabela_vendas = pd.read_excel("Vendas.xlsx")
# visualizar a base de dados
pd.set_option("display.max_columns", None)
#print(tabela_vendas)

# Faturamento por loja
faturamento = tabela_vendas [["ID Loja", "Valor Final"]]. groupby ("ID Loja").sum()
print(faturamento)
print("-"*50)
# quantidade de produtos vendidos por loja
quantidade = tabela_vendas [["ID Loja", "Quantidade"]].groupby("ID Loja").sum()
print(quantidade)
print("-"*50)
# ticket médio por produto em casa loja
ticket_medio = (faturamento["Valor Final"] / quantidade["Quantidade"]).to_frame()
ticket_medio = ticket_medio.rename(columns={0: "Ticket Médio"})
print(ticket_medio)

# envia email com o relatório

outlook = win32.Dispatch("outlook,application")
mail = outlook.CreateItem(0)
mail.To = "seuemail@gmail.com"
mail.Subject = "Testes de Python"
mail.HTMLBody = f'''
<p>Prezados,</p>

<p>Segue o relatório de vendas por cada Loja.</p>

<p>Faturamento:</p>
{faturamento.to_html(formatters={"Valor Final": "R${:,.2f}" .format})}

<p>Quantidade Vendida:</p>
{quantidade.to_html()}

<p>Ticket Médio dos produtos em cada Loja:</p>
{ticket_medio.to_html(formatters={"Ticket Medio": "R${:,.2f}" .format})}

<p>Qualquer dúvida estou à disposição.</p>

<p>Att.,</p>

<p>Renato Cossi</p>
'''
mail.Send()

