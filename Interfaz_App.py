from tkinter import *
import sqlite3
from tkinter import messagebox

#---------------------FUNCIÓN CONEXIÓN-------------------------

def conexionBBDD():
    
    miConexion = sqlite3.connect("Usuarios")
    
    miCursor = miConexion.cursor()
    
    
    try:
        miCursor.execute('''
                        
                        CREATE TABLE DATOSUSUARIOS (
                        ID INTEGER PRIMARY KEY AUTOINCREMENT,
                        NOMBRE_USUARIO VARCHAR(50),
                        PASSWORD VARCHAR(50),
                        APELLIDO_USUARIO VARCHAR(50),
                        DIRECCION VARCHAR(50),
                        COMENTARIOS VARCHAR(100)
                        )
                        
                        ''')
        
        messagebox.showinfo("BBDD", "BBDD creada con éxito")
    
    except:
        
        messagebox.showwarning("!Atención¡", "La BBDD ya existe") 

#---------------------FUNCIONES-------------------------
#---------------------FUNCIÓN SALIR-------------------------

def salirAplicacion():
    
    valor = messagebox.askquestion("Salir", "¿Desea salir de la aplicación?")

    if valor == "yes":
        
        root.destroy()
        
#---------------------FUNCIÓN BORRAR CAMPOS-------------------------

def limpiarCampos():
    
    miID.set("")
    miNombre.set("")
    miPass.set("")
    miApellido.set("")
    miDireccion.set("")
    cuadroComentarios.delete(1.0, END)
    
#---------------------FUNCIONES CRUD-------------------------
#---------------------CREAR-------------------------

def crear():
    
    miConexion = sqlite3.connect("Usuarios")
    
    miCursor = miConexion.cursor()
    
    datos = miNombre.get(), miPass.get(), miApellido.get(), miDireccion.get(), cuadroComentarios.get("1.0", END)
    # miCursor.execute("INSERT INTO DATOSUSUARIOS VALUES(NULL, '" + miNombre.get() +
    #                  "','" + miPass.get() +
    #                  "','" + miApellido.get() +
    #                  "','" + miDireccion.get() +
    #                  "','" + cuadroComentarios.get("1.0", END) + "')")
    
    miCursor.execute("INSERT INTO DATOSUSUARIOS VALUES (NULL, ?,?,?,?,?)", (datos))
    
    miConexion.commit()
    
    messagebox.showinfo("BBDD", "Registro insertado con éxito")

#---------------------LEER-------------------------

def leer():
    
    miConexion = sqlite3.connect("Usuarios")
    
    miCursor = miConexion.cursor()
    
    miCursor.execute("SELECT * FROM DATOSUSUARIOS WHERE ID=" + miID.get())
    
    elUsuario = miCursor.fetchall()
    
    for usuario in elUsuario:
        
        miID.set(usuario[0])
        miNombre.set(usuario[1])
        miPass.set(usuario[2])
        miApellido.set(usuario[3])
        miDireccion.set(usuario[4])
        cuadroComentarios.insert(1.0, usuario[5])
        
    miConexion.commit()
    
#---------------------ACTUALIZAR-------------------------

def actualizar():
    
    miConexion = sqlite3.connect("Usuarios")
    
    miCursor = miConexion.cursor()
    
    # datos = miNombre.get(), miPass.get(), miApellido.get(), miDireccion.get, cuadroComentarios.get("1.0", END)
    miCursor.execute("UPDATE DATOSUSUARIOS SET NOMBRE_USUARIO='" + miNombre.get() +
                     "', PASSWORD='" + miPass.get() +
                     "', APELLIDO_USUARIO='" + miApellido.get() +
                     "', DIRECCION='" + miDireccion.get() +
                     "', COMENTARIOS='" + cuadroComentarios.get("1.0", END) +
                     "' WHERE ID=" + miID.get())

    # miCursor.execute("UPDATE DATOSUSUARIOS SET NOMBRE_USUARIO=?, PASSWORD=?, APELLIDO_USUARIO=?, DIRECCION=?, COMENTARIOS=? " +
    #                  "WHERE ID=" + miID.get(),(datos))

    miConexion.commit()
    
    messagebox.showinfo("BBDD", "Registro actualizado con éxito")

#---------------------ELIMINAR-------------------------

def eliminar():
    
    miConexion = sqlite3.connect("Usuarios")
    
    miCursor = miConexion.cursor()
    
    miCursor.execute("DELETE FROM DATOSUSUARIOS WHERE ID=" + miID.get())
    
    miConexion.commit()
    
    messagebox.showinfo("BBDD", "Registro eliminado con éxito")


root = Tk()

#---------------------CREACIÓN BARRA MENU-------------------------

barraMenu = Menu(root)
root.config(menu= barraMenu, width= 300, height= 300)

bbddMenu = Menu(barraMenu, tearoff= 0)
bbddMenu.add_command(label= "Conectar", command= conexionBBDD)
bbddMenu.add_command(label= "Salir", command= salirAplicacion)

borrarMenu = Menu(barraMenu, tearoff= 0)
borrarMenu.add_command(label= "Borrar campos", command= limpiarCampos)

crudMenu = Menu(barraMenu, tearoff= 0)
crudMenu.add_command(label= "Crear", command= crear)
crudMenu.add_command(label= "Leer", command= leer)
crudMenu.add_command(label= "Actualizar" , command= actualizar)
crudMenu.add_command(label= "Borrar", command= eliminar)

ayudaMenu = Menu(barraMenu, tearoff= 0)
ayudaMenu.add_command(label= "Licencia")
ayudaMenu.add_command(label= "Acerca de...")

barraMenu.add_cascade(label= "BBDD", menu= bbddMenu)
barraMenu.add_cascade(label= "Borrar", menu= borrarMenu)
barraMenu.add_cascade(label= "CRUD", menu= crudMenu)
barraMenu.add_cascade(label= "Ayuda", menu= ayudaMenu)

#---------------------PRIMER FRAME-------------------------

primerFrame = Frame(root)
primerFrame.pack()

miID = StringVar()
miNombre = StringVar()
miApellido = StringVar()
miPass = StringVar()
miDireccion = StringVar()

#---------------------ID-------------------------

cuadroID = Entry(primerFrame, textvariable= miID)
cuadroID.grid(row= 0, column= 1, padx= 10, pady= 10)
etiquetaID = Label(primerFrame, text= "ID:")
etiquetaID.grid(row= 0, column= 0, sticky= "e", padx= 10, pady= 10)

#---------------------NOMBRE-------------------------

cuadroNombre = Entry(primerFrame, textvariable= miNombre)
cuadroNombre.grid(row= 1, column= 1, padx= 10, pady= 10)
cuadroNombre.config(fg= "red", justify= "right")
etiquetaNombre = Label(primerFrame, text= "Nombre:")
etiquetaNombre.grid(row= 1, column= 0, sticky= "e", padx= 10, pady= 10)

#---------------------PASSWORD-------------------------

cuadroPass = Entry(primerFrame, textvariable= miPass)
cuadroPass.grid(row= 2, column= 1, padx= 10, pady= 10)
cuadroPass.config(show= "?")
etiquetaPass = Label(primerFrame, text= "Password:")
etiquetaPass.grid(row= 2, column= 0, sticky= "e", padx= 10, pady= 10)

#---------------------APELLIDO-------------------------

cuadroApellido = Entry(primerFrame, textvariable= miApellido)
cuadroApellido.grid(row= 3, column= 1, padx= 10, pady= 10)
etiquetaApellido = Label(primerFrame, text= "Apellido:")
etiquetaApellido.grid(row= 3, column= 0, sticky= "e", padx= 10, pady= 10)

#---------------------DIRECCIÓN-------------------------

cuadroDireccion = Entry(primerFrame, textvariable= miDireccion)
cuadroDireccion.grid(row= 4, column= 1, padx= 10, pady= 10)
etiquetaDireccion = Label(primerFrame, text= "Dirección:")
etiquetaDireccion.grid(row= 4, column= 0, sticky= "e", padx= 10, pady= 10)

#---------------------COMENTARIOS-------------------------

cuadroComentarios = Text(primerFrame, width= 20, height= 10)
cuadroComentarios.grid(row= 5, column= 1, padx= 10, pady= 10)
etiquetaComentarios = Label(primerFrame, text= "Comentarios:")
etiquetaComentarios.grid(row= 5, column= 0, sticky= "e", padx= 10, pady= 10)

scrollVert = Scrollbar(primerFrame, command= cuadroComentarios.yview)
scrollVert.grid(row= 5, column= 2, sticky= "nsew")

cuadroComentarios.config(yscrollcommand= scrollVert.set)

#---------------------SEGUNDO FRAME-------------------------
#---------------------AQUÍ VAN LOS BOTONES-------------------------

segundoFrame = Frame(root)
segundoFrame.pack()

botonCrear = Button(segundoFrame, text= "Create", command= crear)
botonCrear.grid(row= 1, column= 0, padx= 10 , pady= 10)

botonLeer = Button(segundoFrame, text= "Read", command= leer)
botonLeer.grid(row= 1, column= 1, padx= 10, pady= 10)

botonActualizar = Button(segundoFrame, text= "Update", command= actualizar)
botonActualizar.grid(row= 1, column= 2, padx= 10, pady= 10)

botonBorrar = Button(segundoFrame, text= "Delete", command= eliminar)
botonBorrar.grid(row= 1, column= 3, padx= 10, pady= 10)

root.mainloop()