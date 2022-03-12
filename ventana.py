from tkinter import *
from tkinter import ttk
import enfermedades
import base_de_datos

#crear ventana principal
class Ventana:
    def __init__(self):
        self.__dimension='800x500'
        self.__color_fondo='ivory3'
        self.__titulo_aplicacion='Asistente de Farmacia'
        #self.__icono='version_proyecto_v2.0/medicina.ico'     #ojo con la direccion del icono
        self.ventana=Tk()
    def get_dimension(self):
        return self.__dimension
    def get_color_fondo(self):
        return self.__color_fondo
    def get_titulo_aplicacion(self):
        return self.__titulo_aplicacion
    #def get_icono(self):
    #    return self.__icono

#muestra la ventana
    def mostrar_ventana(self):
        self.ventana.title(self.get_titulo_aplicacion())
        self.ventana.config(bg=self.get_color_fondo())
        #self.ventana.iconbitmap(self.get_icono())
        self.ventana.geometry(self.get_dimension())
        self.ventana.resizable(width=False, height=False)       #permite dimensionar la ventana
        self.ventana.mainloop() 

#Dividimos la ventana en las partes necesarias para trabajar en ellas
class Frames(Ventana):
    def __init__(self):
        super().__init__()
        self.__numero_frames=[]

    def get_numero_frames(self):
        return self.__numero_frames
    def set_numero_frames(self,valor):
        self.__numero_frames.append(valor)

#Creamos y ubicamos el frame dentro de la ventana
    def crear_un_frame (self,lugar,baground,ancho,largo,donde_ubicar):
        espacio=LabelFrame(lugar,bg=baground,width=ancho,height=largo)
        espacio.pack(side=donde_ubicar,padx=5,pady=5)
        self.set_numero_frames(espacio)

#todos los componentes que van dentro de la ventana
class Añadir_a_frames(Frames,enfermedades.Enfermedades_concretas):
    def __init__(self):
        Frames.__init__(self)
        enfermedades.Enfermedades_concretas.__init__(self)
        self.__lista_labels=[]
        self.__lista_listas=[]
        self.__sintomas=[]
        self.__lista_medicamentos=[]
        

    def get_lista_labels(self):
        return self.__lista_labels
    def set_lista_labels(self,valor):
        self.__lista_labels.append(valor)
    def get_lista_listas(self):
        return self.__lista_listas
    def set_lista_listas(self,valor):
        self.__lista_listas.append(valor)
    def get_lista_medicamentos(self):
        return self.__lista_medicamentos
    def set_lista_medicamentos(self,valor):
        self.__lista_medicamentos=valor
    def get_sintomas(self):
        return self.__sintomas
    def set_sintomas(self,valor):
        try:
            self.__sintomas.remove(valor)
        except:
            self.__sintomas.append(valor)
    def crear_un_frame(self,lugar,color,ancho,largo,donde_ubicar=0,opcion=0):
        if opcion==0:
            nuevo_frame=Frame(lugar)
            nuevo_frame.config(width=largo,height=ancho,bg=color)
            self.set_numero_frames(nuevo_frame)
        else:
            super().crear_un_frame(lugar,color,ancho,largo,donde_ubicar)

#scrole del frame izquierdo utilizando canvas        
    def crear_scrole(self):
        crear_canvas = Canvas (self.get_numero_frames()[0],width=200,height=500)
        crear_canvas.pack(side=LEFT)#importante el canvas lado izquierdo

        yscrollbar = Scrollbar (self.get_numero_frames()[0],orient='vertical',command=crear_canvas.yview)
        yscrollbar.pack(side=RIGHT,fill="y")

        crear_canvas.configure(yscrollcommand=yscrollbar.set)
        crear_canvas.bind('<Configure>',lambda e: crear_canvas.configure(scrollregion = crear_canvas.bbox('all')))
        #lamba funcion de tipo anonimo, solo con pequeñas funciones
#el nuevo frame es donde se trabajara para que entre al canvas
#de esta forma funcionara el scroll para todo el canvas
        self.crear_un_frame(crear_canvas,'black',500,200) #el bg en negro se utiliza para verificar espacios en blanco
        crear_canvas.create_window((100,0),window=self.get_numero_frames()[2],anchor='n')
        self.llenar_frame_izquierdo()

#se crean todos los elementos izquierdos        
    def llenar_frame_izquierdo(self):
        Label(self.get_numero_frames()[2],text='Listado de sintomas',anchor='w',width=28).pack(fill='x')
        self.set_lista_labels(Label(self.get_numero_frames()[2],text='   >Enfermedades concretas',anchor='w').pack(fill='x'))
        lista=Listbox(self.get_numero_frames()[2])
        self.crear_lista(lista,self.get_diccionario_enfermedad())
        self.set_lista_labels(Label(self.get_numero_frames()[2],text='   >Lugar de Molestia',anchor='w').pack(fill='x'))
        self.crear_lista_modificada(self.get_diccionario_dolores())

#lista del primer frame, es especial por que viene de un diccionario aparte        
    def crear_lista (self,listbox,donde_analizo):
        for key in donde_analizo:
            listbox.insert(END,key)
        listbox.config(width=33,height=3)
        listbox.bind('<Double-Button>',self.capturar)
        listbox.pack()
        self.set_lista_listas(listbox)

#Se crea los label y las listas del segundo diccionario
    def crear_lista_modificada (self,donde_analizo):
        cuenta=1
        for key in donde_analizo:
            lista=Listbox(self.get_numero_frames()[2])
            self.set_lista_labels(Label(self.get_numero_frames()[2],text=f'      >{key}',anchor='w').pack(fill='x'))
            cuenta+=1
            
            diccionario=donde_analizo[key]
            for key_dos in diccionario:
                lista.insert(END,key_dos)
                lista.config(width=33,height=3)
            lista.bind('<Double-Button>',self.capturar)
            lista.pack()
            self.set_lista_listas(lista)
        
    #def ocultar_listas(self,numero):
        #print(self.lista_listas[numero])
        #if self.contador[numero]%2==0:
        #    self.lista_listas[numero].pack_forget()
        #    self.contador[numero]+=1
            
        #else:

        #    print('ho')
        #    self.lista_listas[numero].config(width=33,height=3)
        #    self.lista_listas[numero].pack()
        #    print('la')
            #self.lista_listas[numero].pack()
        #    print('lo')
        #    self.contador[numero]+=1    
        #    print('l')


    #captura los doble clic dentro de cualquier lista para trabajar con sus datos        
    def capturar (self,event):
        variable_soporte=event.widget
        variable_soporte_dos=variable_soporte.curselection()
        variable_soporte_tres=variable_soporte.get(variable_soporte_dos[0])
        self.set_sintomas(variable_soporte_tres)
        self.listado_sintomas()

    def mostrar_sintomas(self):
        Label(self.get_numero_frames()[3],text=' > Listado de sintomas:',anchor='w',width=30).pack(side='top',fill='x')    #,width=33,height=33,anchor='nw'
        self.crear_un_frame(self.get_numero_frames()[3],'ivory3',400,210)   #frame donde se ubicara los sintomas
        self.get_numero_frames()[5].pack(fill='x')
        Button(self.get_numero_frames()[3],text='Hacer Receta',width=30,command=self.hacer_receta).pack(side='bottom') #boton de la receta
    
    def listado_sintomas(self):
        listado_de_los_sintomas=''
        for i in self.get_sintomas():
            listado_de_los_sintomas+=(i.ljust(80,' '))+'\n'
        if listado_de_los_sintomas=='':
            listado_de_los_sintomas='                                                                              '
            self.label_especial=Label(self.get_numero_frames()[5],text=listado_de_los_sintomas,bg='ivory3')
        else:
            self.label_especial=Label(self.get_numero_frames()[5],text=listado_de_los_sintomas,bg='ivory3',justify='left')
        self.label_especial.place(x=0,y=0)  #.place(porque no redimensiona el frame)

    #Distinge los medicamentos que se daran al paciente    
    def hacer_receta (self):
        Label(self.get_numero_frames()[7],bg='ivory3',width = 500, height = 500).place(x=0,y=0)
        self.set_lista_medicamentos(self.imprime(self.get_sintomas()))
        self.receta_medica=base_de_datos.buscar_en_base_datos(self.get_lista_medicamentos())
        self.receta_medica=base_de_datos.agregar_a_receta(self.receta_medica)
        self.dar_las_indicaciones()
    def vaciar_campos(self):
        eliminar=self.get_sintomas().copy() #el copy es importante por que sino elimina la lista por saltos
        for i in eliminar:
            self.set_sintomas(i)
            self.listado_sintomas()
        self.set_lista_medicamentos('')
        Label(self.get_numero_frames()[7],bg='ivory3',width = 500, height = 500).place(x=0,y=0)

    def mostrar_receta(self):
        self.crear_un_frame(self.get_numero_frames()[4],'ivory3',500,350)   #frame donde se ubicara la receta
        self.get_numero_frames()[6].pack(fill='x')
        
        Label(self.get_numero_frames()[6],text=' >Receta: ',width=30,anchor='w').pack(side='top',fill='x') #boton vaciar campos
        self.crear_un_frame(self.get_numero_frames()[6],'ivory3',400,300)   #frame donde se ubicara la receta dentro del frame
        self.get_numero_frames()[7].pack(side='top',fill='y')
        Button(self.get_numero_frames()[6],text='Vaciar campos',width=30,command=self.vaciar_campos).pack(side='bottom',fill='x') #boton vaciar campos
        
    def dar_las_indicaciones(self):
        if len(self.get_sintomas())==0:
            Label(self.get_numero_frames()[7],bg='ivory3',width = 500, height = 500).place(x=0,y=0)
        else:
            Label(self.get_numero_frames()[7],text=self.receta_medica,bg='ivory3',
        justify='left').place(x=0,y=0)