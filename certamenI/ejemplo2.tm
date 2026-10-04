maquina Inversor {
    alfabeto: 0, 1, _
    estados: q_leer, q_fin
    inicio: q_leer
    finales: q_fin

    transiciones: {
        q_leer, 0 -> q_leer, 1, DER
        q_leer, 1 -> q_leer, 0, DER
        q_leer, _ -> q_fin, _, QUIETO
    }
}