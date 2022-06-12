
#Passo a passo de solução

import pandas as pd
from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "ACead83cd60c8b4143843fb1b48feacd83"
# Your Auth Token from twilio.com/console
auth_token  = "f5c98ec5186e27cb49d8466471d7ba00"
client = Client(account_sid, auth_token)

#Abrir os 6 arquivos em Excel
lista_meses = ["janeiro", "fevereiro", "março", "abril", "maio", "junho"]

for mes in lista_meses:
   # print(mes)
    tabela_vendas = pd.read_excel(f"{mes}.xlsx")
  #  print(tabela_vendas)
    if(tabela_vendas["Vendas"] > 55000).any():
        vendedor = tabela_vendas.loc[tabela_vendas["Vendas"] > 55000, "Vendedor"].values[0]
        vendas = tabela_vendas.loc[tabela_vendas["Vendas"] > 55000, "Vendas"].values[0]
        print(f"No mês {mes} alguém bateu a meta. Vendedor: {vendedor}, Vendas: {vendas}")
        message = client.messages.create(
            to="+55SEUTELEFONE",
            from_="+19707172767",
            body=f"No mês {mes} alguém bateu a meta. Vendedor: {vendedor}, Vendas: {vendas}")
        print(message.sid)






#Para cada arquivo:

#Verificar se algum avlaor na coluna vendas daquele arquivo é maior que 55.000

#Se for maior do que 55.000  -> Envia um sms com o Nome, o mês e as vedas do vendedor

# Caso não seja maior do que 55.000 não faz nada

#Instalar : integração com sms, integração com excel
# Twilio library
#pandas
# openpyxl
# twilio
#caso não funcione o comando pip deverá colocar a variavel de ambiente com o caminho do python C:\Users\renat\AppData\Local\Programs\Python\Python310\Scripts  ( depois fechar o prompt e inicia ele de novo e roda o comando pip install + o nome da biblioteca

