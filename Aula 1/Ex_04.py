# Um dono de um clube precisa cercar o campo de futebol society com uma tela de aço.
# O campo mede 30m de largura por 50m de comprimento. Sabendo que cada metro de tela custa R$ 26,00,
# desenvolva um programa que calcule quanto de tela de aço será necessária para
# cercar o campo e quanto custará.

##Organizando os dados
### 30m == largura ___ 50m == comprimento >>> 30²+50²

largura = 30**2
comprimento = 50**2
tela_largura = largura*26
tela_comprimento = comprimento*26
quantidade_telas = tela_largura+tela_comprimento//26
preço_total = tela_largura+tela_comprimento
print(f"\033[036mSerá necessário usar {quantidade_telas} telas de aço,para cercar o campo;")
print(f"\033[035mE o preço total será de: \033[031mR$ {preço_total:.2f}")