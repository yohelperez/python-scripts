capital_inicial = 82000000
tasa_efectiva_anual = 0.13
tiempo_anios = 6

valor_futuro = capital_inicial * (1 + tasa_efectiva_anual) ** tiempo_anios
ganancia = valor_futuro - capital_inicial
rentabilidad = ganancia / capital_inicial * 100

print(f"\nValor futuro: ${valor_futuro:,.2f} COP")
print(f"Ganancia neta: ${ganancia:,.2f} COP")
print(f"Rentabilidad: {rentabilidad:.2f}%")
