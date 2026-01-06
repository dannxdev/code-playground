import re
import string


def analizar_texto(text: str):
    text = text.lower()
    text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
    palabras = text.split()
    count = {}
    for palabra in palabras:
        count[palabra] = count.get(palabra, 0) + 1

    analisis = {
        "total_palabras": len(palabras),
        "palabras_unicas": set(palabras),
        "palabra_mas_frecuente": max(count, key=count.get, default="")
    }
    return analisis


texto = "En un pequeño pueblo rodeado de colinas verdes y cielos despejados, vivía un grupo de personas que dedicaban sus días a cultivar la tierra y cuidar de los animales. Cada mañana, el canto de los pájaros anunciaba el inicio de una jornada llena de trabajo y esperanza. Los niños corrían por los campos mientras los adultos compartían historias junto al fuego, recordando que la unión y la solidaridad eran los valores más importantes para mantener viva la comunidad. Con esfuerzo y dedicación, todos aportaban su granito de arena para construir un futuro mejor para las próximas generaciones."

print(analizar_texto(texto))
