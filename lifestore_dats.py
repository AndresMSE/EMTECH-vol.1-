from nbformat import write

def register():
    print("\n" + "// REGISTRO AL SISTEMA" + "\n")
    Database = open("Datos_R.txt", "r")
    users = []
    passw = []
    for i in Database:
        a,b = i.split(", ")
        b = b.strip()
        users.append(a)
        passw.append(b)
    data_dict = dict(zip(users,passw))
    print("REGISTRO DE USUARIO" + "\n")
    Username = input("Ingresa tu nombre de usuario: ")
    Password1 = input("Escribe tu contraseña: ")
    Password2 = input("Confirma tu contraseña: ")
    
    if len(Username) == 0: 
        print("Debes ingresar tus datos")
        register()
    else:
        if len(Password1) <= 6:
            print("Error: La contraseña debe ser mayor a 6 caracteres")
            register()
        elif Password1 != Password2:
            print("Error: Contraseñas no coinciden, vuelve a intentar")
            register()
        elif  Username in users:
            print("Error: El usuario ya está registrado")
            register()
        else:
            Database = open("Datos_R.txt","a")
            Database.write(Username+ ", " + Password1 +"\n")
            Database.close()
            print("Registrado con éxito!")
            home()
def access():
    print("\n" + "// ACCESO AL SISTEMA"+"\n")
    Database = open("Datos_R.txt", "r")
    users = []
    passw = []
    for i in Database:
        a,b = i.split(", ")
        b = b.strip()
        users.append(a)
        passw.append(b)
    data_dict = dict(zip(users,passw))
    print("ACCESO DE USUARIO"+"\n")
    Username = input("Ingresa tu nombre de usuario: ")
    Password = input("Ingresa tu contraseña: ")
    try:
        if data_dict[Username]:
            try:
                if Password == data_dict[Username]:
                    print("Acceso permitido")
                    print("Bienvenido!")
                else:
                    print("El usuario o contraseña no coinciden")
                    access()
            except:
                print("El usuario o contraseña no coinciden")
                access()
        else:
            print("El usuario no está registrado ")
            answer = input("¿Desea reintentar [retry] o registrarse [sign up]? ")
            if answer == "retry":
                access()
            elif answer == "sign up":
                register()
            else:
                print("No has seleccionado una opción ")
                home()
    except:
        print("Error de acceso, el usuario no está registrado")
        answer = input("¿Desea reintentar [retry] o volver al menu [home]? ")
        if answer == "retry":
            access()
        elif answer == "home":
            home()
        else:
            print("No has seleccionado una opción ")
            home()

def home(option = None):
    print("\n" + "// BIENVENIDO AL SISTEMA"+"\n")
    option = input("¿Desea registrarse [sign up] o ingresar [log in]? ")
    if option == "sign up":
        register()
    elif option == "log in" :
        access()
    else:
        print("No has seleccionado una opción válida")
        home()
home()

