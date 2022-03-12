class Enfermedades_concretas:
    def __init__(self):
        self.__diccionario_enfermedad={'Fiebre':'Ibuprofeno 600mg',
            'Escalofrio':'Paracetamol 500mg',
            'Dolor Muscular':'Naproxeno sodico 550mg',
            'Mareo':'Anautin',
            'Colico':'Femen Forte',
            'Estres':'Complejo B amp',
            'Vomito':'Pedialyte 60',
            'Picazon del cuerpo':'Loratadina 10mg',
            'Palidez':'Pedialyte 60',
            'Desparacitante':'Colufase 500mg'}
        self.__diccionario_dolores={'Dolor de cabeza':{'Dol. Cab. Punsante':'Migradorixina',
            'Dol. Cab. Recurrente':'Migradorixina',
            'Molesta la luz':'BuprexMigra',
            'Dol. Cab. Simple':'BuprexMigra',
            'Cosquilleo':'Gerimax'},
            'Dolor del oido':{'Zumbido':'Otozambon',
            'Molestia en el oidio':'Otozambon',
            'Picazon en el oido':'Otozambon'},
            'Dolor visual':{'Ardor en la vista':'Gentamicina gotas',
            'Ojos rojos':'Visine Extra',
            'Tiene lagañas':'Visine Extra',
            'Inchazonde los ojos':'Visine Extra'},
            'Dolor al cuero cabelludo':{'Picazon en la cabeza':'Medicasp',
            'Ardor en la cabeza':'Medicasp'},
            'Dolor bucal':{'Llagas':'Topident',
            'Labios Partidos':'Pedialyte 60',
            'Herpes labial':'Aciclovir 800mg',
            'Dolor de muelas':'Molarex Forte'},
            'Dolor nasal':{'Secrecion de nariz':'Neogripal',
            'Nariz tapada':'Afrin'},
            'Dolor de cuello-garganta':{'duele al Pasar liquidos':'Nimesulida 100mg',
            'Ardor cuello-garganta':'Ibuprofeno 600mg',
            'Afonico':'Activox'},
            'Dolor del pecho':{'Punzadas al corazon':'Insocaps',
            'Cosquilleo en el pecho':'Insocaps',
            'Mal Golpe en el pecho':'Diclofenaco 50mg',
            'Dolor de mamas':'Paracetamol 500mg',
            'Falta de aire':'Salbutamol'},
            'Dolor de brazos-piernas':{
            'Dolor en Articulaciones brzos-piernas':'Arcoxia 90mg',
            'Cosquilleo brazos-piernas':'Dolo-neurobion',
            'Tronchedura del musculo':'Naproxeno sodico 550mg'},
            'Dolor de espalda':{'Estres':'Complejo B amp',
            'Molestia en espalda':'Gerimax',
            'Dolor lumbar':'Dolo-neurobion',
            'Dol. Espalda por mal movimiento':'Diclofenaco 50mg',
            'Inflamacion en espalda':'Dolo-neurobion'},
            'Dolor estomacal':{'Retorsijones':'Proxina',
            'Flojera estomacal':'Enterogermina',
            'Ardor de barriga':'Omeprazol 20mg',
            'Llenura':'Sal Andrius',
            'Gases':'Sal Andrius'},
            'Dolor de los pies':{'Inchazon en los pies':'Ibuprofeno 600mg',
            'Pies helados':'Complejo B amp'},
            'Dolor de partes intimas':{'Ardor al orinar':'Uvamin',
            'Mal olor en la orina':'Uvamin',
            'Secrecion(Mujeres)':'Lomecan-V'}
        }
    def get_diccionario_enfermedad(self):
        return self.__diccionario_enfermedad
    def get_diccionario_dolores(self):
        return self.__diccionario_dolores
        
    def imprime(self,lista):
        contador=0
        lista_medicamentos=[]
        for key in lista:
            for sintoma in self.get_diccionario_enfermedad():
                if key==sintoma:
                    lista_medicamentos.append(self.get_diccionario_enfermedad()[key]) 
                    contador+=1
        if contador < len(lista):
            for key in lista:
                for dolor in self.get_diccionario_dolores():
                    for sintoma in self.get_diccionario_dolores()[dolor]:
                        if sintoma==key:
                            lista_medicamentos.append(self.get_diccionario_dolores()[dolor][sintoma])
        return lista_medicamentos