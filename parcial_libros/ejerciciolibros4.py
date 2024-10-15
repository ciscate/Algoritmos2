"""
Registrar todas las ventas realizadas, ademas deberá calcular por cada venta dependiendo de la forma de pago
Lo siguiente
Forma de pago = 1 [Efectivo] Aplicar un 15% de descuento al total de la compra
Forma de pago = 2 [Tarjeta de débito] Aplicar un 10% de descuento al total de la compra
Forma de pago = 3 [Tarjeta de crédito] No aplicar descuento al total de la compra

ventas = {id_venta:[id_libro, cantidad, precio, total, forma_pago]}
           int        int       int     float   float     int 
           clave      0          1         2       3        4
           
"""
datos_venta = {}

for id_venta, datos in ventas.items():
    
    id_libro, cantidad, precio, total, forma_pago = datos
    
    if forma_pago == 1:
        descuento = total * 0.15
    elif forma_pago == 2:
        descuento = total * 0.10
    else:
        descuento = 0
        
    precio_final = total - descuento
    
    datos_venta[id_venta] = precio_final
    
for id_venta, precio_final in datos_venta.items():
    print(f"La venta nro: {id_venta} con el descuento correspondiente tiene un precio final de: {precio_final:.2f}")
    
    
    