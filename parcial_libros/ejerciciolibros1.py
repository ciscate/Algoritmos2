"""
Buscar y mostrar el mayor y el menor precio, ademas del mayor y menor costo

libreria = {id_libro:[titulo,autor,genero,cantidad,minimo,costo,precio]
              int    string string string   int     int   float  float
             clave      0      1      2      3       4      5      6
}

variables sugeridas:
    mayor_precio
    menor_precio
    mayor_costo
    menor_costo
"""

datos_guardados = False

for id_libro, datos in libreria.items():
    
    titulo, autor, genero, cantidad, minimo, costo, precio = datos
    
    if not datos_guardados:
        mayor_precio = precio
        menor_precio = precio
        mayor_costo = costo
        menor_costo = costo
        datos_guardados = True
    else:
        if mayor_precio < precio:
            mayor_precio = precio
        if menor_precio > precio:
            menor_precio = precio
        if mayor_costo < costo:
            mayor_costo = costo
        if menor_costo > costo:
            menor_costo = costo
            
print(f"El mayor precio es: ${mayor_precio:.2f}")
print(f"El menor precio es: ${menor_precio:.2f}")
print(f"El mayor costo es: ${mayor_costo:.2f}")
print(f"El menor costo es: ${menor_costo:.2f}")

