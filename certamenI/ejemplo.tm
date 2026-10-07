# Cambia simbolos: ej 0 por 1
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

#Recorre la cinta hasta encontrar _ y luego realiza una suma de 1 en binario
maquina Sumador {
    alfabeto: 0, 1, _
    estados: q0, q_sumar, q_fin
    inicio: q0
    finales: q_fin

    transiciones: {
        q0, 0 -> q0, 0, DER
        q0, 1 -> q0, 1, DER
        q0, _ -> q_sumar, _, IZQ

        q_sumar, 0 -> q_fin, 1, QUIETO
        q_sumar, 1 -> q_sumar, 0, IZQ
        q_sumar, _ -> q_fin, 1, QUIETO
    }
}