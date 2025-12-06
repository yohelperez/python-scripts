# Datos iniciales
monto_inicial = 1000000  # COP
tasa_anual = 0.13  # 13% EA
dias = 365

# Cálculo de tasa diaria correcta (de EA a ED)
tasa_diaria = (1 + tasa_anual)**(1/365) - 1

# Interés compuesto para n días
intereses = monto_inicial * ((1 + tasa_diaria)**dias - 1)

interes_anual = monto_inicial * tasa_anual  # referencia

print(f"Intereses a los {dias} días: {intereses}")
print(f"Interés anual: {interes_anual}")
