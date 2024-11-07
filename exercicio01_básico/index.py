from datetime import datetime, timedelta


# declarando as variáveis
data_atual = datetime.today()
data_futura = data_atual + timedelta(days = 2)

#formatando as datas
padrao_data = '{}/{}/{}'.format(data_atual.day, data_atual.month, data_atual.year)
padrao_data_futura = '{}/{}/{}'.format(data_futura.day, data_futura.month, data_futura.year)



print(padrao_data)
print(padrao_data_futura)

