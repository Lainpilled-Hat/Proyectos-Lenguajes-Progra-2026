# Recibe un parámetro N. BLANCO se reemplaza por el tercer argumento de main.py.
subrutina marcar_celdas(N) {
    q_paso_N, BLANCO -> q_fin_N, 1, DER
}

# DEFINICIÓN DE LA MÁQUINA
maquina ProcesadorConSubrutina {
    alfabeto: 0, 1
    estados: q0, q_paso_3, q_fin_3, q_fin
    inicio: q0
    finales: q_fin

    # Llamada estilo función; el entero se usa porque esta subrutina lo requiere.
    marcar_celdas(3)

    transiciones: {
        q0, 0 -> q0, 0, DER
        q0, 1 -> q0, 1, DER
        
        # Conecta el flujo principal con los estados generados por la subrutina.
        q0, BLANCO -> q_paso_3, BLANCO, QUIETO
        
        q_fin_3, BLANCO -> q_fin, BLANCO, QUIETO
    }
}