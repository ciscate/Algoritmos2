"""
Buscar el mayor y el menor consumo, y mostrar de ellos el usuario, el consumo y el periodo

usuarios = {cuenta:[usuario,localidad,partido,tarifa]
             int     string   string  string  string
             clave     0         1       2      3
}

consumos = {id_consumo:[cuenta,consumo_kwh,periodo]}
              int        int       int      string    
                          0         1          2          
"""
datos_guardados = False
datos_mayor = []
datos_menor = []

for id_consumo, datos in consumos.items():
    
    cuenta, consumo, periodo = datos
    usuario = usuarios[cuenta][0]
    
    if not datos_guardados:
        mayor_consumo = menor_consumo = consumo
        datos_mayor = datos_menor = [usuario, periodo, consumo]
        datos_guardados = True
    else:
        if consumo > mayor_consumo:
            mayor_consumo = consumo
            datos_mayor = [usuario, periodo, consumo]
        
        if consumo < menor_consumo:
            menor_consumo = consumo
            datos_menor = [usuario, periodo, consumo]

usuario_mayor, periodo_mayor, consumo_mayor = datos_mayor
print(f"El usuario {usuario_mayor} generó el mayor consumo: {consumo_mayor} kWh en el periodo {periodo_mayor}")

usuario_menor, periodo_menor, consumo_menor = datos_menor
print(f"El usuario {usuario_menor} generó el menor consumo: {consumo_menor} kWh en el periodo {periodo_menor}")



