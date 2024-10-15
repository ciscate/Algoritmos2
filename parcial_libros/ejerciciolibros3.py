"""
Calcular y registrar los incrementos solicitados, ademas de mostrar del resultado final obtenido solo los títulos y
precios

libreria = {id_libro:[titulo,autor,genero,cantidad,minimo,costo,precio]
              int    string string string   int     int   float  float
             clave      0      1      2      3       4      5      6                
}

variables sugeridas:
    incremento_precio: Genero = 1(Infantil) El precio se debe incrementar un 30%
                       Genero = 7(Suspenso) El precio se debe incrementar un 30%
                       El resto de os generos, el precio se debe incrementar un 20%
"""
datos_actualizados = {}

for id_libro, datos in libreria.items():
    
    titulo, autor, genero, cantidad, minimo, costo, precio = datos
    
    if genero in ['Infantil', 'Suspenso']:
        incremento_precio = precio * 0.30
    else:
        incremento_precio = precio * 0.20
        
    precio_actualizado = precio + incremento_precio
    
    datos_actualizados[titulo] = precio_actualizado
    
for titulo, precio_actualizado in datos_actualizados.items():
    print(f"El titulo del libro es: {titulo} y su precio fue actualizado a: {precio_actualizado:.2f}")
    


        
    