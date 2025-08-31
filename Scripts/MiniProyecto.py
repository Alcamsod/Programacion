import calendar
from datetime import datetime

##################################
########## MiniProyecto ##########
##################################


def conversion_divisa(dinero: float, tipo_cambio: float, moneda: str):
    """
    Funcion que recibe una cantidad de dinero en euros el tipo de cambio para obtener el valor en AUD. El tipo de cambio es el de € -> $, si se pone otro no será un retorno real
    """
    print("💰 Realizando la conversión de moneda")
    if moneda == "EUR":
        convertido = dinero * tipo_cambio
        print(f"💸 {dinero} € equivalen a {convertido} AUD")
    elif moneda == "AUD":
        convertido = dinero / tipo_cambio
        print(f"💸 {dinero} AUD equivalen a {convertido} €")
    else:
        print(" Has introducido una moneda que no contemplo")
        convertido = None
    return convertido


def gastos(gastos_totales, gasto, moneda):
    """
    Función que registra los gastos diarios en EUROS
    """
    if moneda == "EUR":
        gastos_totales.append(gasto)
        print(f"📄 Se ha añadido un gasto de {gasto} €")
    elif moneda == "AUD":
        gasto_euros = conversion_divisa(gasto, 1.62, "AUD")
        gastos_totales.append(gasto_euros)
        print(
            f"📄 Se ha añadido un gasto de {gasto} €, tras convertirlo desde {moneda}"
        )
    return gastos_totales


def calcular_presupuesto_diario(ahorro_euros, salario_mensual, gastos_totales):
    """
    Función que calcula el presupuesto diario a partir de los ingresos totales y una intención de ahorro
    """
    today = datetime.today()
    dias_mes = calendar.monthrange(today.year, today.month)[1]
    salario_mensual_eur = conversion_divisa(salario_mensual, 1.62, "AUD")
    presupuesto_diario = (salario_mensual_eur - ahorro_euros - sum(gastos_totales)) / dias_mes
    if presupuesto_diario < 0:
        print("🚨 ¡Atención! Tu presupuesto diario es negativo.")
        return None
    else:
        print(f"💸 Tu presupuesto diario es de {presupuesto_diario} €")
        return presupuesto_diario


#### Ahora hacemos un script que llame a todas las funciones
# Imaginemos que tenemos ya un salario, unos gasto y un objetivo de ahorro.

SALARIO_MENSUAL = 3000 # AUD
GASTOS = [500, 200, 150, 70]
AHORRO_OBJETIVO = 500 # EUR

# Tenemos un nuevo gasto
nuevos_gastos = gastos(GASTOS, 50, "EUR")
# He recibido un dinero en AUD de ayuda
AYUDA = 200 #AUD
ayuda_eur = conversion_divisa(AYUDA, 1.62, "AUD")
# Calculamos el presupuesto
presupuesto = calcular_presupuesto_diario(AHORRO_OBJETIVO, SALARIO_MENSUAL, nuevos_gastos)