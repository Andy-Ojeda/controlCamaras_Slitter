import cv2
import numpy as np
import tkinter as tk
from PIL import Image, ImageTk
from msg import imprimir_mensaje


imprimir_mensaje()


subTitulo = "Entrada de chapa (192.168.13.14)"

# Variables globales
distancia_UP = 146
distancia_DOWN = 148

centro_UP_ajuste = -25
centro_DOWN_ajuste = 25

valor_Y_UP = 25
valor_Y_DOWN = 550

canvas_w = 0
canvas_h = 0

# Función para actualizar las dimensiones del canvas al cargar la ventana
def on_load():
    global canvas_w, canvas_h
    canvas_w = canvas.winfo_width()
    canvas_h = canvas.winfo_height()
    print("La ventana ha sido cargada con ancho:", canvas_w, "y alto:", canvas_h)

# Función para actualizar las líneas con los valores de los textboxes
def update_distancia():
    global distancia_UP, distancia_DOWN
    distancia_UP = int(entry_up.get())
    distancia_DOWN = int(entry_down.get())

def update_centro():
    global centro_UP_ajuste, centro_DOWN_ajuste
    centro_UP_ajuste = int(center_up.get())
    centro_DOWN_ajuste = int(center_down.get())

def update_y():
    global valor_Y_UP, valor_Y_DOWN
    valor_Y_UP = int(y_up.get())
    valor_Y_DOWN = int(y_down.get())


def toggle_menu(event=None):
    # Mostrar u ocultar el menú lateral
    if menu_frame.winfo_ismapped():
        menu_frame.pack_forget()  # Ocultar el menú
    else:
        menu_frame.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=False)  # Mostrar el menú
            






# Función que se ejecuta continuamente para mostrar el feed de la webcam
def update_frame():
    global distancia_UP, distancia_DOWN, centro_UP_ajuste, centro_DOWN_ajuste, valor_Y_UP, valor_Y_DOWN, canvas_w, canvas_h

    ret, frame = cap.read()
    if not ret:
        return

    canvas_width = canvas.winfo_width()  # Obtener el ancho del canvas
    canvas_height = canvas.winfo_height()  # Obtener el alto del canvas

    frame = cv2.resize(frame, (canvas_width, canvas_height))


    height, width, _ = frame.shape

    centro_UP = width // 2 - centro_UP_ajuste
    centro_DOWN = width // 2 + centro_DOWN_ajuste

    left_UP = centro_UP - distancia_UP
    left_DOWN = centro_DOWN - distancia_DOWN
    right_UP = centro_UP + distancia_UP
    right_DOWN = centro_DOWN + distancia_DOWN

    # Dibujar las líneas
    cv2.line(frame, (centro_UP, valor_Y_UP), (centro_DOWN, valor_Y_DOWN), (0, 255, 0), thickness=2, lineType=cv2.LINE_AA)
    cv2.line(frame, (left_UP, valor_Y_UP), (left_DOWN, valor_Y_DOWN), (255, 0, 255), thickness=2, lineType=cv2.LINE_AA)
    cv2.line(frame, (right_UP, valor_Y_UP), (right_DOWN, valor_Y_DOWN), (255, 0, 255), thickness=2, lineType=cv2.LINE_AA)

    # Convertir el frame a formato compatible con tkinter
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    img = Image.fromarray(frame)
    imgtk = ImageTk.PhotoImage(image=img)

    # Actualizar el canvas con la nueva imagen
    canvas.create_image(0, 0, anchor=tk.NW, image=imgtk)
    canvas.imgtk = imgtk  # Guardar la referencia para evitar que la imagen sea recolectada por el garbage collector

    # Llamar nuevamente a update_frame
    root.after(10, update_frame)

# Configurar la ventana de Tkinter
root = tk.Tk()
root.title("Webcam con Control de Líneas")

#! Frame para los controles superiores
control_frame = tk.Frame(root, bg="lightgray", height=30)
control_frame.pack(side=tk.TOP, fill=tk.X)
control_frame.pack_propagate(False)  # Evita que el frame ajuste automáticamente su tamaño

# subTitulo = tk.Label(control_frame, text=f"{subTitulo}", font=("Arial", 16), anchor="center", bg="lightgray")
# subTitulo.pack()


#! Boton de Menú
menu_button = tk.Button(control_frame, text="☰", command=toggle_menu)
menu_button.pack(side="right", anchor="ne", padx=3, pady=2)

#! Crear un Label a la izquierda
label = tk.Label(control_frame, text=f"{subTitulo}", padx=5, bg="lightgray", font=("Arial", 12))
label.pack(side="left", padx=3, pady=2)


#! Frame para el canvas
camera_frame = tk.Frame(root, highlightthickness=2)
camera_frame.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

#! Frame para el Menú
menu_frame = tk.Frame(root, highlightthickness=2, bg="orange")
menu_frame.pack_propagate(False)  # Evitar que el frame se ajuste automáticamente al contenido
menu_frame.pack_forget()  # Ocultar el menú al inicio

menu_frame.configure(height=150) 


titulo_menu = tk.Label(menu_frame, text="Configuración:", font=("Arial", 16), anchor="center", bg="orange")
titulo_menu.pack(pady=5)

# Crear un canvas para mostrar el feed de la webcam
canvas = tk.Canvas(camera_frame, width=800, height=600)
canvas.pack()



# ---------------------------------  Distancia desde el Centro  -------------------------------------------
# Label y Textbox para distancia_UP
label_up = tk.Label(menu_frame, text="Distancia UP:", bg="lightgray")
label_up.place(x=10, y=50)
entry_up = tk.Entry(menu_frame, width=5)
entry_up.insert(0, str(distancia_UP))
entry_up.place(x=110, y=50)

# Label y Textbox para distancia_DOWN
label_down = tk.Label(menu_frame, text="Distancia DOWN:", bg="lightgray")
label_down.place(x=10, y=73)
entry_down = tk.Entry(menu_frame, width=5)
entry_down.insert(0, str(distancia_DOWN))
entry_down.place(x=110, y=73)

# Botón para actualizar las líneas
button_update = tk.Button(menu_frame, text="Actualizar", command=update_distancia)
button_update.place(x=10, y=100)
# -----------------------------------------------------------------------------------------------------------

# ------------------------------  Valores Linea Central  -------------------------------
# Label y Textbox para centro_UP
label_up_center = tk.Label(menu_frame, text="Centro UP:", bg="lightgray")
label_up_center.place(x=200, y=50)
center_up = tk.Entry(menu_frame, width=5)
center_up.insert(0, str(centro_UP_ajuste))
center_up.place(x=288, y=50)

# Label y Textbox para centro_DOWN
label_down_center = tk.Label(menu_frame, text="Centro DOWN:", bg="lightgray")
label_down_center.place(x=200, y=73)
center_down = tk.Entry(menu_frame, width=5)
center_down.insert(0, str(centro_DOWN_ajuste))
center_down.place(x=288, y=73)

# Botón para actualizar los valores del centro
button_update_center = tk.Button(menu_frame, text="Actualizar", command=update_centro)
button_update_center.place(x=200, y=100)
# --------------------------------------------------------------------------------------

# ------------------------------  Valores Y  -------------------------------
# Label y Textbox para valor_Y_UP
label_up_y = tk.Label(menu_frame, text="Y_UP:", bg="lightgray")
label_up_y.place(x=380, y=50)
y_up = tk.Entry(menu_frame, width=5)
y_up.insert(0, str(valor_Y_UP))
y_up.place(x=441, y=50)

# Label y Textbox para valor_Y_DOWN
label_down_y = tk.Label(menu_frame, text="Y_DOWN:", bg="lightgray")
label_down_y.place(x=380, y=73)
y_down = tk.Entry(menu_frame, width=5)
y_down.insert(0, str(valor_Y_DOWN))
y_down.place(x=441, y=73)

# Botón para actualizar los valores Y
button_update_y = tk.Button(menu_frame, text="Actualizar", command=update_y)
button_update_y.place(x=380, y=100)
# --------------------------------------------------------------------------

# Iniciar la captura de la cámara
# ip = "http://192.168.43.172:4747/video"
# ip = "http://192.168.220.35:4747/video"
url = 1
# ip = "192.168.13.14"  # Camara de Guillotina
# ip = "192.168.13.11"    # Camara de Cuchillas
# url = f"rtsp://admin:Royo12345@{ip}:80/cam/realmonitor?channel=1&subtype=1"

cap = cv2.VideoCapture(url)
cap.set(3, 800)
cap.set(4, 600)

# Llamar a la función que actualiza el feed de la cámara
root.after(100, on_load)  # Ejecutar la función `on_load` una vez que la ventana se haya cargado






root.title("AndyO - Slitter, Guia de centrado")
logo_path = "C:/Users/HP/Desktop/Probando Ando/Python/cosas_de_PYTHON/AndyO.ico" 
icono = ImageTk.PhotoImage(file=logo_path)
root.iconphoto(False, icono)


update_frame()

# Iniciar el loop principal de Tkinter
root.mainloop()

# Liberar la cámara cuando se cierre la ventana
cap.release()
cv2.destroyAllWindows()
