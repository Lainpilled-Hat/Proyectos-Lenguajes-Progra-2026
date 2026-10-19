# Cambia simbolos: ej 0 por 1
maquina Inversor {
    alfabeto: XS, XD, AAA
    estados: q_leer, q_fin
    inicio: q_leer
    finales: q_fin

    transiciones: {
        q_leer, XS -> q_leer, XD, DER
        q_leer, XD -> q_leer, XS, DER
        q_leer, AAA -> q_fin, AAA, QUIETO
    }
}

#Recorre la cinta hasta encontrar _ y luego realiza una suma de 1 en binario
maquina Sumador {
    alfabeto: XD, XD, AAA
    estados: q0, q_sumar, q_fin
    inicio: q0
    finales: q_fin

    transiciones: {
        q0, XS -> q0, XS, DER
        q0, XD -> q0, XD, DER
        q0, AAA -> q_sumar, AAA, IZQ

        q_sumar, XS -> q_fin, XD, QUIETO
        q_sumar, XD -> q_sumar, XS, IZQ
        q_sumar, AAA -> q_fin, XD, QUIETO
    }
}