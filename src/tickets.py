import os
import re

def formatear(directorio : str)

    os.chdir(directorio)

    tks = os.listdir()

    regla_de_busqueda = "\#\d{5}"

    for i in tks:
        text = re.findall(regla_de_busqueda,i)
        try:
            os.rename(i, str(text[0]) + ".pdf")
        except:
            pass


