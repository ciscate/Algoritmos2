
total_autos = 0
suma_costos = 0
suma_precios = 0

autos = {}

for marca, datos in concesionario.items():
    
    costo, anio, cantidad, precio, version, combustible = datos
    
    total_autos += cantidad
    suma_costos += costo
    suma_precios += precio
    
    costo_promedio = suma_costos / cantidad
    precio_promedio = suma_precios / cantidad
    
    autos[marca] = [costo_promedio, precio_promedio]
    
for marca, datos in autos.items():
    
    costo_promedio, precio_promedio = datos
    print(f"El auto {marca} tiene un costo promedio de ${costo_promedio:.2f} y su precio promedio de venta es de ${precio_promedio:.2f}")

print(f"El total de autos es de {total_autos}")
    
    
    
    
    