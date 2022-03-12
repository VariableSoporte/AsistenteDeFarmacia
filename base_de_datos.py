import sqlite3
#se genera la receta despues de todos los filtros
def agregar_a_receta(medicinas):
    mi_coneccion = sqlite3.connect("C:/Users/windows/Desktop/python-curse/version_proyecto_v2.0/medicamentos_base_datos.db")
    mi_cursor = mi_coneccion.cursor()
    mi_cursor.execute('select * from Medicamentos')
    lista_que_contiene_base=mi_cursor.fetchall()
    receta_recomendada='>Se recomienda :\n'
    contador=0
    for i in medicinas:
        for lista in lista_que_contiene_base:
            if lista[0]==i:
                receta_recomendada+=f"-{lista[0]}, cada {lista[1]} horas por {lista[2]} día/s\n"
                contador+=1
    mi_coneccion.close()
    #filtro de control de sobremedicacion
    if contador> 4:
        receta_recomendada='>Se recomienda :\nVisitar al medico para revisar su caso en particular\nEn caso de haber ingresado sintomas erroneos\npor favor use el boton de vaciar campos\ny asegurese de ingresar los sintomas\nde una sola persona'

    return receta_recomendada

#obtenermos los medicamentos con los parametros de accion para no sobrerecetar
def buscar_en_base_datos(dato):
    mi_coneccion = sqlite3.connect("C:/Users/windows/Desktop/python-curse/version_proyecto_v2.0/medicamentos_base_datos.db")
    mi_cursor = mi_coneccion.cursor()
    mi_cursor.execute('select * from Medicamentos')
    lista_que_contiene_base = mi_cursor.fetchall()
    recomendaciones=[]
    for i in dato:
        for lista in lista_que_contiene_base:
            if lista[0]==i:
                recomendaciones.append([lista[0],lista[4],lista[3]])

    recomendaciones=filtrar_medicina(recomendaciones)            
    mi_coneccion.close()
    return recomendaciones

#filtramos los medicamentos repetidos
def filtrar_medicina(lista_con_listas):
    lista_filtrada=[]
    lista_cabeza=[]
    lista_analgesico=[]
    lista_estres=[]

    for i in lista_con_listas:
        if i[2]=='Cabeza':
            lista_cabeza.append(i[1])
        elif i[2]=='Analgesico':
            lista_analgesico.append(i[1])
        elif i[2]=='Estres':
            lista_estres.append(i[1])
        else:
            lista_filtrada.append(i[0])
    lista_cabeza.sort(reverse=True)
    lista_analgesico.sort(reverse=True)
    lista_estres.sort(reverse=True)
    for i in lista_con_listas:
        if i[2]=='Cabeza'and i[1]==lista_cabeza[0]:
            lista_filtrada.append(i[0])
        elif i[2]=='Analgesico'and i[1]==lista_analgesico[0]:
            lista_filtrada.append(i[0])     
        elif i[2]=='Estres'and i[1]==lista_estres[0]:
            lista_filtrada.append(i[0])
    return list(set(lista_filtrada))