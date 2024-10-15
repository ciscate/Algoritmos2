"""
Calcular y mostrar el total y el promedio de los consumos de un periodo. Tener en cuenta que el periodo se ingresa por teclado

consumos = {id_consumo:[cuenta,consumo_kwh,periodo]}
              int        int       int      string    
             clave        0         1          2   

variables sugeridas:
    consumo_total,
    consumo_medio
"""
sumatoria_consumo = 0
cantidad_consumos = 0

periodo = input("Ingrese el periodo a analizar ")

for id_consumo, datos in consumo.items():
    
    consumo, periodo, periodo_consumo = datos
    
    if periodo_consumo == periodo:
        sumatoria_consumo += consumo
        cantidad_consumos += 1
    
if cantidad_consumos > 0:
    consumo_medio = sumatoria_consumo / cantidad_consumos
else:
    consumo_medio = 0
    
print(f"El consumo medio del periodo {periodo} fue de {consumo_medio:.2f}kwh de un consumo total de {sumatoria_consumo:.2f}kwh")
    

