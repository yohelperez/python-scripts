aporte_mensual = 2000000       # tu aporte mensual
capital_inicial = 0
tasa_efectiva_anual = 0.15     # 10% EA, historial del S&P500 / VOO
tiempo_anios = 5

# Total invertido (suma de aportes)
total_invertido = aporte_mensual * 12 * tiempo_anios + capital_inicial

# Tasa efectiva mensual (TEM)
tasa_mensual = (1 + tasa_efectiva_anual)**(1/12) - 1

# Valor futuro del capital inicial
valor_futuro = capital_inicial * (1 + tasa_mensual)**(12 * tiempo_anios)

# Valor futuro de los aportes mensuales
valor_futuro += aporte_mensual * (((1 + tasa_mensual)**(12 * tiempo_anios) - 1) / tasa_mensual)

# Resultados
ganancia_neta = valor_futuro - total_invertido
rentabilidad = (ganancia_neta / total_invertido) * 100

print(f"\nValor futuro: ${valor_futuro:,.2f} COP")
print(f"Total invertido: ${total_invertido:,.2f} COP")
print(f"Ganancia neta: ${ganancia_neta:,.2f} COP")
print(f"Rentabilidad: {rentabilidad:.2f}%")
