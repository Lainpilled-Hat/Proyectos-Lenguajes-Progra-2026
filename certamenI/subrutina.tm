# DEFINICIÓN DE LA SUBRUTINA
# Recibe un parámetro N. Al compilar, la 'N' se reemplaza por el número entero indicado.
subrutina marcar_celdas(N) {
    q_paso_N, _ -> q_fin_N, 1, DER
}

#DEFINICIÓN DE LA MÁQUINA 
maquina ProcesadorConSubrutina {
    alfabeto: 0, 1, _
    estados: q0, q_paso_3, q_fin_3, q_fin
    inicio: q0
    finales: q_fin

    # Invocación de la subrutina
    usa marcar_celdas(3)

    transiciones: {
        q0, 0 -> q0, 0, DER
        q0, 1 -> q0, 1, DER
        
        # Conecta el flujo principal con los estados generados por la subrutina
        q0, _ -> q_paso_3, _, QUIETO
        
        q_fin_3, _ -> q_fin, _, QUIETO
    }
}