
faltantes = {}
importe_total = 0

for marca, datos in concesionario.items():
    
    costo, anio, cantidad, precio, version, minimo, combustible = datos
    
    if cantidad < minimo:
        reposicion = (minimo - cantidad) + 10
        costo_reposicion = reposicion * costo
        
        faltantes[marca] = [reposicion,costo_reposicion]
        
        importe_total += costo_reposicion
        
for marca, datos in faltantes.items():
    
    reposicion, costo_reposicion = datos
    
    print(f"El auto {marca}, se encuentra en faltante y hay que reponer {reposicion} unidades a un costo de {costo_reposicion:.2f}")

print(f"El importe total de la reposicion general es: ${importe_total:.2f}")
        
        