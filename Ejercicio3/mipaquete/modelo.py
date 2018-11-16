import abc


class PersonaEquipo(metaclass=abc.ABCMeta):
    """
        se define la clases abstracta
    """
    #__metaclass__ = abc.ABCMeta
    
    def __init__(self, nom):
        self.nombre = nom
    def obtener_nombre(self):
        return self.nombre 
    @abc.abstractmethod
    def entrenar():
        pass

class Futbolista(PersonaEquipo):
    def __init__(self,n):
        super(Futbolista, self).__init__(n)
    def entrenar(self):
        print("Yo %s futbolista, hago práctica en el entrenamiento"%self.obtener_nombre())

class Medico(PersonaEquipo):
    def __init__(self,n):
        super(Medico,self).__init__(n)
    def entrenar(self):
        print  ("Yo %s medico, atiendo a los jugadores en el entrenamiento." % self.obtener_nombre())
class Presidente(PersonaEquipo):
    def __init__(self,n):
        super(Presidente,self).__init__(n)
    def entrenar(self):
        print ("Yo %s presidente, pongo el dinero para el entrenamiento." % self.obtener_nombre())

class Entrenador(PersonaEquipo):
    """docstring for Entrenador"""
    def __init__(self, n):
        super(Entrenador, self).__init__(n)
    def entrenar(self):
        print ("Yo %s entrenador, soy el director del entrenamiento." % self.obtener_nombre())       