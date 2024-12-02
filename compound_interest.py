# Datos iniciales
monto_inicial = 1000000  # COP
tasa_anual = 0.13  # 13% EA
dias = 3

# Cálculo de tasa diaria
tasa_diaria = tasa_anual / 365

# Interés compuesto para n días
intereses = monto_inicial * ((1 + tasa_diaria) ** dias - 1)
interes_anual = monto_inicial * tasa_anual
print(f"intereses a los {dias} dias: {intereses} \ninteres anual: {interes_anual}")