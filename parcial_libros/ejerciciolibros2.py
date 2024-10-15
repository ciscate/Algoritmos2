"""
Calcular y mostrar el total de los libros, ademas del promedio de los costos y precios 

libreria = {id_libro:[titulo,autor,genero,cantidad,minimo,costo,precio]
              int    string string string   int     int   float  float
             clave      0      1      2      3       4      5      6
}

variables sugeridas:
    total_libros
    costo_medio
    precio_medio

"""

total_libros = 0
suma_precios = 0
suma_costos = 0

datos_libro = []


for id_libro, datos in libreria.items():
    
    titulo, autor, genero, cantidad, minimo, costo, precio = datos
    
    total_libros += cantidad
    suma_precios += precio
    suma_costos += costo
    
costo_medio = suma_costos / total_libros
precio_medio = suma_precios / total_libros
    
print(f"Cantidad de libros: {total_libros}, su costo medio es de: {costo_medio:.2f} y su precio medio es: {precio_medio:.2f}")

    
    
    