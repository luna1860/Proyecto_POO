def main():
    nombres = []
    for i in range(1, 2): # Ajusta el rango según sea necesario
        nombre = solicitar_nombre()
        nombres.append(nombre)

    jugadores = [Jugador(nombre) for nombre in nombres]
    juego = Juego(jugadores)
    juego.jugar()
    mostrar_resultados_finales(juego.resultados_rondas)

if __name__ == "__main__":
    main()