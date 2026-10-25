maquina RevisarTercerSimbolo {
    alfabeto: a, b
    estados: q_leer, q_acepta, q_rechaza
    inicio: q_leer
    finales: q_acepta

    desplazar(2)

    transiciones: {
        q_leer, a -> q_rechaza, a, QUIETO
        q_leer, b -> q_acepta, b, QUIETO
        q_leer, BLANCO -> q_rechaza, BLANCO, QUIETO
    }
}