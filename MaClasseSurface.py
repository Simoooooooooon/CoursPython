class CalculateurSurface:
    
    # Initialisons la classe
    def __init__(self, precision):
        self.precision = precision

    def calculer_aire_rectangle(self, longueur, largeur):
        aire = longueur * largeur
        return round(aire, self.precision)

    def calculer_aire_cercle(self, rayon):
        import math
        aire = math.pi * rayon ** 2
        return round(aire, self.precision)