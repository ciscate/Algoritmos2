valores_actualizados = {}

for marca, datos in concesionario.items():
    
    costo, anio, cantidad, precio, version, combustible = datos
    
    if version == 1:
        incremento = precio * 0.20
    elif version == 7:
        incremento = precio * 0.15
    else:
        incremento = precio * 0.10
        
    precio_final = precio + incremento
    
    valores_actualizados[marca] = precio_final
    
for marca, precio_final in valores_actualizados.items():
    
    print(f"El auto {marca} tiene un precio final de ${precio_final:.2f}")
    