from colorama import Fore, Style
import os
import time
import random

def game():
    
    os.system("cls")

    palabras = ["agua", "aire", "alambre", "alcohol", "alfombra", "alimento", "almohada", "amigo", "amor", "animal",
                "anillo", "aniversario", "anteojos", "apartamento", "armario", "arte", "asiento", "auto", "avenida", "avion",
                "baile", "balcon", "bandera", "banqueta", "barrio", "batido", "bicicleta", "billete", "bizcocho", "bocadillo",
                "bolso", "bolsillo", "bomba", "bote", "botella", "brazo", "caballo", "cabello", "calle", "cama",
                "camiseta", "cancion", "carro", "casa", "celular", "cerveza", "chocolate", "cielo", "coche", "cocina",
                "colina", "color", "comida", "computadora", "corazon", "cuento", "cuerpo", "diente", "dinero", "dulce",
                "edificio", "elefante", "empresa", "enfermedad", "escuela", "escritorio", "espacio", "espejo", "estrella", "fiesta",
                "fuego", "futbol", "gafas", "galleta", "gato", "guitarra", "habitacion", "hamburguesa", "helado", "hombre",
                "hoja", "hombre", "hospital", "hotel", "humo", "iglesia", "isla", "jabon", "jardin", "joya",
                "juego", "lago", "libro", "luz", "maleta", "mano", "mar", "mesa", "mochila", "montana",
                "naranja", "nino", "noche", "nube", "ojo", "oso", "pajaro", "palabra", "pantalla", "panuelo",
                "parque", "paso", "pastel", "pelota", "perro", "pescado", "piano", "playa", "plaza", "pueblo",
                "puerta", "puesto", "rio", "regalo", "reloj", "restaurante", "ropa", "silla", "sol", "sombrero",
                "sueno", "taza", "tren", "trabajo", "universidad", "vino", "yogur", "zapato", "arbol", "ultimo",
                "aceite", "acera", "adorno", "afuera", "alfiler", "alga", "almacen", "amplio", "anden", "ancho",
                "angulo", "antena", "apellido", "arena", "area", "arena", "asado", "asador", "asfalto", "astronomo",
                "aventura", "aviso", "avenida", "avion", "ayer", "banda", "bandeja", "banquero", "barco", "barrio",
                "bateria", "bautizo", "bebe", "beso", "bicicleta", "billetera", "billete", "boda", "bolsillo", "bomba",
                "bordado", "borrador", "brazalete", "caballo", "cabello", "cabeza", "cafe", "calle", "camion", "camino",
                "caminante", "campo", "cancion", "candado", "canon", "caracol", "caravana", "caramelo", "carne", "carta",
                "casa", "cascada", "casco", "castillo", "cayendo", "cebolla", "cedro", "celebracion", "celular", "cena",
                "cereza", "cerilla", "cicatriz", "ciego", "cigarro", "ciudad", "cielo", "ciruela", "coche", "coco",
                "codigo", "cola", "colina", "cometa", "comida", "compas", "computadora", "concierto", "conductor", "conejito",
                "conferencia", "construccion", "corazon", "correo", "correr", "cosecha", "crema", "cruz", "cuaderno", "cuerpo",
                "culebra", "cultura", "cumpleanos", "dama", "danza", "dentista", "desayuno", "desierto", "dibujo", "dientes",
                "dinero", "disfraz", "doctor", "dolor", "dulce", "durazno", "ebano", "eclipse", "economia", "edificio",
                "educacion", "elefante", "emocion", "enfermero", "entrenador", "escalera", "escritorio", "espada", "espejo", "esqueleto",
                "estacion", "estomago", "estrella", "excursion", "familia", "fiesta", "flor", "fogata", "fondo", "fotografia",
                "fuego", "fuente", "futbolista", "galaxia", "galleta", "gato", "globo", "golosina", "guitarra", "gusano",
                "hada", "helado", "heroe", "hierba", "hoja", "hombre", "hongo", "huracan", "iglesia", "ilusion",
                "invierno", "isla", "jabon", "jardin", "jirafa", "jiron", "juego", "lagarto", "lagrima", "lago",
                "lampara", "leccion", "libro", "luz", "maleta", "manzana", "mar", "medalla", "mente", "milagro",
                "misterio", "monstruo", "mujer", "nacimiento", "nieve", "nube", "ola", "oreja", "oro", "oso",
                "pajaro", "palabra", "pantalla", "panuelo", "parque", "paso", "pastel", "pelota", "perro", "pescado",
                "piano", "playa", "plaza", "pueblo", "puerta", "puesto", "rio", "regalo", "reloj", "restaurante",
                "ropa", "silla", "sol", "sombrero", "sueno", "taza", "tren", "trabajo", "universidad", "vino",
                "yogur", "zapato", "arbol", "ultimo","aceituna", "agujero", "almohada", "almohadon", "ancla", "anecdota",
                "anemona", "arcilla", "arcangel", "bambu", "banquito", "banquillo", "barquito", "barra", "baritono", "baston",
                "batea", "batuta", "beba", "ano", "bisabuelo", "bisagra", "boina", "bolita", "bota", "boton",
                "buhardilla", "buho", "cabrito", "cachorro", "cachucha", "cactus", "cafecito", "cafetera", "caja", "calabaza",
                "calma", "campana", "canasta", "cancion", "candil", "caracol", "carita", "carpeta", "casita", "casona",
                "cebo", "cebolla", "cigarrillo", "ciudadela", "cortina", "cuentagotas", "cuento", "cuerito", "cuero", "cuna",
                "dama", "dormitorio", "dragon", "duda", "ducha", "dulzura", "emocion", "enfermo", "escoba", "escopeta",
                "espada", "espalda", "espejito", "estacion", "estampa", "estampilla", "estatuilla", "etiqueta", "farol", "felicidad",
                "flor", "fogon", "fotografia", "galletita", "gatito", "guitarra", "gusanito", "hadita", "harina", "herramienta",
                "hoja", "huevito", "ilusion", "imaginacion", "imperdible", "joyita", "juguetito", "junio", "lamparita", "lanzallamas",
                "lapiz", "luciernaga", "maceta", "manita", "manta", "mantita", "manzanita", "mariposa", "mascota", "mesita",
                "montanita", "montana", "muneca", "nino", "osito", "papelito", "papelon", "pastillita", "perrito", "piedrita",
                "pirulin", "placard", "placita", "placita", "platito", "plumita", "poesia", "policia", "pollito", "pulsera",
                "ramita", "rata", "ratita", "raton", "rocola", "rulito", "sabiduria", "silla", "sonrisa", "sorbito",
                "tobillo", "tortita", "una", "ventanita", "vestidito", "zapatito", "zapato"]

    palabra_aleatoria = random.choice(palabras)

    correcto = False

    palabras_ingresadas = []  # Lista para almacenar las palabras ingresadas por el usuario
    letras_correctas = [] # Lista para almacenar letras correctas de las palabras ingresadas por el usuario
    
    tamaño_palabra = len(palabra_aleatoria)
    
    while correcto == False:
        print("Es una palabra de "+str(tamaño_palabra)+" letras")

        palabra_secreta = palabra_aleatoria
        for caracter in palabra_aleatoria:
            if caracter not in letras_correctas:
                palabra_secreta = palabra_secreta.replace(caracter,"_") # Voy reemplazando las letras que el usuario acierta

        print(palabra_secreta+" .")
        palabra = input("\nAdivina la palabra: ")
        os.system("cls")

        # Resaltar las letras que coinciden
        highlighted_word = ""
        for i in range(len(palabra)):
            letra_palabra = palabra[i]

            if i >= len(palabra_aleatoria):
                letra_traduccion = None
            else:
                letra_traduccion = palabra_aleatoria[i]

            if letra_palabra == letra_traduccion: # pinto las letras correctas en la posicion correcta
                highlighted_word += Fore.GREEN + letra_palabra + Style.RESET_ALL
                letras_correctas.append(letra_palabra) # si pinto la letra la agrego al arreglo de letras correctas
            else:
                highlighted_word += Fore.RED + letra_palabra + Style.RESET_ALL

        palabras_ingresadas.append(highlighted_word)  # Agregar la palabra ingresada a la lista

        print("Palabra ingresada:", highlighted_word)

        if palabra.lower().replace(" ", "") == palabra_aleatoria.lower().replace(" ", ""): # Si es correcta termino el bucle
            correcto = True

    print("\nCorrecto!")
    time.sleep(1)

            # Para imprimir las palabras ingresadas
    print("\nPalabras ingresadas por el usuario:")
    for p in palabras_ingresadas:
        print(p)
        
    time.sleep(0.5)

    print("\nCantidad de intentos: "+str(len(palabras_ingresadas)))
    
    time.sleep(0.5)

def main():
    keepPlaying = True
    while keepPlaying:
        game()
        flag = None  # Inicializa flag como None
        while flag not in (1, 2):  # Utiliza un conjunto de valores válidos
            respuesta = input("\n¿Volver a jugar? (1. Si / 2. No): ")
            if respuesta.strip().isdigit():  # Verifica si la entrada contiene solo dígitos
                flag = int(respuesta)
                if flag == 1:
                    break
                elif flag == 2:
                    keepPlaying = False
                else:
                    os.system("cls")
                    print("Opción no válida. Por favor, ingrese 1 o 2.")
                    time.sleep(1)
            else:
                os.system("cls")
                print("Entrada no válida. Por favor, ingrese 1 o 2.")
                time.sleep(1)

if __name__ == "__main__":
    main()