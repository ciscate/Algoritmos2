"""
Calcular y mostrar la cantidad de usuarios de una localidad, ademas del porcentaje que ocupa respecto
del partido al que pertenece. Tener en cuenta que la localidad se ingresa por teclado

usuarios = {cuenta:[usuario,localidad,partido,tarifa]
             int     string   string  string  string
            clave      0         1       2      3
}

variables sugeridas: 
    cantidad_usuarios,
    porcentaje_usuarios
"""

cantidad_usuarios = 0
cantidad_usuarios_partido = 0


localidad = input("Ingrese la localidad ")

for cuenta, datos in usuarios.items():
    
    usuario, localidad_usuario, partido_usuario, tarifa = datos
    
    if localidad == localidad_usuario:
        partido_localidad = partido_usuario
        
if partido_localidad:
    for cuenta, datos in usuarios.items():
        
        usuario, localidad_usuario, partido_usuario, tarifa = datos
        
        if localidad == localidad_usuario:
            cantidad_usuarios += 1
        
        if partido_usuario == partido_localidad:
            cantidad_usuarios_partido += 1
            
if cantidad_usuarios_partido > 0:
    porcentaje_usuarios = (cantidad_usuarios / cantidad_usuarios_partido) * 100
else:
    porcentaje_usuarios = 0
    
print(f"La cantidad de usuarios en {localidad} es: {cantidad_usuarios}")
print(f"El porcentaje de usuarios en la localidad respecto al partido es: {porcentaje_usuarios:.2f}%")

        