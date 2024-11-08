import cv2
import tkinter as tk
from PIL import Image, ImageTk
from msg import imprimir_mensaje
import os
import json
import sys

base_path = "C:/Royo/Slitter/In_Out"


# Variables globales
distancia_UP = 0
distancia_DOWN = 0

distancia_UP_extra = 0
distancia_DOWN_extra = 0

distancia_UP_extra_extra = 0
distancia_DOWN_extra_extra = 0




centro_UP_ajuste = 0
centro_DOWN_ajuste = 0

valor_Y_UP = 0
valor_Y_DOWN = 0

valor_Y_UP_extra = 0
valor_Y_DOWN_extra = 0

valor_Y_UP_extra_extra = 0
valor_Y_DOWN_extra_extra = 0





titulo = "AndyO - Slitter"
subTitulo = "Entrada / Salida"

# Iniciar la captura de la cámara
url = 1
ip = "192.168.13.14"  # Camara de Guillotina
# ip = "192.168.13.11"    # Camara de Cuchillas
# url = f"rtsp://admin:Royo12345@{ip}:80/cam/realmonitor?channel=1&subtype=1"


current_color_0 = "green"
current_color_1 = "red"
current_color_2 = "red"
current_color_3 = "red"

canvas_w = 0
canvas_h = 0










def maximizar(event=None):
    root.state('zoomed')

def restaurar(event=None):
    root.state('normal')  

def mitadPantallaDerecha(event=None):
    root.geometry('%dx%d+%d+%d' % (root.winfo_screenwidth()/2, root.winfo_screenheight(), root.winfo_screenwidth()/2, 0))

def mitadPantallaIzquierda(event=None):
    root.geometry('%dx%d+%d+%d' % (root.winfo_screenwidth()/2, root.winfo_screenheight(), 0, 0))







def resource_path(relative_path):
    """Obtiene la ruta absoluta del recurso, para desarrollo o ejecutable."""
    # Para la versión empaquetada, usamos _MEIPASS
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    # Para el modo de desarrollo, usa la ruta actual
    return os.path.join(os.path.abspath("."), relative_path)

def get_config_path():
    """Obtiene la ruta del archivo de configuración."""
    return resource_path('configuracion.json')


def guardar_datos():
    # Crear un diccionario con los datos que deseas guardar
    datos = {
        'titulo': titulo,
        'subtitulo': subTitulo,
        'ip': ip,
        
        'distancia_UP': distancia_UP,
        'distancia_DOWN': distancia_DOWN,
        
        'distancia_UP_extra': distancia_UP_extra,
        'distancia_DOWN_extra': distancia_DOWN_extra,
        
        'distancia_UP_extra_extra': distancia_UP_extra_extra,
        'distancia_DOWN_extra_extra': distancia_DOWN_extra_extra,
        
        
        'centro_UP_ajuste': centro_UP_ajuste,
        'centro_DOWN_ajuste': centro_DOWN_ajuste,
        
        'valor_Y_UP': valor_Y_UP,
        'valor_Y_DOWN': valor_Y_DOWN,
        
        'valor_Y_UP_extra': valor_Y_UP_extra,
        'valor_Y_DOWN_extra': valor_Y_DOWN_extra,
        
        'valor_Y_UP_extra_extra': valor_Y_UP_extra_extra,
        'valor_Y_DOWN_extra_extra': valor_Y_DOWN_extra_extra,

        'color_0': current_color_0,
        'color_1': current_color_1,
        'color_2': current_color_2,
        'color_3': current_color_3,
    }
    
    try:
        # Guardar los datos en un archivo de texto (usando JSON para formateo sencillo)
        # ruta_archivo = os.path.join(base_path, 'configuracion.json')
        ruta_archivo = os.path.join(archivo_in_out)
        with open(ruta_archivo, 'w') as archivo:
            json.dump(datos, archivo, indent=4)
        print(f"Datos guardados exitosamente en {archivo_in_out}.")
    except Exception as e:
        print(f"Error al guardar los datos: {e}")

def cargar_datos():
    global distancia_UP, distancia_DOWN, centro_UP_ajuste, centro_DOWN_ajuste, valor_Y_UP, valor_Y_UP_extra, valor_Y_UP_extra_extra, valor_Y_DOWN, valor_Y_DOWN_extra, valor_Y_DOWN_extra_extra, ip, titulo, subTitulo, distancia_UP_extra, distancia_UP_extra_extra, distancia_DOWN_extra, distancia_DOWN_extra_extra, current_color_0, current_color_1, current_color_2, current_color_3

    try:
        # Leer los datos desde el archivo de texto
        # ruta_archivo = os.path.join(base_path, 'configuracion.json')
        ruta_archivo = os.path.join(archivo_in_out)
        with open(ruta_archivo, 'r') as archivo:
            datos = json.load(archivo)
        
        # Asignar los valores a las variables correspondientes
        ip = datos.get("ip", "192.168.13.1")
        titulo = datos.get("titulo", "AndyO - ")
        subTitulo = datos.get("subtitulo", "Entrada / Salida")
        
        distancia_UP = datos.get("distancia_UP", 140)
        distancia_DOWN = datos.get("distancia_DOWN", 148)
        
        distancia_UP_extra = datos.get("distancia_UP_extra", 150)
        distancia_DOWN_extra = datos.get("distancia_DOWN_extra", 158)
        
        distancia_UP_extra_extra = datos.get("distancia_UP_extra_extra", 160)
        distancia_DOWN_extra_extra = datos.get("distancia_DOWN_extra_extra", 168)
        
        
        
        
        centro_UP_ajuste = datos.get("centro_UP_ajuste", -25)
        centro_DOWN_ajuste = datos.get("centro_DOWN_ajuste", 25)
        
        
        valor_Y_UP = datos.get("valor_Y_UP", 25)
        valor_Y_DOWN = datos.get("valor_Y_DOWN", 550)
        
        valor_Y_UP_extra = datos.get("valor_Y_UP_extra", 25)
        valor_Y_DOWN_extra = datos.get("valor_Y_DOWN_extra", 550)
        
        valor_Y_UP_extra_extra = datos.get("valor_Y_UP_extra_extra", 25)
        valor_Y_DOWN_extra_extra = datos.get("valor_Y_DOWN_extra_extra", 550)

        current_color_0 = datos.get("color_0", "green")
        current_color_1 = datos.get("color_1", "red")
        current_color_2 = datos.get("color_2", "red")
        current_color_3 = datos.get("color_3", "red")




        print("Datos cargados exitosamente.")
    except FileNotFoundError:
        print("Archivo de configuración no encontrado. Usando valores predeterminados.")
    except json.JSONDecodeError:
        print("Error al decodificar el archivo JSON. Usando valores predeterminados.")





# Función para actualizar las dimensiones del canvas al cargar la ventana
# def on_load():
#     global canvas_w, canvas_h
#     canvas_w = canvas.winfo_width()
#     canvas_h = canvas.winfo_height()
#     print("La ventana ha sido cargada con ancho:", canvas_w, "y alto:", canvas_h)


# Función para actualizar las líneas con los valores de los textboxes
def update():
# def update_distancia():
    global distancia_UP, distancia_UP_extra, distancia_UP_extra_extra, distancia_DOWN, distancia_DOWN_extra, distancia_DOWN_extra_extra
    
    distancia_UP = int(entry_up.get())
    distancia_DOWN = int(entry_down.get())
    
    distancia_UP_extra = int(entry_up_extra.get())
    distancia_DOWN_extra = int(entry_down_extra.get())
    
    distancia_UP_extra_extra = int(entry_up_extra_extra.get())
    distancia_DOWN_extra_extra = int(entry_down_extra_extra.get())

    global centro_UP_ajuste, centro_DOWN_ajuste
    centro_UP_ajuste = int(center_up.get())
    centro_DOWN_ajuste = int(center_down.get())

    global valor_Y_UP, valor_Y_UP_extra, valor_Y_UP_extra_extra, valor_Y_DOWN, valor_Y_DOWN_extra, valor_Y_DOWN_extra_extra
    valor_Y_UP = int(y_up.get())
    valor_Y_DOWN = int(y_down.get())
    valor_Y_UP_extra = int(y_up_extra.get())
    valor_Y_DOWN_extra = int(y_down_extra.get())      
    valor_Y_UP_extra_extra = int(y_up_extra_extra.get())
    valor_Y_DOWN_extra_extra = int(y_down_extra_extra.get())


def toggle_menu(event=None):
    # Mostrar u ocultar el menú lateral
    if menu_frame.winfo_ismapped():
        menu_frame.pack_forget()  # Ocultar el menú
    else:
        menu_frame.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=False)  # Mostrar el menú
            


def cv2_color(tk_color):
    """Convertir un color de Tkinter a BGR para OpenCV"""
    tk_colors = {
        "red": (0, 0, 255),
        "navy": (128, 0, 0),
        "blue": (255, 0, 0),
        "cyan": (255, 255, 0),
        "darkgreen": (0, 100, 0),
        "green": (0, 255, 0),
        "lime": (50, 205, 50),
        "gold": (0, 215, 255),
        "yellow": (0, 255, 255),
        "purple": (128, 0, 128),
        "magenta": (255, 0, 255),
        "black": (0, 0, 0),
        "white": (255, 255, 255),
    }
    return tk_colors.get(tk_color, (0, 0, 0))  # Negro por defecto




def cambiar_color_0(event=None):
        global current_color_0
        colores0 = ["red", "navy", "blue", "cyan", "darkgreen", "green", "lime", "gold", "yellow", "purple", "magenta", "black", "white"]
        # Obtiene el índice actual del color
        current_index0 = colores0.index(current_color_0)
        # Cambia al siguiente color en la lista (ciclo)
        current_color_0 = colores0[(current_index0 + 1) % len(colores0)]
        # Cambia el color del cuadrado
        color_0_button.configure(fg=current_color_0)
        
def cambiar_color_1(event=None):
        global current_color_1
        colores = ["red", "navy", "blue", "cyan", "darkgreen", "green", "lime", "gold", "yellow", "purple", "magenta", "black", "white"]
        # Obtiene el índice actual del color
        current_index = colores.index(current_color_1)
        # Cambia al siguiente color en la lista (ciclo)
        current_color_1 = colores[(current_index + 1) % len(colores)]
        # Cambia el color del cuadrado
        color_1_button.configure(fg=current_color_1)

def cambiar_color_2(event=None):
        global current_color_2
        colores2 = ["red", "navy", "blue", "cyan", "darkgreen", "green", "lime", "gold", "yellow", "purple", "magenta", "black", "white"]
        # Obtiene el índice actual del color
        current_index2 = colores2.index(current_color_2)
        # Cambia al siguiente color en la lista (ciclo)
        current_color_2 = colores2[(current_index2 + 1) % len(colores2)]
        # Cambia el color del cuadrado
        color_2_button.configure(fg=current_color_2)

def cambiar_color_3(event=None):
        global current_color_3
        colores3 = ["red", "navy", "blue", "cyan", "darkgreen", "green", "lime", "gold", "yellow", "purple", "magenta", "black", "white"]
        # Obtiene el índice actual del color
        current_index3 = colores3.index(current_color_3)
        # Cambia al siguiente color en la lista (ciclo)
        current_color_3 = colores3[(current_index3 + 1) % len(colores3)]
        # Cambia el color del cuadrado
        color_3_button.configure(fg=current_color_3)
        












# Función que se ejecuta continuamente para mostrar el feed de la webcam
def update_frame():
    global distancia_UP, distancia_UP_extra, distancia_UP_extra_extra, distancia_DOWN, distancia_DOWN_extra, distancia_DOWN_extra_extra, centro_UP_ajuste, centro_DOWN_ajuste, valor_Y_UP, valor_Y_DOWN, canvas_w, canvas_h

    ret, frame = cap.read()
    if not ret:
        return

    # canvas_width = canvas.winfo_width()  # Obtener el ancho del canvas
    # canvas_height = canvas.winfo_height()  # Obtener el alto del canvas

    # frame = cv2.resize(frame, (canvas_width, canvas_height))


    height, width, _ = frame.shape

    centro_UP = width // 2 - centro_UP_ajuste
    centro_DOWN = width // 2 + centro_DOWN_ajuste

    left_UP = centro_UP - distancia_UP
    left_DOWN = centro_DOWN - distancia_DOWN
    right_UP = centro_UP + distancia_UP
    right_DOWN = centro_DOWN + distancia_DOWN

    left_UP_extra = centro_UP - distancia_UP_extra
    left_DOWN_extra = centro_DOWN - distancia_DOWN_extra
    right_UP_extra = centro_UP + distancia_UP_extra
    right_DOWN_extra = centro_DOWN + distancia_DOWN_extra

    left_UP_extra_extra = centro_UP - distancia_UP_extra_extra
    left_DOWN_extra_extra = centro_DOWN - distancia_DOWN_extra_extra
    right_UP_extra_extra = centro_UP + distancia_UP_extra_extra
    right_DOWN_extra_extra = centro_DOWN + distancia_DOWN_extra_extra


    # Dibujar las líneas
    # cv2.line(frame, (centro_UP, valor_Y_UP), (centro_DOWN, valor_Y_DOWN), (0, 255, 0), thickness=2, lineType=cv2.LINE_AA)
    cv2.line(frame, (centro_UP, 2), (centro_DOWN, height), cv2_color(current_color_0), thickness=2, lineType=cv2.LINE_AA)
    


    cv2.line(frame, (left_UP, valor_Y_UP), (left_DOWN, valor_Y_DOWN), cv2_color(current_color_1), thickness=2, lineType=cv2.LINE_AA)
    cv2.line(frame, (right_UP, valor_Y_UP), (right_DOWN, valor_Y_DOWN), cv2_color(current_color_1), thickness=2, lineType=cv2.LINE_AA)
    # Dibujar las líneas adicionales
    cv2.line(frame, (left_UP_extra, valor_Y_UP_extra), (left_DOWN_extra, valor_Y_DOWN_extra), cv2_color(current_color_2), thickness=2, lineType=cv2.LINE_AA)
    cv2.line(frame, (right_UP_extra, valor_Y_UP_extra), (right_DOWN_extra, valor_Y_DOWN_extra), cv2_color(current_color_2), thickness=2, lineType=cv2.LINE_AA)
    # Dibujar las líneas adicionales adicionales
    cv2.line(frame, (left_UP_extra_extra, valor_Y_UP_extra_extra), (left_DOWN_extra_extra, valor_Y_DOWN_extra_extra), cv2_color(current_color_3), thickness=2, lineType=cv2.LINE_AA)
    cv2.line(frame, (right_UP_extra_extra, valor_Y_UP_extra_extra), (right_DOWN_extra_extra, valor_Y_DOWN_extra_extra), cv2_color(current_color_3), thickness=2, lineType=cv2.LINE_AA)



    # Convertir el frame a formato compatible con tkinter
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    img = Image.fromarray(frame)
    imgtk = ImageTk.PhotoImage(image=img)

    # Actualizar el canvas con la nueva imagen
    camera_canvas.create_image(0, 0, anchor=tk.NW, image=imgtk)
    camera_canvas.imgtk = imgtk  # Guardar la referencia para evitar que la imagen sea recolectada por el garbage collector

    # Llamar nuevamente a update_frame
    root.after(10, update_frame)



#?==========================================================================================

# Configurar la ventana de Tkinter
root = tk.Tk()
root.pack_propagate(True) 


root.title(titulo)

logo_path = os.path.join(base_path, 'AndyO.ico')
icono = ImageTk.PhotoImage(file=logo_path)
root.iconphoto(False, icono)


# Minimizar la ventana al iniciar
root.iconify()






archivo_in_out = "C:/Royo/Slitter/In_Out/configuracion_In.json"
seleccion_in_out = imprimir_mensaje()

if seleccion_in_out != "":
    root.deiconify()
    print("Cargando configuraciones...")

if seleccion_in_out == "in":
    archivo_in_out = "C:/Royo/Slitter/In_Out/configuracion_In.json"
    print("Cargando configuración de Cámara de entrada")

if seleccion_in_out == "out":
    archivo_in_out = "C:/Royo/Slitter/In_Out/configuracion_Out.json"
    print("Cargando configuración de Cámara de salida")
        








cargar_datos()


cap = cv2.VideoCapture(url)
cap.set(3, 800)
cap.set(4, 600)


#! Frame para los controles superiores
control_frame = tk.Frame(root, bg="lightgray", height=30)
control_frame.pack(side=tk.TOP, fill=tk.X)
control_frame.pack_propagate(False)  # Evita que el frame ajuste automáticamente su tamaño
#! Boton de Menú
menu_button = tk.Button(control_frame, text="☰", command=toggle_menu)
menu_button.pack(side="right", anchor="ne", padx=3, pady=2)
#! Crear un Label a la izquierda
label = tk.Label(control_frame, text=f"{subTitulo}", padx=5, bg="lightgray", font=("Arial", 12))
label.pack(side="left", padx=3, pady=2)



#! Frame para el canvas
camera_frame = tk.Frame(root, highlightthickness=2)
camera_frame.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
camera_frame.pack_propagate(True) 



canvas_width = 640
canvas_height = 480
# Crear un canvas dentro del frame para permitir desplazamiento
camera_canvas = tk.Canvas(camera_frame, width=canvas_width, height=canvas_height, bg="black")
camera_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Crear barra de desplazamiento vertical
v_scrollbar = tk.Scrollbar(camera_frame, orient="vertical", command=camera_canvas.yview)
v_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
# Crear barra de desplazamiento horizontal
h_scrollbar = tk.Scrollbar(camera_frame, orient="horizontal", command=camera_canvas.xview)
h_scrollbar.pack(side=tk.BOTTOM, fill=tk.X)

# Configurar el canvas para que use las barras de desplazamiento
camera_canvas.configure(yscrollcommand=v_scrollbar.set, xscrollcommand=h_scrollbar.set)
# Ajustar la región de desplazamiento del canvas
camera_canvas.config(scrollregion=(0, 0, canvas_width, canvas_height))




#! Frame para el Menú
menu_frame = tk.Frame(root, highlightthickness=2, bg="orange")
menu_frame.pack_propagate(False)  # Evitar que el frame se ajuste automáticamente al contenido
menu_frame.pack_forget()  # Ocultar el menú al inicio

menu_frame.configure(height=180) 


titulo_menu = tk.Label(menu_frame, text="Configuración:", font=("Arial", 16), anchor="center", bg="orange")
titulo_menu.pack(pady=5)

# Crear un Label a la izquierda
label_ip = tk.Label(menu_frame, text=f"IP: {ip}", font=("Arial", 10), bg="orange")
label_ip.pack(pady=2)
label_ip.place(x=10 , y=10)


cor_x = 30


color_0_button = tk.Button(menu_frame, text="Color", fg=current_color_0, command=cambiar_color_0)
color_0_button.pack()
color_0_button.place(x=300+cor_x+cor_x+cor_x , y=144)

color_1_button = tk.Button(menu_frame, text="Color", fg=current_color_1, command=cambiar_color_1)
color_1_button.pack()
color_1_button.place(x=12 , y=144)

color_2_button = tk.Button(menu_frame, text="Color", fg=current_color_2, command=cambiar_color_2)
color_2_button.pack()
color_2_button.place(x=107+cor_x , y=144)

color_3_button = tk.Button(menu_frame, text="Color", fg=current_color_3, command=cambiar_color_3)
color_3_button.pack()
color_3_button.place(x=202+cor_x+cor_x , y=144)

button_update_center = tk.Button(menu_frame, text="  OK  ", command=update)
button_update_center.pack()
button_update_center.place(x=300+cor_x+cor_x+cor_x, y=50)

guardar_button = tk.Button(menu_frame, text="Guardar", command=guardar_datos)
guardar_button.pack()
guardar_button.place(x=342+cor_x+cor_x+cor_x, y=50)








# # Crear un canvas para mostrar el feed de la webcam
# canvas_width = 640
# canvas_height = 480
# canvas = tk.Canvas(camera_frame, width=canvas_width, height=canvas_height, bg="black")
# canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)


# ---------------------------------  Distancia desde el Centro  -------------------------------------------
# Label y Textbox para distancia_UP
label_up = tk.Label(menu_frame, text="Dist_1🔺", bg="lightgray")
label_up.place(x=12, y=50)
entry_up = tk.Entry(menu_frame, width=5)
entry_up.insert(0, str(distancia_UP))
entry_up.place(x=63, y=52)

# Label y Textbox para distancia_DOWN
label_down = tk.Label(menu_frame, text="Dist_1🔻", bg="lightgray")
label_down.place(x=12, y=73)
entry_down = tk.Entry(menu_frame, width=5)
entry_down.insert(0, str(distancia_DOWN))
entry_down.place(x=63, y=75)
#?-----------------------------------------------------------
# Label y Textbox para distancia_UP_extra
label_up_extra = tk.Label(menu_frame, text="Dist_2🔺", bg="lightgray")
label_up_extra.place(x=107+cor_x, y=50)
entry_up_extra = tk.Entry(menu_frame, width=5)
entry_up_extra.insert(0, str(distancia_UP_extra))
entry_up_extra.place(x=158+cor_x, y=52)

# Label y Textbox para distancia_DOWN_extra
label_down_extra = tk.Label(menu_frame, text="Dist_2🔻", bg="lightgray")
label_down_extra.place(x=107+cor_x, y=73)
entry_down_extra = tk.Entry(menu_frame, width=5)
entry_down_extra.insert(0, str(distancia_DOWN_extra))
entry_down_extra.place(x=158+cor_x, y=75)
#?-----------------------------------------------------------
# Label y Textbox para distancia_UP_extra_extra
label_up_extra_extra = tk.Label(menu_frame, text="Dist_3🔺", bg="lightgray")
label_up_extra_extra.place(x=202+cor_x+cor_x, y=50)
entry_up_extra_extra = tk.Entry(menu_frame, width=5)
entry_up_extra_extra.insert(0, str(distancia_UP_extra_extra))
entry_up_extra_extra.place(x=253+cor_x+cor_x, y=52)

# Label y Textbox para distancia_DOWN_extra_extra
label_down_extra_extra = tk.Label(menu_frame, text="Dist_3🔻", bg="lightgray")
label_down_extra_extra.place(x=202+cor_x+cor_x, y=73)
entry_down_extra_extra = tk.Entry(menu_frame, width=5)
entry_down_extra_extra.insert(0, str(distancia_DOWN_extra_extra))
entry_down_extra_extra.place(x=253+cor_x+cor_x, y=75)
#?-----------------------------------------------------------















# Botón para actualizar las líneas
# button_update = tk.Button(menu_frame, text="Actualizar", command=update_distancia)
# button_update.place(x=10, y=100)
# -----------------------------------------------------------------------------------------------------------

# ------------------------------  Valores Linea Central  -------------------------------
# Label y Textbox para centro_UP
label_up_center = tk.Label(menu_frame, text="Centro 🔺", bg="lightgray")
label_up_center.place(x=300+cor_x+cor_x+cor_x, y=96)
center_up = tk.Entry(menu_frame, width=5)
center_up.insert(0, str(centro_UP_ajuste))
center_up.place(x=359+cor_x+cor_x+cor_x, y=98)

# Label y Textbox para centro_DOWN
label_down_center = tk.Label(menu_frame, text="Centro 🔻", bg="lightgray")
label_down_center.place(x=300+cor_x+cor_x+cor_x, y=119)
center_down = tk.Entry(menu_frame, width=5)
center_down.insert(0, str(centro_DOWN_ajuste))
center_down.place(x=359+cor_x+cor_x+cor_x, y=121)

# --------------------------------------------------------------------------------------

# ------------------------------  Valores Y  -------------------------------
# Label y Textbox para valor_Y_UP
label_up_y = tk.Label(menu_frame, text="Mov_1🔺", bg="lightgray")
label_up_y.place(x=12, y=96)
y_up = tk.Entry(menu_frame, width=4)
y_up.insert(0, str(valor_Y_UP))
y_up.place(x=69, y=98)

# Label y Textbox para valor_Y_DOWN
label_down_y = tk.Label(menu_frame, text="Mov_1🔻", bg="lightgray")
label_down_y.place(x=12, y=119)
y_down = tk.Entry(menu_frame, width=4)
y_down.insert(0, str(valor_Y_DOWN))
y_down.place(x=69, y=121)
# --------------------------------------------------------------------------
# Label y Textbox para valor_Y_UP_extra
label_up_y_extra = tk.Label(menu_frame, text="Mov_2🔺", bg="lightgray")
label_up_y_extra.place(x=107+cor_x, y=96)
y_up_extra = tk.Entry(menu_frame, width=4)
y_up_extra.insert(0, str(valor_Y_UP_extra))
y_up_extra.place(x=164+cor_x, y=98)

# Label y Textbox para valor_Y_DOWN_extra
label_down_y_extra = tk.Label(menu_frame, text="Mov_2🔻", bg="lightgray")
label_down_y_extra.place(x=107+cor_x, y=119)
y_down_extra = tk.Entry(menu_frame, width=4)
y_down_extra.insert(0, str(valor_Y_DOWN_extra))
y_down_extra.place(x=164+cor_x, y=121)
# --------------------------------------------------------------------------
# Label y Textbox para valor_Y_UP_extra_extra
label_up_y_extra_extra = tk.Label(menu_frame, text="Mov_3🔺", bg="lightgray")
label_up_y_extra_extra.place(x=202+cor_x+cor_x, y=96)
y_up_extra_extra = tk.Entry(menu_frame, width=4)
y_up_extra_extra.insert(0, str(valor_Y_UP_extra))
y_up_extra_extra.place(x=259+cor_x+cor_x, y=98)

# Label y Textbox para valor_Y_DOWN_extra_extra
label_down_y_extra_extra = tk.Label(menu_frame, text="Mov_3🔻", bg="lightgray")
label_down_y_extra_extra.place(x=202+cor_x+cor_x, y=119)
y_down_extra_extra = tk.Entry(menu_frame, width=4)
y_down_extra_extra.insert(0, str(valor_Y_DOWN_extra_extra))
y_down_extra_extra.place(x=259+cor_x+cor_x, y=121)
# --------------------------------------------------------------------------







root.bind('m', maximizar)
root.bind('d', mitadPantallaDerecha)
root.bind('i', mitadPantallaIzquierda)
root.bind('<Escape>', restaurar)






update_frame()

# Iniciar el loop principal de Tkinter
root.mainloop()

# Liberar la cámara cuando se cierre la ventana
cap.release()
cv2.destroyAllWindows()
