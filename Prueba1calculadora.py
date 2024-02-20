import tkinter as tk
from PIL import Image, ImageTk

def agregar_caracter(caracter):
    expresion_actual = variable_expresion.get()
    variable_expresion.set(expresion_actual + str(caracter))

def borrar_caracter():
    expresion_actual = variable_expresion.get()
    variable_expresion.set(expresion_actual[:-1])

def limpiar_pantalla():
    variable_expresion.set("")

def calcular_resultado():
    try:
        expresion = variable_expresion.get()
        resultado = eval(expresion)
        variable_expresion.set(resultado)
    except Exception as e:
        variable_expresion.set("Error")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Jericle234")
ventana.geometry("300x400")

ruta_imagen = r'C:\Users\jereRomero\Downloads\jere.ico'  # Cambia esto a la ruta de tu icono
imagen = Image.open(ruta_imagen)

# # Convertir la imagen a un formato que Tkinter pueda manejar
imagen_tk = ImageTk.PhotoImage(imagen)

# # Establecer la imagen como ícono de la ventana
ventana.iconphoto(True, imagen_tk)


# Variable para almacenar la expresión actual
variable_expresion = tk.StringVar()

# Crear una casilla de entrada (Entry) vinculada a la variable
entrada = tk.Entry(ventana, textvariable=variable_expresion, font=('Arial', 14), justify='right')
entrada.grid(row=0, column=0, columnspan=4, padx=10, pady=10, ipady=10)

# Definir los botones
botones = [
    '1', '2', '3', '/',
    '4', '5', '6', '*',
    '7', '8', '9', '-',
    '0', '.', '=', '+'
]

# Funciones para los botones
row_val = 1
col_val = 0

for boton_texto in botones:
    tk.Button(ventana, text=boton_texto, width=5, height=2,
            command=lambda bt=boton_texto: agregar_caracter(bt) if bt != '=' else calcular_resultado()).grid(row=row_val, column=col_val, padx=5, pady=5)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Botón de borrado
tk.Button(ventana, text="C", width=5, height=2, command=limpiar_pantalla).grid(row=row_val, column=col_val, padx=5, pady=5)

# Botón de retroceso
col_val += 1
tk.Button(ventana, text="<-", width=5, height=2, command=borrar_caracter).grid(row=row_val, column=col_val, padx=5, pady=5)

# Mostrar la ventana
ventana.mainloop()