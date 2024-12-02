# Datos iniciales después del reinicio
intereses_mensuales = 18498.24  # COP
tasa_anual = 0.13  # 13% EA

# Cálculo de la tasa mensual (TEM)
tasa_mensual = (1 + tasa_anual) ** (1 / 12) - 1

# Cálculo del monto promedio
monto_estimado = intereses_mensuales / tasa_mensual
print(monto_estimado)
