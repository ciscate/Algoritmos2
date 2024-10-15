"""
Calcular y registrar los incrementos solicitados, luego mostrar del resultado final obtenido las tarifas y los precios actualizados

tarifas = {tarifa : valor}
           string   float
           clave
           
variable sugerida: 
    incremento_valor
    tarifa = T1-R1 El valor se debe incrementar un 20%
    tarifa = T2-R1 El valor se debe incrementar un 20%
    Para el resto de las tarifas el valor se debe incrementar un 40%
"""
tarifas_actualizadas = {}

for tarifa, valor in tarifas.items():
    
    if tarifa == 'T1-R1':
        valor_actualizado = valor + (valor * 0.20)
    elif tarifa == 'T2-R1':
        valor_actualizado = valor + (valor * 0.30)
    else:
        valor_actualizado = valor + (valor * 0.40)
        
    tarifas_actualizadas[tarifa] = valor_actualizado
    
print("tarifas y valores actualizados")
for tarifa, valor_actualizado in tarifas_actualizadas.items():
    print(f"Tarifa: {tarifa}, Valor actualizado: ${valor_actualizado:.2f}")
