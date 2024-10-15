"""
Registrar los servicios facturados de un periodo, ademas deberá calcular por cada servicio facturado
Dependiendo Del consumo lo siguiente:
consumo <1000 kWh se aplicará un descuento del 20% al valor final
Consumo >=1000 kWh y <2000 kWh se aplicará un descuento del 10% al valor final
Consumo >=2000 kWh y <3000 kwh se aplicará un descuento del 5% al valor final
Consumo >=3000 kWh no se aplicará un descuento al valor fina
Debera ingresar el periodo por teclado



consumos = {id_consumo:[cuenta,consumo_kwh,periodo]}
              int        int       int      string    
             clave        0         1          2   

facturas_servicios = {
    id_factura:[cuenta,consumo_kwh,tarifa,valor_final]}
       int         int      int     string      float
       clave        0        1         2          3

"""


periodo_analizar = input("Ingrese el periodo a analizar ")

for id_factura, datos in facturas_servicios.items():
    
    id_factura, cuenta, consumo_kwh, tarifa, valor_final = datos
    periodo = consumos[cuenta][2]
    
    if periodo == periodo_analizar:
        if consumo_kwh < 1000:
            valor_actualizado = valor_final - (valor_final * 0.20)
        elif 1000 <= consumo_kwh < 2000:
            valor_actualizado = valor_final - (valor_final * 0.10)
        elif 2000 <= consumo_kwh < 3000:
            valor_actualizado = valor_final - (valor_final * 0.05)
        else:
            valor_actualizado = valor_final
            
        print(f"Factura ID: {id_factura}, Consumo: {consumo_kwh} kWh, Valor final actualizado: ${valor_actualizado:.2f}")
            
            
        