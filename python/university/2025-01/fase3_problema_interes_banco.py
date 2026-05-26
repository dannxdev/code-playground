# Problema 4: Un banco está ofreciendo interés al 0.7% mes vencido a la
# cantidad de meses que el cliente desee. Se requiere una aplicación que le
# proyecte a un cliente cuánto dinero obtendrá si deposita un capital
# determinado a un número de meses, esta información se debe capturar
# por teclado. Se debe mostrar por pantalla el capital mes a mes hasta el
# número de meses capturado.

def interes_banco(capital, cant_meses):
    capital_inicial = capital
    print(f"\nCapital Inicial: ${capital}\n")
    for mes in range(1, cant_meses + 1):
        capital_con_intereses = (capital * 0.007) + capital
        print(f"Capital Mes {mes}: ${round(capital_con_intereses, 2)}")
        capital = capital_con_intereses
        if mes == cant_meses:
            ganancia = capital - capital_inicial
            porcentaje_crecimiento = (ganancia * 100) / capital_inicial
            print(
                f"\nTu capital crecio ${round(ganancia, 2)} un {round(porcentaje_crecimiento, 2)}%.\n")


if __name__ == "__main__":
    print("========================================")
    print("      Problema 4: Interes Banco      ")
    print("========================================\n")

    capital_usuario = int(input("Ingrese el capital: "))
    cantidad_meses = int(input("Ingrese la cantidad de meses: "))

    interes_banco(capital_usuario, cantidad_meses)
