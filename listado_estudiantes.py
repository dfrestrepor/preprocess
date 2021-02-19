import pandas as pd
import os

PATH = os.path.abspath(os.path.dirname("__file__"))


class Student(object):

    def __init__(self, fecha):
        self.fecha = fecha
        self.asistencia = []
        self.columns = ['nombre', 'pais', 'ocupacion']
        self.df = pd.DataFrame(list(), columns=self.columns)
        self.messages('inicio')
        self.created_student()

    def created_student(self):
        nombre = input('Ingrese el nombre: ')
        pais = input('Ingrese el País: ')
        ocupacion = input('Ingrese la ocupación: ')
        estudiante = {'nombre':nombre, 'pais':pais, 'ocupacion':ocupacion}
        self.df = self.df.append(estudiante, ignore_index=True)
        print(self.df)
        self.save_student('creado')

    def edit_student(self):
        name = input('Ingrese el nombre del DS: ')
        field = input('Ingrese el nombre del campo por actualizar: ')
        put = input('Ingrese la actualizacion: ')
        index = self.df.index[self.df['nombre'] == name]
        self.df.loc[index[0]:,field] = put
        self.save_student('actualizado')

    def save_student(self, message):
        self.df.to_csv(PATH + '/listado_'+ self.fecha + '.csv', index=False)
        self.messages(message)

    def get_student(self):
        print(self.df)

    def messages(self, ms):
        message = {'inicio': '## Hola Soy el administrador de estudiantes \n'
                             '############################################',
                    'creado': 'El estudiante ha sido guardado ',
                    'actualizado': 'El estudiante actualizado'
                   }
        print(message[ms])





