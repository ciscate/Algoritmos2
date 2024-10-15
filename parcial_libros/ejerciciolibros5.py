"""
Calcular y registrar sólo los libros que se encuentran en falta para la venta. Tener en cuenta que
para hacerlo Deberá la cantidad disponible ser menor que la cantidad mínima. Ademas de reponer
el mínimo, deberá haber una cantidad mínima de 10 libros mas sobre el el mínimo establecido. Al
finalizar la carga de los faltantes se deberá ademas calcular el importe total que se abonara por la
reposición de los libros que se encuentran en falta. Por ejemplo para calcular los libros faltantes: Si
hay solo 3 libros disponibles y el mínimo que debe haber es de 7, la compra debería realizarse es
de 14 libros.

libreria = {id_libro:[titulo,autor,genero,cantidad,minimo,costo,precio]
              int    string string string   int     int   float  float
             clave      0      1      2      3       4      5      6
}

faltantes = {id_libro:[cantidad, costo]}
               int        int    float
               clave      0        1

variable sugerida:
    importe_total
"""
importe_total = 0

for id_libro, datos in libreria.items():
    
    titulo, autor, genero, cantidad, minimo, costo, precio = datos
    
    if cantidad < minimo:
        cantidad_reponer = (minimo - cantidad) + 10
        
        costo_reposicion = cantidad_reponer * costo
        
        faltantes[id_libro] = [cantidad_reponer, costo_reposicion]
        
        importe_total += costo_reposicion
        
for id_libro, datos_faltantes in faltantes.items():
    
    cantidad_reponer, costo_reposicion = datos_faltantes
    titulo = liberia[id_libro][0]
    
    print(f"Libro en falta. {titulo}, cantidad a reponer: {cantidad_reponer}, costo total: ${costo_reposicion:.2f}")

print(f"Importe total a abonar por la reposicion de los libros faltantes: ${importe_total:.2f}")

