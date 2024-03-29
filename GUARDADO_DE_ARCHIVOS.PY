# Definición de datos

eventos={
    1:"Evento 1",
    2:"Evento 2"
}

asistentes={
    1:"Asistente 1",
    2:"Asistente 2",
    3:"Asistente 3"
}

registro={
    1:[1,1],
    2:[2,1],
    3:[3,1],
    4:[1,2],
    5:[2,2]
}

repositorio=[eventos,asistentes,registro]

# Librería para serializar json
import pickle

repositorio_pickle = pickle.dumps(repositorio)

print(repositorio_pickle)

nuevo_objeto=pickle.loads(repositorio_pickle)

print(repositorio==nuevo_objeto)

import pickle
import os

class archivador:
    objeto=''
    archivo='sin_nombre.pickle'
    respaldar=False

    def __init__(self,objeto='',archivo='',respaldar=False):
        self.objeto=objeto
        self.archivo=archivo
        self.respaldar=respaldar

    def guardar_archivo(self,
                        objeto='',
                        archivo='sin_nombre.pickle',
                        respaldar=False):
        try:
            if self.respaldar:
                nombre_bak=self.archivo.split('.')[0]+'.bak'
                if os.path.exists(archivo):
                    if (os.path.exists(nombre_bak)):
                        os.remove(nombre_bak)
                        os.rename(archivo,nombre_bak)
            # Se genera la versión serializada del objeto.
            with open(archivo,"wb+") as f:
                pickle.dump(objeto,f)
        except:
            # Si algo sale mal, retorna False (no fue posible)
            # y un str vacío.
            return False
        # Si pudo hacer la operación, retorna True.
        return True

    def leer_archivo(self,archivo):
        try:
            with open(archivo,"rb") as f:
                datos_recuperados=pickle.load(f)
        except:
            return False,''
        # Si todo salió bien, retorna verdadero, y los datos.
        return True, datos_recuperados

# Generar una instancia de la clase
trabajo=archivador()


# Leo el archivo.
resultado, repositorio=trabajo.leer_archivo('repositorio.pickle')
resultado, sin_modificar=trabajo.leer_archivo('repositorio.pickle')


# Modifico datos.
repositorio[0][3]="Evento 3"

print(repositorio)
print(sin_modificar)

# Ejecutar el método guardar_archivo()
trabajo.guardar_archivo(repositorio,'repositorio.pickle',False)

archivo='archivo.doc'
nombre_bak=archivo.split('.')[0]+'.bak'
print(nombre_bak)