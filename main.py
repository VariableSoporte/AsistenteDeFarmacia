import ventana
ventana_principal=ventana.Añadir_a_frames()
ventana_principal.crear_un_frame(ventana_principal.ventana,'ivory4',200,500,'left',1)
ventana_principal.crear_un_frame(ventana_principal.ventana,'ivory3',600,500,'right',1)
ventana_principal.crear_scrole()
#ojo con el orden de los frames puesto que cambiarian en la posicion de las listas
ventana_principal.crear_un_frame(ventana_principal.get_numero_frames()[1],'sky blue',200,500,'left',1)
ventana_principal.crear_un_frame(ventana_principal.get_numero_frames()[1],'sky blue',350,500,'right',1)
ventana_principal.mostrar_sintomas()
ventana_principal.mostrar_receta()
ventana_principal.mostrar_ventana()

#refactorizacion