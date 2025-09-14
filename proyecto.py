{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "607631c9",
   "metadata": {},
   "outputs": [],
   "source": [
    " #EJERCICIO 1\n",
    "def contar_frecuencias(cadena):\n",
    "    dic = {}\n",
    "    for c in cadena:\n",
    "        if c != \" \":\n",
    "            dic[c] = dic.get(c, 0) + 1\n",
    "    return dic\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "e11310a0",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'T': 1, 'e': 1, 'n': 2, 'g': 2, 'o': 2, 'u': 1, 'a': 1, 't': 1}\n"
     ]
    }
   ],
   "source": [
    "print(contar_frecuencias(\"Tengo un gato\"))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c73b0f9a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[2, 4, 6, 8, 10]\n"
     ]
    }
   ],
   "source": [
    "#EJERCICIO 2\n",
    "def duplicar(x):\n",
    "    return x * 2\n",
    "\n",
    "numeros = [1, 2, 3, 4, 5]\n",
    "\n",
    "dobles = list(map(duplicar, numeros))\n",
    "\n",
    "print(dobles)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8ae0c8ad",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['gato', 'tortuga']\n"
     ]
    }
   ],
   "source": [
    "#EJERCICIO 3\n",
    "def buscar_palabras(lista, objetivo):\n",
    "    resultado = []\n",
    "    for palabra in lista:\n",
    "        if objetivo in palabra:\n",
    "            resultado.append(palabra)\n",
    "    return resultado\n",
    "\n",
    "palabras = [\"gato\", \"perro\", \"pajaro\", \"vencejo\", \"golondrina\", \"tortuga\"]\n",
    "objetivo = \"to\"\n",
    "print(buscar_palabras(palabras, objetivo))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "389108d5",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[-1, -1, -4, 11, -28, 28]\n"
     ]
    }
   ],
   "source": [
    "#EJERCICIO 4. DIFERENCIA ENTRE DOS LISTAS\n",
    "lista_numeros = [1,10,14,18,22,42]\n",
    "lista_numeros2 = [2,11,18,7,50,14]\n",
    "\n",
    "def resta(x, y):\n",
    "    return x - y\n",
    "\n",
    "def diferencias(lista_numeros, lista_numeros2):\n",
    "    return list(map(resta, lista_numeros, lista_numeros2))\n",
    "\n",
    "print(diferencias(lista_numeros, lista_numeros2))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e276784c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(5.8, 'aprobado')\n"
     ]
    }
   ],
   "source": [
    "#EJERCICIO 5. MEDIA DE NOTAS Y APROBADO >5\n",
    "notas= [5,7,4,8,5]\n",
    "\n",
    "def evaluar_notas(notas, nota_aprobado=5):\n",
    "    media = sum(notas) / len(notas)\n",
    "    estado = \"aprobado\" if media >= nota_aprobado else \"suspenso\"\n",
    "    return (media, estado)\n",
    "\n",
    "print(evaluar_notas(notas))\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "bb3c636c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "3628800\n"
     ]
    }
   ],
   "source": [
    "#EJERCICIO 5: FACTORIAL DE MANERA RECURSIVA\n",
    "def factorial(n):\n",
    "    if n == 0 or n == 1:\n",
    "        return 1\n",
    "    else:\n",
    "        return n * factorial(n - 1)\n",
    "\n",
    "\n",
    "print(factorial(10))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "83db7fee",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['(1, 2)', '(3, 4)', '(5, 6)']\n"
     ]
    }
   ],
   "source": [
    "#EJERCICIO 6: TUPPLAS A STRING\n",
    "def tuplas_a_strings(lista_tuplas):\n",
    "    return list(map(str, lista_tuplas))\n",
    "\n",
    "lista = [(1, 2), (3, 4), (5, 6)]\n",
    "print(tuplas_a_strings(lista))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1383743a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "24\n"
     ]
    }
   ],
   "source": [
    "#EJERCICIO 7: FACTORIAL\n",
    "def factorial(n):\n",
    "    if n == 0 or n == 1:   \n",
    "        return 1\n",
    "    return n * factorial(n - 1) \n",
    "\n",
    "\n",
    "print(factorial(4))  \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6ca3601b",
   "metadata": {},
   "outputs": [],
   "source": [
    "#EJERCICIO 8: PROGRAMA DOS NUMEROS Y DIVISION DE ESTOS\n",
    "def dividir():\n",
    "    try:\n",
    "        num1 = float(input(\"Introduce el primer número: \"))\n",
    "        num2 = float(input(\"Introduce el segundo número: \"))\n",
    "\n",
    "        resultado = num1 / num2\n",
    "    except ValueError:\n",
    "        print(\"❌ Error: Debes ingresar solo números.\")\n",
    "    except ZeroDivisionError:\n",
    "        print(\"❌ Error: No se puede dividir entre cero.\")\n",
    "    else:\n",
    "        print(f\"✅ División exitosa: {num1} / {num2} = {resultado}\")\n",
    "\n",
    "\n",
    "\n",
    "dividir()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3377ae52",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['Perro', 'Gato', 'Conejo', 'Hámster']\n"
     ]
    }
   ],
   "source": [
    "#EJERCICIO 9: LISTA DE MASCOTAS Y EXCLUIR PROHIBIDAS\n",
    "def es_permitida(mascota):\n",
    "    prohibidas = [\"Mapache\", \"Tigre\", \"Serpiente Pitón\", \"Cocodrilo\", \"Oso\"]\n",
    "    return mascota not in prohibidas\n",
    "\n",
    "def filtrar_mascotas(lista_mascotas):\n",
    "    return list(filter(es_permitida, lista_mascotas))\n",
    "\n",
    "\n",
    "mascotas = [\"Perro\", \"Gato\", \"Tigre\", \"Conejo\", \"Cocodrilo\", \"Hámster\"]\n",
    "print(filtrar_mascotas(mascotas))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "edac6f86",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "✅ El promedio es: 6.25\n"
     ]
    }
   ],
   "source": [
    "#EJERCICIO 10: LISTA NUMEROS Y PROMEDIO\n",
    "class ListaVaciaError(Exception):\n",
    "    pass\n",
    "\n",
    "\n",
    "def calcular_promedio(numeros):\n",
    "    if not numeros: \n",
    "        raise ListaVaciaError(\"La lista de números está vacía.\")\n",
    "    return sum(numeros) / len(numeros)\n",
    "\n",
    "\n",
    "try:\n",
    "    lista = [5, 7, 4, 9]   \n",
    "    promedio = calcular_promedio(lista)\n",
    "    print(f\"✅ El promedio es: {promedio}\")\n",
    "except ListaVaciaError as e:\n",
    "    print(f\"❌ Error: {e}\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3eb39d2a",
   "metadata": {},
   "outputs": [],
   "source": [
    "#EJERCICIO 11: PROGRAMA PARA PEDIR EDAD\n",
    "def pedir_edad():\n",
    "    try:\n",
    "        edad = int(input(\"Introduce tu edad: \"))\n",
    "\n",
    "        if edad < 0 or edad > 120:\n",
    "            raise ValueError(\"La edad debe estar entre 0 y 120.\")\n",
    "\n",
    "    except ValueError as e:\n",
    "        print(f\"❌ Error: {e}\")\n",
    "    else:\n",
    "        print(f\"✅ Edad registrada correctamente: {edad} años\")\n",
    "\n",
    "\n",
    "\n",
    "pedir_edad()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4d58b240",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[3, 5, 3, 11]\n"
     ]
    }
   ],
   "source": [
    "#EJERCICIO 12: LONGITUDES PALABRAS DE UN TEXTO\n",
    "def longitudes_palabras(frase):\n",
    "    palabras = frase.split()\n",
    "    return list(map(len, palabras))\n",
    "\n",
    "\n",
    "\n",
    "texto = \"Los gatos son fantasticos\"\n",
    "print(longitudes_palabras(texto))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "b6a708dc",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[('T', 't'), ('O', 'o'), ('G', 'g'), ('I', 'i'), ('A', 'a')]\n"
     ]
    }
   ],
   "source": [
    "#EJERCICIO 13: LISTA DE TUPLA CON CADA LETRA MAYUS Y MINUS\n",
    "def letras_mayus_minus(conjunto):\n",
    "   \n",
    "    unicas = list(set(conjunto))\n",
    "\n",
    "    return list(map(lambda c: (c.upper(), c.lower()), unicas))\n",
    "\n",
    "\n",
    "caracteres = \"gatito\"\n",
    "print(letras_mayus_minus(caracteres))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "df822296",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['gato', 'golondrina']\n"
     ]
    }
   ],
   "source": [
    "#EJERCICIO 14: BUSCAR POR LETRA OBJETIVO EN LISTA\n",
    "def empieza_con(palabra, letra):\n",
    "    return palabra.startswith(letra)\n",
    "\n",
    "def filtrar_por_letra(palabras, letra):\n",
    " \n",
    "    def aux(palabra):\n",
    "        return empieza_con(palabra, letra)\n",
    "    return list(filter(aux, palabras))\n",
    "\n",
    "\n",
    "\n",
    "lista = [\"gato\", \"perro\", \"pajaro\", \"golondrina\", \"tortuga\"]\n",
    "letra_objetivo = \"g\"\n",
    "print(filtrar_por_letra(lista, letra_objetivo))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "93139fec",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[4, 5, 6, 7, 8]\n"
     ]
    }
   ],
   "source": [
    "#EJERCICIO 15:FUNCIÓN LAMBDA QUE SUME 3\n",
    "\n",
    "numeros= [1, 2, 3, 4, 5]\n",
    "\n",
    "\n",
    "resultado = list(map(lambda x: x + 3, numeros))\n",
    "\n",
    "print(resultado)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "f000368e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['gatos', 'animales', 'curiosos']\n"
     ]
    }
   ],
   "source": [
    "#EJERCICIO 16: FUNCION CADENA DE TEXTO\n",
    "def palabras_mas_largas(cadena, n):\n",
    "    palabras = cadena.split()  \n",
    "    return list(filter(lambda palabra: len(palabra) > n, palabras))\n",
    "\n",
    "\n",
    "\n",
    "texto = \"Los gatos son animales muy curiosos\"\n",
    "n = 4\n",
    "print(palabras_mas_largas(texto, n))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "cf3ab4fb",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "572\n"
     ]
    }
   ],
   "source": [
    "#EJERCICIO 17: FUNCION LISTA DIGITOS\n",
    "from functools import reduce\n",
    "\n",
    "def lista_a_numero(digitos):\n",
    "   \n",
    "    return reduce(lambda acc, d: acc * 10 + d, digitos)\n",
    "\n",
    "\n",
    "\n",
    "digitos = [5, 7, 2]\n",
    "print(lista_a_numero(digitos)) \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "73c3899f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[{'nombre': 'Ana', 'edad': 20, 'calificacion': 95}, {'nombre': 'Marta', 'edad': 21, 'calificacion': 90}, {'nombre': 'Sofía', 'edad': 20, 'calificacion': 92}]\n"
     ]
    }
   ],
   "source": [
    "#Ejercicio 18: Lista de estudiantes\n",
    "estudiantes = [\n",
    "    {\"nombre\": \"Ana\", \"edad\": 20, \"calificacion\": 95},\n",
    "    {\"nombre\": \"Luis\", \"edad\": 22, \"calificacion\": 85},\n",
    "    {\"nombre\": \"Marta\", \"edad\": 21, \"calificacion\": 90},\n",
    "    {\"nombre\": \"Pedro\", \"edad\": 23, \"calificacion\": 78},\n",
    "    {\"nombre\": \"Sofía\", \"edad\": 20, \"calificacion\": 92}\n",
    "]\n",
    "\n",
    "def es_excelente(estudiante):\n",
    "    return estudiante[\"calificacion\"] >= 90\n",
    "\n",
    "\n",
    "aprobados = list(filter(es_excelente, estudiantes))\n",
    "\n",
    "\n",
    "print(aprobados)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "e46ceb7f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1, 3, 5, 7, 9]\n"
     ]
    }
   ],
   "source": [
    "#Ejercicio 19: función lambda y filtrar por impares\n",
    "numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]\n",
    "\n",
    "impares = list(filter(lambda x: x % 2 != 0, numeros))\n",
    "\n",
    "print(impares)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "1abb831e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1, 3, 7, 10]\n"
     ]
    }
   ],
   "source": [
    "#Ejercicio 20: lista int\n",
    "\n",
    "valores = [1, \"hola\", 3, \"python\", 7, \"42\", 10]\n",
    "\n",
    "\n",
    "def es_entero(x):\n",
    "    return isinstance(x, int)\n",
    "\n",
    "solo_enteros = list(filter(es_entero, valores))\n",
    "\n",
    "print(solo_enteros)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "ecae168e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "27\n",
      "125\n"
     ]
    }
   ],
   "source": [
    "#Ejercicio 21: cubo de un numero con lambda\n",
    "\n",
    "cubo = lambda x: x ** 3\n",
    "\n",
    "\n",
    "print(cubo(3))  \n",
    "print(cubo(5))  \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "5ff4b628",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "120\n"
     ]
    }
   ],
   "source": [
    "#ejercicio 22: producto total de una lista usando reduce\n",
    "\n",
    "from functools import reduce\n",
    "\n",
    "\n",
    "numeros = [2, 3, 4, 5]\n",
    "\n",
    "\n",
    "producto_total = reduce(lambda x, y: x * y, numeros)\n",
    "\n",
    "print(producto_total)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "bda83898",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Hola a todos\n"
     ]
    }
   ],
   "source": [
    "#ejercicio 23: concatena lista de palabras usando reduce\n",
    "\n",
    "from functools import reduce\n",
    "\n",
    "\n",
    "palabras = [\"Hola\", \"a\", \"todos\"]\n",
    "\n",
    "frase = reduce(lambda a, b: a + \" \" + b, palabras)\n",
    "\n",
    "print(frase)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "7ec76c6c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "65\n"
     ]
    }
   ],
   "source": [
    "#ejercicio 24: diferencia de una lista usando reduce\n",
    "\n",
    "from functools import reduce\n",
    "\n",
    "\n",
    "numeros = [100, 20, 5, 10]\n",
    "\n",
    "\n",
    "diferencia_total = reduce(lambda x, y: x - y, numeros)\n",
    "\n",
    "print(diferencia_total)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "17e8a4af",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "12\n"
     ]
    }
   ],
   "source": [
    "#ejercicio 25: contar los carácteres en una cadena\n",
    "\n",
    "def contar_caracteres(texto):\n",
    "    return len(texto)\n",
    "\n",
    "\n",
    "\n",
    "cadena = \"Hola a todos\"\n",
    "print(contar_caracteres(cadena))  \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "5ad66a44",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1\n",
      "4\n"
     ]
    }
   ],
   "source": [
    "#Ejercicio 26: funcion lambda que calcule el resto de una division\n",
    "resto = lambda a, b: a % b\n",
    "\n",
    "\n",
    "print(resto(10, 3))  \n",
    "print(resto(25, 7))  \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f15d34c1",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "7.333333333333333\n"
     ]
    }
   ],
   "source": [
    "# Ejercicio 27: Función que calcule el promedio de una lista de números\n",
    "def promedio(lista):\n",
    "    \"\"\"Calcula el promedio de una lista de números.\"\"\"\n",
    "    if not lista:  \n",
    "        return 0\n",
    "    return sum(lista) / len(lista)\n",
    "\n",
    "\n",
    "numeros = [5, 7, 10]\n",
    "print(promedio(numeros)) \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "4b2a7ee9",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Ejercicio 28: Función que devuelva el primer elemento duplicado en una lista\n",
    "def primer_duplicado(lista):\n",
    "    vistos = set()\n",
    "    for elem in lista:\n",
    "        if elem in vistos:\n",
    "            return elem\n",
    "        vistos.add(elem)\n",
    "    return None"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "8307982a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "3\n"
     ]
    }
   ],
   "source": [
    "# Ejercicio 28: Función que busque y devuelva el primer elemento duplicado en una lista\n",
    "def primer_duplicado(lista):\n",
    "    vistos = set()\n",
    "    for elem in lista:\n",
    "        if elem in vistos:\n",
    "            return elem\n",
    "        vistos.add(elem)\n",
    "    return None\n",
    "\n",
    "\n",
    "lista = [1, 3, 2, 3, 4]\n",
    "print(primer_duplicado(lista))  \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "13653733",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "#####6789\n"
     ]
    }
   ],
   "source": [
    "#Ejercicio 29: Funcion que enmascare todos los caracteres de una variable excepto los últimos cuatro\n",
    "def enmascarar(valor):\n",
    "    \n",
    "    s = str(valor)\n",
    "    if len(s) <= 4:\n",
    "        return s\n",
    "    return \"#\" * (len(s) - 4) + s[-4:]\n",
    "\n",
    "#\n",
    "dato = \"123456789\"\n",
    "print(enmascarar(dato))  \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "99b160e9",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "True\n",
      "False\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "True\n",
      "False\n"
     ]
    }
   ],
   "source": [
    "# ejercicio 30: determina si dos palabras son anagramas\n",
    "def son_anagramas(palabra1, palabra2):\n",
    "    \"\"\"Devuelve True si las dos palabras son anagramas, False en caso contrario.\"\"\"\n",
    "    return sorted(palabra1.lower()) == sorted(palabra2.lower())\n",
    "\n",
    "\n",
    "print(son_anagramas(\"Roma\", \"Amor\"))   \n",
    "print(son_anagramas(\"Hola\", \"Mundo\"))  \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "id": "a58a649f",
   "metadata": {},
   "outputs": [
    {
     "ename": "KeyboardInterrupt",
     "evalue": "Interrupted by user",
     "output_type": "error",
     "traceback": [
      "\u001b[31m---------------------------------------------------------------------------\u001b[39m",
      "\u001b[31mKeyboardInterrupt\u001b[39m                         Traceback (most recent call last)",
      "\u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[42]\u001b[39m\u001b[32m, line 16\u001b[39m\n\u001b[32m     14\u001b[39m \u001b[38;5;66;03m# Ejemplo de uso\u001b[39;00m\n\u001b[32m     15\u001b[39m \u001b[38;5;28;01mtry\u001b[39;00m:\n\u001b[32m---> \u001b[39m\u001b[32m16\u001b[39m     \u001b[43mbuscar_nombre\u001b[49m\u001b[43m(\u001b[49m\u001b[43m)\u001b[49m\n\u001b[32m     17\u001b[39m \u001b[38;5;28;01mexcept\u001b[39;00m \u001b[38;5;167;01mValueError\u001b[39;00m \u001b[38;5;28;01mas\u001b[39;00m e:\n\u001b[32m     18\u001b[39m     \u001b[38;5;28mprint\u001b[39m(e)\n",
      "\u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[42]\u001b[39m\u001b[32m, line 5\u001b[39m, in \u001b[36mbuscar_nombre\u001b[39m\u001b[34m()\u001b[39m\n\u001b[32m      2\u001b[39m \u001b[38;5;28;01mdef\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[34mbuscar_nombre\u001b[39m():\n\u001b[32m----> \u001b[39m\u001b[32m5\u001b[39m     nombres = \u001b[38;5;28;43minput\u001b[39;49m\u001b[43m(\u001b[49m\u001b[33;43m\"\u001b[39;49m\u001b[33;43mIntroduce una lista de nombres separados por comas: \u001b[39;49m\u001b[33;43m\"\u001b[39;49m\u001b[43m)\u001b[49m.split(\u001b[33m\"\u001b[39m\u001b[33m,\u001b[39m\u001b[33m\"\u001b[39m)\n\u001b[32m      6\u001b[39m     nombres = [n.strip() \u001b[38;5;28;01mfor\u001b[39;00m n \u001b[38;5;129;01min\u001b[39;00m nombres]  \n\u001b[32m      7\u001b[39m     nombre_buscar = \u001b[38;5;28minput\u001b[39m(\u001b[33m\"\u001b[39m\u001b[33mIntroduce el nombre a buscar: \u001b[39m\u001b[33m\"\u001b[39m).strip()\n",
      "\u001b[36mFile \u001b[39m\u001b[32m~\\AppData\\Local\\Packages\\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\\LocalCache\\local-packages\\Python311\\site-packages\\ipykernel\\kernelbase.py:1275\u001b[39m, in \u001b[36mKernel.raw_input\u001b[39m\u001b[34m(self, prompt)\u001b[39m\n\u001b[32m   1273\u001b[39m     msg = \u001b[33m\"\u001b[39m\u001b[33mraw_input was called, but this frontend does not support input requests.\u001b[39m\u001b[33m\"\u001b[39m\n\u001b[32m   1274\u001b[39m     \u001b[38;5;28;01mraise\u001b[39;00m StdinNotImplementedError(msg)\n\u001b[32m-> \u001b[39m\u001b[32m1275\u001b[39m \u001b[38;5;28;01mreturn\u001b[39;00m \u001b[38;5;28;43mself\u001b[39;49m\u001b[43m.\u001b[49m\u001b[43m_input_request\u001b[49m\u001b[43m(\u001b[49m\n\u001b[32m   1276\u001b[39m \u001b[43m    \u001b[49m\u001b[38;5;28;43mstr\u001b[39;49m\u001b[43m(\u001b[49m\u001b[43mprompt\u001b[49m\u001b[43m)\u001b[49m\u001b[43m,\u001b[49m\n\u001b[32m   1277\u001b[39m \u001b[43m    \u001b[49m\u001b[38;5;28;43mself\u001b[39;49m\u001b[43m.\u001b[49m\u001b[43m_parent_ident\u001b[49m\u001b[43m[\u001b[49m\u001b[33;43m\"\u001b[39;49m\u001b[33;43mshell\u001b[39;49m\u001b[33;43m\"\u001b[39;49m\u001b[43m]\u001b[49m\u001b[43m,\u001b[49m\n\u001b[32m   1278\u001b[39m \u001b[43m    \u001b[49m\u001b[38;5;28;43mself\u001b[39;49m\u001b[43m.\u001b[49m\u001b[43mget_parent\u001b[49m\u001b[43m(\u001b[49m\u001b[33;43m\"\u001b[39;49m\u001b[33;43mshell\u001b[39;49m\u001b[33;43m\"\u001b[39;49m\u001b[43m)\u001b[49m\u001b[43m,\u001b[49m\n\u001b[32m   1279\u001b[39m \u001b[43m    \u001b[49m\u001b[43mpassword\u001b[49m\u001b[43m=\u001b[49m\u001b[38;5;28;43;01mFalse\u001b[39;49;00m\u001b[43m,\u001b[49m\n\u001b[32m   1280\u001b[39m \u001b[43m\u001b[49m\u001b[43m)\u001b[49m\n",
      "\u001b[36mFile \u001b[39m\u001b[32m~\\AppData\\Local\\Packages\\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\\LocalCache\\local-packages\\Python311\\site-packages\\ipykernel\\kernelbase.py:1320\u001b[39m, in \u001b[36mKernel._input_request\u001b[39m\u001b[34m(self, prompt, ident, parent, password)\u001b[39m\n\u001b[32m   1317\u001b[39m \u001b[38;5;28;01mexcept\u001b[39;00m \u001b[38;5;167;01mKeyboardInterrupt\u001b[39;00m:\n\u001b[32m   1318\u001b[39m     \u001b[38;5;66;03m# re-raise KeyboardInterrupt, to truncate traceback\u001b[39;00m\n\u001b[32m   1319\u001b[39m     msg = \u001b[33m\"\u001b[39m\u001b[33mInterrupted by user\u001b[39m\u001b[33m\"\u001b[39m\n\u001b[32m-> \u001b[39m\u001b[32m1320\u001b[39m     \u001b[38;5;28;01mraise\u001b[39;00m \u001b[38;5;167;01mKeyboardInterrupt\u001b[39;00m(msg) \u001b[38;5;28;01mfrom\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[38;5;28;01mNone\u001b[39;00m\n\u001b[32m   1321\u001b[39m \u001b[38;5;28;01mexcept\u001b[39;00m \u001b[38;5;167;01mException\u001b[39;00m:\n\u001b[32m   1322\u001b[39m     \u001b[38;5;28mself\u001b[39m.log.warning(\u001b[33m\"\u001b[39m\u001b[33mInvalid Message:\u001b[39m\u001b[33m\"\u001b[39m, exc_info=\u001b[38;5;28;01mTrue\u001b[39;00m)\n",
      "\u001b[31mKeyboardInterrupt\u001b[39m: Interrupted by user"
     ]
    }
   ],
   "source": [
    "# Ejercicio 31: Buscar un nombre en una lista ingresada por el usuario\n",
    "def buscar_nombre():\n",
    "\n",
    "    \n",
    "    nombres = input(\"Introduce una lista de nombres separados por comas: \").split(\",\")\n",
    "    nombres = [n.strip() for n in nombres]  \n",
    "    nombre_buscar = input(\"Introduce el nombre a buscar: \").strip()\n",
    "    \n",
    "    if nombre_buscar in nombres:\n",
    "        print(f\"{nombre_buscar} fue encontrado.\")\n",
    "    else:\n",
    "        raise ValueError(f\"{nombre_buscar} no está en la lista.\")\n",
    "\n",
    "# Ejemplo de uso\n",
    "try:\n",
    "    buscar_nombre()\n",
    "except ValueError as e:\n",
    "    print(e)\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "acc8ab8f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Analista\n",
      "Carlos Ruiz no trabaja aquí.\n"
     ]
    }
   ],
   "source": [
    "#Ejercicio 32: nombre lista de empleados. Si te lo encuentra, te dice el puesto de trabajo y si no lanza una excepción\n",
    "def obtener_puesto(nombre, empleados):\n",
    "    for emp in empleados:\n",
    "        if emp[\"nombre\"] == nombre:\n",
    "            return emp[\"puesto\"]\n",
    "    return f\"{nombre} no trabaja aquí.\"\n",
    "\n",
    "\n",
    "empleados = [\n",
    "    {\"nombre\": \"Ana Pérez\", \"puesto\": \"Gerente\"},\n",
    "    {\"nombre\": \"Luis Gómez\", \"puesto\": \"Analista\"},\n",
    "    {\"nombre\": \"Marta López\", \"puesto\": \"Diseñadora\"}\n",
    "]\n",
    "\n",
    "print(obtener_puesto(\"Luis Gómez\", empleados))    \n",
    "print(obtener_puesto(\"Carlos Ruiz\", empleados))   \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "id": "99a5fbe9",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[11, 22, 33, 44]\n"
     ]
    }
   ],
   "source": [
    "# Ejercicio 33: Función lambda que sume elementos correspondientes de dos listas\n",
    "lista1 = [1, 2, 3, 4]\n",
    "lista2 = [10, 20, 30, 40]\n",
    "\n",
    "sumar_listas = lambda l1, l2: list(map(lambda x, y: x + y, l1, l2))\n",
    "\n",
    "\n",
    "resultado = sumar_listas(lista1, lista2)\n",
    "print(resultado) \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "88c34c09",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'longitud_tronco': 2, 'numero_ramas': 2, 'longitudes_ramas': [2, 1]}\n"
     ]
    }
   ],
   "source": [
    "#Ejercicio 34: Clase Arbol con tronco y ramas\n",
    "\n",
    "class Arbol:\n",
    "    def __init__(self):\n",
    "        self.tronco = 1\n",
    "        self.ramas = []\n",
    "\n",
    "    def crecer_tronco(self):\n",
    "        self.tronco += 1\n",
    "\n",
    "    def nueva_rama(self):\n",
    "        self.ramas.append(1)\n",
    "\n",
    "    def crecer_ramas(self):\n",
    "        self.ramas = [rama + 1 for rama in self.ramas]\n",
    "\n",
    "    def quitar_rama(self, posicion):\n",
    "        if 0 <= posicion < len(self.ramas):\n",
    "            self.ramas.pop(posicion)\n",
    "        else:\n",
    "            print(\"Posición inválida. No se pudo quitar la rama.\")\n",
    "\n",
    "    def info_arbol(self):\n",
    "        return {\n",
    "            \"longitud_tronco\": self.tronco,\n",
    "            \"numero_ramas\": len(self.ramas),\n",
    "            \"longitudes_ramas\": self.ramas\n",
    "        }\n",
    "\n",
    "# Caso de uso:\n",
    "arbol = Arbol()                \n",
    "arbol.crecer_tronco()          \n",
    "arbol.nueva_rama()             \n",
    "arbol.crecer_ramas()           \n",
    "arbol.nueva_rama()             \n",
    "arbol.nueva_rama()             \n",
    "arbol.quitar_rama(2)          \n",
    "print(arbol.info_arbol())      \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d2fd466a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Bob agregó 20. Saldo actual: 70\n",
      "Bob transfirió 30 a Alicia.\n",
      "Saldos -> Bob: 40, Alicia: 130\n",
      "Alicia retiró 50. Saldo actual: 80\n"
     ]
    }
   ],
   "source": [
    "# Ejercicio 35: Clase UsuarioBanco\n",
    "\n",
    "class UsuarioBanco:\n",
    "    def __init__(self, nombre, saldo, cuenta_corriente=True):\n",
    "        self.nombre = nombre\n",
    "        self.saldo = saldo\n",
    "        self.cuenta_corriente = cuenta_corriente\n",
    "\n",
    "    def retirar_dinero(self, cantidad):\n",
    "        if not self.cuenta_corriente:\n",
    "            raise ValueError(f\"{self.nombre} no tiene cuenta corriente.\")\n",
    "        if cantidad > self.saldo:\n",
    "            raise ValueError(f\"{self.nombre} no tiene suficiente saldo para retirar {cantidad}.\")\n",
    "        self.saldo -= cantidad\n",
    "        print(f\"{self.nombre} retiró {cantidad}. Saldo actual: {self.saldo}\")\n",
    "\n",
    "    def transferir_dinero(self, destino, cantidad):\n",
    "        if not self.cuenta_corriente or not destino.cuenta_corriente:\n",
    "            raise ValueError(\"Ambos usuarios deben tener cuenta corriente para transferir.\")\n",
    "        if cantidad > self.saldo:\n",
    "            raise ValueError(f\"{self.nombre} no tiene suficiente saldo para transferir {cantidad}.\")\n",
    "        self.saldo -= cantidad\n",
    "        destino.saldo += cantidad\n",
    "        print(f\"{self.nombre} transfirió {cantidad} a {destino.nombre}.\")\n",
    "        print(f\"Saldos -> {self.nombre}: {self.saldo}, {destino.nombre}: {destino.saldo}\")\n",
    "\n",
    "    def agregar_dinero(self, cantidad):\n",
    "        if not self.cuenta_corriente:\n",
    "            raise ValueError(f\"{self.nombre} no tiene cuenta corriente.\")\n",
    "        self.saldo += cantidad\n",
    "        print(f\"{self.nombre} agregó {cantidad}. Saldo actual: {self.saldo}\")\n",
    "\n",
    "\n",
    "# ejemplo\n",
    "alicia = UsuarioBanco(\"Alicia\", 100, True)\n",
    "bob = UsuarioBanco(\"Bob\", 50, True)\n",
    "\n",
    "bob.agregar_dinero(20)            \n",
    "bob.transferir_dinero(alicia, 30)\n",
    "alicia.retirar_dinero(50)         \n",
    "\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "266be5d0",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "➡ Contar palabras:\n",
      "{'hola': 3, 'mundo': 2, 'python': 1}\n",
      "\n",
      "➡ Reemplazar 'hola' por 'hi':\n",
      "hi mundo hi python mundo hi\n",
      "\n",
      "➡ Eliminar 'mundo':\n",
      "hola hola python hola\n"
     ]
    }
   ],
   "source": [
    "# ejercicio 36: funcion procesar texto y contar palabras.\n",
    "#contar palabras\n",
    "def contar_palabras(texto):\n",
    "    palabras = texto.split()\n",
    "    contador = {}\n",
    "    for palabra in palabras:\n",
    "        palabra = palabra.lower()\n",
    "        contador[palabra] = contador.get(palabra, 0) + 1\n",
    "    return contador\n",
    "\n",
    "# Reemplazar palabras\n",
    "def reemplazar_palabras(texto, palabra_original, palabra_nueva):\n",
    "    return texto.replace(palabra_original, palabra_nueva)\n",
    "\n",
    "# Eliminar palabra\n",
    "def eliminar_palabra(texto, palabra_a_eliminar):\n",
    "    palabras = texto.split()\n",
    "    palabras_filtradas = [p for p in palabras if p != palabra_a_eliminar]\n",
    "    return \" \".join(palabras_filtradas)\n",
    "\n",
    "#procesar_texto\n",
    "def procesar_texto(texto, opcion, *args):\n",
    "    if opcion == \"contar\":\n",
    "        return contar_palabras(texto)\n",
    "    elif opcion == \"reemplazar\":\n",
    "        if len(args) != 2:\n",
    "            raise ValueError(\"Para 'reemplazar' debes pasar palabra_original y palabra_nueva.\")\n",
    "        return reemplazar_palabras(texto, args[0], args[1])\n",
    "    elif opcion == \"eliminar\":\n",
    "        if len(args) != 1:\n",
    "            raise ValueError(\"Para 'eliminar' debes pasar una palabra a eliminar.\")\n",
    "        return eliminar_palabra(texto, args[0])\n",
    "    else:\n",
    "        raise ValueError(\"Opción no válida. Usa: 'contar', 'reemplazar' o 'eliminar'.\")\n",
    "\n",
    "\n",
    "# ejemplo\n",
    "texto = \"hola mundo hola python mundo hola\"\n",
    "\n",
    "print(\"➡ Contar palabras:\")\n",
    "print(procesar_texto(texto, \"contar\"))\n",
    "\n",
    "print(\"\\n➡ Reemplazar 'hola' por 'hi':\")\n",
    "print(procesar_texto(texto, \"reemplazar\", \"hola\", \"hi\"))\n",
    "\n",
    "print(\"\\n➡ Eliminar 'mundo':\")\n",
    "print(procesar_texto(texto, \"eliminar\", \"mundo\"))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e3b999b2",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Ejercicio 37: programa momento del dia\n",
    "def momento_del_dia():\n",
    "    try:\n",
    "        hora = int(input(\"Introduce la hora en formato 24h (0-23): \"))\n",
    "        if hora < 0 or hora > 23:\n",
    "            print(\"La hora debe estar entre 0 y 23.\")\n",
    "        elif 6 <= hora < 12:\n",
    "            print(\"Es de día (mañana).\")\n",
    "        elif 12 <= hora < 20:\n",
    "            print(\"Es de tarde.\")\n",
    "        else:\n",
    "            print(\"Es de noche.\")\n",
    "    except ValueError:\n",
    "        print(\"Por favor, introduce un número válido.\")\n",
    "\n",
    "#ejemplo uso\n",
    "momento_del_dia()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9c7a1a4c",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Ejercicio 38: programa calificaciones\n",
    "def calificacion_en_texto(calificacion):\n",
    "    if 0 <= calificacion <= 69:\n",
    "        return \"insuficiente\"\n",
    "    elif 70 <= calificacion <= 79:\n",
    "        return \"bien\"\n",
    "    elif 80 <= calificacion <= 89:\n",
    "        return \"muy bien\"\n",
    "    elif 90 <= calificacion <= 100:\n",
    "        return \"excelente\"\n",
    "    else:\n",
    "        return \"calificación fuera de rango\"\n",
    "\n",
    "\n",
    "# Ejemplo de uso\n",
    "nota = int(input(\"Introduce la calificación numérica (0-100): \"))\n",
    "print(f\"Tu calificación es: {calificacion_en_texto(nota)}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "7be397ec",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Área triángulo: 25.0\n",
      "Área rectángulo: 32\n",
      "Área círculo: 28.274333882308138\n"
     ]
    }
   ],
   "source": [
    "#ejercicio 39: función parámetro figura y datos\n",
    "import math\n",
    "\n",
    "def calcular_area(figura, datos):\n",
    "    \"\"\"\n",
    "    Calcula el área de una figura:\n",
    "    - 'triangulo': datos = (base, altura)\n",
    "    - 'rectangulo': datos = (base, altura)\n",
    "    - 'circulo': datos = (radio,)\n",
    "    \"\"\"\n",
    "    figura = figura.lower()\n",
    "    \n",
    "    if figura == \"triangulo\":\n",
    "        if len(datos) != 2:\n",
    "            raise ValueError(\"Para un triángulo se necesitan dos valores: (base, altura)\")\n",
    "        base, altura = datos\n",
    "        return (base * altura) / 2\n",
    "    \n",
    "    elif figura == \"rectangulo\":\n",
    "        if len(datos) != 2:\n",
    "            raise ValueError(\"Para un rectángulo se necesitan dos valores: (base, altura)\")\n",
    "        base, altura = datos\n",
    "        return base * altura\n",
    "    \n",
    "    elif figura == \"circulo\":\n",
    "        if len(datos) != 1:\n",
    "            raise ValueError(\"Para un círculo se necesita un valor: (radio,)\")\n",
    "        (radio,) = datos\n",
    "        return math.pi * radio ** 2\n",
    "    \n",
    "    else:\n",
    "        raise ValueError(\"Figura no válida. Usa 'triangulo', 'rectangulo' o 'circulo'.\")\n",
    "\n",
    "# Ejemplos\n",
    "print(\"Área triángulo:\", calcular_area(\"triangulo\", (5, 10)))   # 25.0\n",
    "print(\"Área rectángulo:\", calcular_area(\"rectangulo\", (4, 8)))  # 32\n",
    "print(\"Área círculo:\", calcular_area(\"circulo\", (3,)))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a9fbeef9",
   "metadata": {},
   "outputs": [],
   "source": [
    "# ejercicio 40: rograma para calcular el precio final con posible descuento\n",
    "\n",
    "try:\n",
    "    # 1. Solicitar el precio original\n",
    "    precio_original = float(input(\"Introduce el precio original del artículo: \"))\n",
    "\n",
    "    # 2. Preguntar si tiene cupón\n",
    "    tiene_cupon = input(\"¿Tienes un cupón de descuento? (sí/no): \").strip().lower()\n",
    "\n",
    "    if tiene_cupon == \"sí\" or tiene_cupon == \"si\":\n",
    "        # 3. Solicitar valor del cupón\n",
    "        descuento = float(input(\"Introduce el valor del cupón de descuento: \"))\n",
    "        if descuento > 0:\n",
    "            precio_final = precio_original - descuento\n",
    "            if precio_final < 0:\n",
    "                precio_final = 0  # Evitar precio negativo\n",
    "            print(f\"El precio final después del descuento es: {precio_final:.2f} €\")\n",
    "        else:\n",
    "            print(\"El valor del cupón no es válido. No se aplicará descuento.\")\n",
    "            print(f\"Precio final: {precio_original:.2f} €\")\n",
    "    elif tiene_cupon == \"no\":\n",
    "        # Sin descuento\n",
    "        print(f\"No se aplicó descuento. Precio final: {precio_original:.2f} €\")\n",
    "    else:\n",
    "        print(\"Respuesta no válida. Ingresa 'sí' o 'no'.\")\n",
    "except ValueError:\n",
    "    print(\"Por favor, introduce un número válido para el precio o el descuento.\")\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
