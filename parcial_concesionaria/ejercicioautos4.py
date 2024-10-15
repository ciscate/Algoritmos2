
ventas_actualizadas = {}

for factura, datos in ventas.items():
    
    patente, marca, precio, total, forma_pago = datos
    
    if forma_pago == 1:
        descuento = precio * 0.15
        total_actualizado = precio - descuento
    elif forma_pago == 2:
        incremento = precio * 0.07
        total_actualizado = precio + incremento
    elif forma_pago == 3:
        incremento = precio * 0.33
        total_actualizado = precio + incremento
    else:
        incremento = 0
    
    ventas_actualizadas[factura] = total_actualizado
    
for factura, total_actualizado in ventas_actualizadas.items():
    print(f"La factura {factura} tiene un valor actualizado de ${total_actualizado:.2f}")
    
    
    