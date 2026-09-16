maquina Incrementador {
    alfabeto: 0, 1, _
    estados: q0, q_sumar, q_fin
    inicio: q0
    finales: q_fin

    usa desplazar(1)

    transiciones: {
        q0, 0 -> q0, 0, DER
        q0, 1 -> q0, 1, DER
        q0, _ -> q_sumar, _, IZQ

        q_sumar, 0 -> q_fin, 1, QUIETO
        q_sumar, 1 -> q_sumar, 0, IZQ
        q_sumar, _ -> q_fin, 1, QUIETO
    }
}