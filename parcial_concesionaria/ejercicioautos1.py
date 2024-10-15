datos_guardados = False
mayores = []
menores = []

for marca, datos in concesionario.items():
    
    costo, anio, cantidad, precio, version, combustible = datos
    
    if not datos_guardados:
        mayor_precio = menor_precio = precio
        mayor_anio = menor_anio = anio
        datos_guardados = True
    else:
        if mayor_precio < precio:
            mayor_precio = precio
        if menor_precio > precio:
            menor_precio = precio
        if mayor_anio < anio:
            mayor_anio = anio
        if menor_anio > anio:
            menor_anio = anio
        
print(f"El mayor anio es {mayor_anio} y el mayor precio es: ${mayor_precio:.2f}")
print(f"El menor anio es {menor_anio} y el menor precio es ${menor_precio:.2f}")
        