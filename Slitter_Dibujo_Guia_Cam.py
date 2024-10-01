import cv2
import numpy as np
import tkinter as tk
from PIL import Image, ImageTk

# Variables globales
distancia_UP = 152
distancia_DOWN = 257

centro_UP_ajuste = 2
centro_DOWN_ajuste = 17

valor_Y_UP = 250
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

# Función que se ejecuta continuamente para mostrar el feed de la webcam
def update_frame():
    global distancia_UP, distancia_DOWN, centro_UP_ajuste, centro_DOWN_ajuste, valor_Y_UP, valor_Y_DOWN, canvas_w, canvas_h

    ret, frame = cap.read()
    if not ret:
        return

    canvas_width = canvas.winfo_width()  # Obtener el ancho del canvas
    canvas_height = canvas.winfo_height()  # Obtener el alto del canvas

    frame = cv2.resize(frame, (canvas_width, canvas_height))






    center_up.place(x=canvas_width - 40, y=10)
    label_up_center.place(x=canvas_width - 108, y=10)
    center_down.place(x=canvas_width - 40, y=35)
    label_down_center.place(x=canvas_width - 128, y=35)
    button_update_center.place(x=canvas_width - 68, y=60)

    y_up.place(x=canvas_width - 40, y=110)
    label_up_y.place(x=canvas_width - 80, y=110)
    y_down.place(x=canvas_width - 40, y=140)
    label_down_y.place(x=canvas_width - 102, y=140)
    button_update_y.place(x=canvas_width - 68, y=170)







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

# Crear un canvas para mostrar el feed de la webcam
canvas = tk.Canvas(root, width=800, height=600)
canvas.pack()

# ---------------------------------  Distancia desde el Centro  -------------------------------------------
# Label y Textbox para distancia_UP
label_up = tk.Label(root, text="Distancia UP:", bg="lightgray")
label_up.place(x=10, y=10)
entry_up = tk.Entry(root, width=5)
entry_up.insert(0, str(distancia_UP))
entry_up.place(x=110, y=10)

# Label y Textbox para distancia_DOWN
label_down = tk.Label(root, text="Distancia DOWN:", bg="lightgray")
label_down.place(x=10, y=40)
entry_down = tk.Entry(root, width=5)
entry_down.insert(0, str(distancia_DOWN))
entry_down.place(x=110, y=40)

# Botón para actualizar las líneas
button_update = tk.Button(root, text="Actualizar", command=update_distancia)
button_update.place(x=10, y=70)
# -----------------------------------------------------------------------------------------------------------

# ------------------------------  Valores Linea Central  -------------------------------
# Label y Textbox para centro_UP
label_up_center = tk.Label(root, text="Centro UP:", bg="lightgray")
label_up_center.place(x=650, y=10)
center_up = tk.Entry(root, width=5)
center_up.insert(0, str(centro_UP_ajuste))
center_up.place(x=740, y=10)

# Label y Textbox para centro_DOWN
label_down_center = tk.Label(root, text="Centro DOWN:", bg="lightgray")
label_down_center.place(x=650, y=35)
center_down = tk.Entry(root, width=5)
center_down.insert(0, str(centro_DOWN_ajuste))
center_down.place(x=740, y=35)

# Botón para actualizar los valores del centro
button_update_center = tk.Button(root, text="Actualizar", command=update_centro)
button_update_center.place(x=650, y=70)
# --------------------------------------------------------------------------------------

# ------------------------------  Valores Y  -------------------------------
# Label y Textbox para valor_Y_UP
label_up_y = tk.Label(root, text="Y_UP:", bg="lightgray")
label_up_y.place(x=650, y=110)
y_up = tk.Entry(root, width=5)
y_up.insert(0, str(valor_Y_UP))
y_up.place(x=740, y=110)

# Label y Textbox para valor_Y_DOWN
label_down_y = tk.Label(root, text="Y_DOWN:", bg="lightgray")
label_down_y.place(x=650, y=140)
y_down = tk.Entry(root, width=5)
y_down.insert(0, str(valor_Y_DOWN))
y_down.place(x=740, y=140)

# Botón para actualizar los valores Y
button_update_y = tk.Button(root, text="Actualizar", command=update_y)
button_update_y.place(x=650, y=170)
# --------------------------------------------------------------------------

# Iniciar la captura de la cámara
ip = "http://192.168.43.172:4747/video"
ip = 1
cap = cv2.VideoCapture(ip)
cap.set(3, 800)
cap.set(4, 600)

# Llamar a la función que actualiza el feed de la cámara
root.after(100, on_load)  # Ejecutar la función `on_load` una vez que la ventana se haya cargado
update_frame()

# Iniciar el loop principal de Tkinter
root.mainloop()

# Liberar la cámara cuando se cierre la ventana
cap.release()
cv2.destroyAllWindows()
