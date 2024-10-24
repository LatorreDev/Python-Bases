#!/usr/bin/env python3
# Poo in Python

class Personaje:
# Método constructor
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
        self.nombre = nombre
        self.fuerza = fuerza
        self.inteligencia = inteligencia
        self.defensa = defensa
        self.vida = vida
# Método
    def atributos(self):
        print("- Fuerza:", self.fuerza)
        print("- Inteligencia:", self.inteligencia)
        print("- Defensa:", self.defensa)
        print("- Vida:", self.vida)
# Método
    def subir_nivel(self, fuerza, inteligencia, defensa):
        self.fuerza = self.fuerza + fuerza
        self.inteligencia = self.inteligencia + inteligencia
        self.defensa = self.defensa + defensa
# Método
    def esta_vivo(self):
        return self.vida > 0
# Método
    def morir(self):
        self.vida = 0
        print ("La vida de", self.nombre, "baja a", self.vida)
        print(self.nombre, "Ha muerto")
# Método
    def daño(self, enemigo):
        return self.fuerza - enemigo.defensa
# Método
    def atacar(self, enemigo):
        daño = self.daño(enemigo)
        enemigo.vida = enemigo.vida - daño
        print(self.nombre, "Ha realizado", daño, "puntos de daño a", enemigo.nombre)
        if enemigo.esta_vivo():
            print ("La vida de", enemigo.nombre, "es", enemigo.vida)
        else:
            enemigo.morir()

# Clases que hereda de Personaje
class Guerrero(Personaje):
    # Inicializa la clase con un nuevo atributo añadido al final
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, espada):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.espada = espada

    # Cambio de arma
    def cambiar_arma(self):
        opcion = int(input("Elige un arma: (1) Acero Valyrio, daño 8. (2) Matadragones, daño 10: "))
        if opcion == 1:
            self.espada = 8
        elif opcion == 2:
            self.espada = 10
        else:
            print ("Número incorrecto")
    # Añadir Espada a clase guerrero
    def atributos(self):
        super().atributos()
        print("- Espada:", self.espada)

class Mago(Personaje):
    # Inicializa la clase con un nuevo atributo añadido al final
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, grimorio):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.grimorio = grimorio
    
    # Añadir Grimorio a clase mago
    def atributos(self):
        super().atributos()
        print("- Grimorio:", self.grimorio)
    
    # Define daño del mago
    def daño(self, enemigo):
        return self.inteligencia*self.grimorio - enemigo.defensa


print ("---- Personajes ----")
mi_personaje = Personaje("Dave", 10, 50, 15, 45)
mi_enemigo = Personaje("Ghoul", 5, 1, 3, 9)
mi_guerrero = Guerrero("Guts", 200, 50, 400, 1000, 5)
mi_mago = Mago("Alphonse", 10, 70, 20, 400, 66)
print ("----    ----")
print ("---- Personaje Base----")
mi_personaje.atributos()
print ("----    ----")
print ("---- Enemigo Base----")
mi_enemigo.atributos()
print ("----    ----")
# Sube de nivel
print (mi_personaje.nombre, "Ha subido de nivel, sus nuevas estadisticas son: ")
mi_personaje.subir_nivel(10, 30, 10)
# Nuevos Atributos modificados
mi_personaje.atributos()
print ("----    ----")
#print ("---- ¿Está vivo? ----")
#print(mi_personaje.esta_vivo())
#print ("----    ----")
#print ("---- Game Over ----")
#mi_personaje.morir()
#print ("----    ----")
print ("---- Enemigo aparece ----")
print ("Un", mi_enemigo.nombre, "Aparece en la arena de batalla frente a", mi_personaje.nombre)
print ("----    ----")
print ("---- Atacar ----")
print (mi_personaje.nombre, "Decide atacar")
mi_personaje.atacar(mi_enemigo)
print ("----    ----")
print ("---- Nuevo personaje ----")
print (mi_guerrero.nombre, "se ha unido a la batalla como aliado de", mi_personaje.nombre)
print ("Sus estadisticas son: ")
mi_guerrero.atributos()
print ("----    ----")
print ("Elige tu arma: ")
mi_guerrero.cambiar_arma()
print ("----    ----")
print ("Las nuevas estadisticas de", mi_guerrero.nombre, "son: ")
mi_guerrero.atributos()
print ("----  Enemigo Aparece  ----")
print ("Un mago enemigo de nombre", mi_mago.nombre, "Aparece en la arena de batalla frente a", mi_personaje.nombre, "y", mi_guerrero.nombre)
print("Sus estadisticas son: ")
mi_mago.atributos()
print ("----    ----")
print(mi_mago.nombre, "Ataca a", mi_personaje.nombre)
mi_mago.atacar()
print ("----    ----")


