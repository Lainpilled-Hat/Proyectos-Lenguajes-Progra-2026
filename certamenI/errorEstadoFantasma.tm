maquina ErrorEstadoFantasma {
    alfabeto: x, y
    estados: q0, q1, q_fin
    inicio: q0
    finales: q_fin

    transiciones: {
        q0, x -> q1, y, DER
        q1, BLANCO -> q_fin, BLANCO, QUIETO
        
        # ERROR: q_magico no existe en la declaración de estados
        q1, x -> q_magico, y, DER
    }
}