#LOS CONJUNTOS SON TIPOS DE COLECCIONES QUE NO MANTIENEN UN ORDEN. SE CIERRAN EN {}.
#AL NO TENER ORDEN, NO TIENEN ÍNDICES
#NO ALMACENAN ELEMENTOS REPETIDOS.


lista = [1, 5, 9]

#SET EN INGLÉS SIGNIFICA CONJUNTO.
#ES POSIBLE CONVERTIR UNA LISTA EN CONJUNTO DE LA SIGUIENTE FORMA:

conjunto = set(lista)
print(type(conjunto))

#PARA AGREGAR ELEMENTOS A UN CONJUNTO SE UTILIZA:
conjunto.add(10)
#PARA REMOVER ELEMENTOS DE UN CONJUNTO
conjunto.remove(9)

#RECORRER CONJUNTO
for elem in conjunto:
    print(elem)

#ES POSIBLE PREGUNTAR EXISTENCIA DE ELEMENTO DENTRO DEL CONJUNTO
print(5 in conjunto) # EN EL EJEMPLO SE CONSULTA SI EXISTE EL ELEMENTO 5 EN EL CONJUNTO. LA RESPUESTA ES BOOLEANA

conjunto1 = {1, 5, 9}
conjunto2 = {1, 5, 10}

#UNIÓN DE CONJUNTOS
print(conjunto1.union(conjunto2))

#INTERSECCIÓN
print(conjunto1.intersection(conjunto2))


###DICCIONARIOS
#NO SE ALMACENAN VALORES INDIVIDUALES, CADA ELEMENTO ALMACENADO EN UN DICCIONARIO ES UN PAR. UNA CLAVE Y UN VALOR
#EJEMPLOS: {'edad': 19}  {'nombre': 'Marco'}
#PARA ACCEDER A LOS VALORES SE UTILIZAN LAS CLAVES, NO EXISTEN ÍNDICES.

d = {
    'nombre': 'Marco',
    'edad' : 19
}

#PARA OBTENER EL VALOR DE UNA CLAVE LA SINTAXIS ES LA SIGUIENTE:

print(d['edad'])
print(d['nombre'])

#PARA AÑADIR ELEMENTOS A UN DICCIONARIO
d['apellido'] = 'Perez'
print(d)

#PARA ELIMINAR ELEMENTOS DEL DICCIONARIO:
del d['edad']
print(d)

#EDITAR VALORES 
d['edad'] = 20
print(d)

#EDITAR VALORES MEDIANTE OPERACIONES
d['edad'] += 20
print(d)

#RECORRER DICCIONARIO
#PARA RECORRER UN DICCIONARIO HAY QUE DARLE NOMBRE DE VARIABLES A LAS CLAVES (k) Y EL NOMBRE DE VARIABLES
#QUE TOMARÁN LOS VALORES (v).
for k, v in list(d.items()):
    print (k, v)

#CREACIÓN DE ESTRUCTURAS ANIDADAS

e = {
    'nombre':['Hola Mundo', 19],
    'edad':{
        'edad de papá':20, 
        'nombre2': 'Alonso'
    }
}

#PARA ACCEDER A LOS DATOS INTERNOS SE DEBE EJECUTAR DE AFUERA HACIA ADENTRO DE LA SIGUIENTE FORMA:
print(e['nombre'][1])
print(e['edad']['nombre2'])