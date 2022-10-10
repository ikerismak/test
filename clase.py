
# La clase ropa con solo un metodo que recibe esos dos argumentos como indica el problema

class Ropa:

    def descuento(self, costo, tipo):
        descuento = 0
        if tipo == 'fueraDeTemporada':
            if costo < 500:
                descuento = 10
            elif costo >= 500 and costo <= 5000:
                descuento = 20
            else:
                descuento = 0
        else:
            if costo < 1000:
                descuento = 5
            elif costo >= 1000 and costo <= 6000:
                descuento = 10

            else:
                descuento = 0

        return descuento
