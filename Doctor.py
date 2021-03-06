class Doctor():
    def __init__(self,nombre,apellido,fecha_nacimiento,sexo,nombre_usuario,contrasena,especialidad,telefono,citas):
        self.nombre = nombre
        self.apellido = apellido
        self.fecha_nacimiento = fecha_nacimiento
        self.sexo = sexo 
        self.nombre_usuario = nombre_usuario
        self.contrasena = contrasena
        self.especialidad = especialidad
        self.telefono = telefono
        self.citas = citas
        
    def get_json(self):
        return{
            "nombre":self.nombre,
            "apellido":self.apellido,
            "fecha_nacimiento":self.fecha_nacimiento,
            "sexo":self.sexo,
            "nombre_usuario":self.nombre_usuario,
            "contrasena":self.contrasena,
            "especialidad":self.especialidad,
            "telefono":self.telefono,
            "citas":self.citas  
        }    
        
    def modificar_perfil(self,nombre,apellido,fecha_nacimiento,sexo,nombre_usuario,contrasena,especialidad,telefono):
        self.nombre = nombre
        self.apellido = apellido
        self.fecha_nacimiento = fecha_nacimiento
        self.sexo = sexo 
        self.nombre_usuario = nombre_usuario
        self.contrasena = contrasena
        self.especialidad = especialidad
        self.telefono = telefono       