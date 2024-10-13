
#! Aplicación que crea Umbral según selección del Mouse.
#? En pantalla muestra la cámara y textBoxes para configurar la pieza (patrón) a medir para crear un Umbral 
#?    con referencia a él. Por ejemplo, según la pieza (patrón) de 10mm crea un Umbral de 3mm.  

import cv2
import numpy as np
import tkinter as tk
from PIL import Image, ImageTk




class UmbralApp:

    def __init__(self, master):
        self.master = master
        self.points = []
        self.scale = 10.0    # 10mm (PATRÓN DE MEDICIÓN)
        self.spacing = 3.0   # 3mm (TAMAÑO DEL UMBRAL)

        # Variables de zoom
        self.zoom_factor = 1.0
        self.zoom_step = 0.1  # Ajusta este valor para definir la cantidad de zoom por paso
        self.max_zoom = 3.0    # Zoom máximo
        self.min_zoom = 0.5    # Zoom mínimo

        self.msg = 'Seleccione en forma Vertical'
        self.angulo = 0
        
        self.setup_ui()  # Configurar la interfaz gráfica

        # Intentar abrir la cámara
        self.cap = cv2.VideoCapture(ip)
        if not self.cap.isOpened():
            print("Error: No se pudo abrir la cámara.")
            exit()  # Salir si la cámara no se abre

       

        self.update_frame()  # Iniciar el ciclo de actualización del frame

    def setup_ui(self):
        """Configura la interfaz gráfica de la aplicación."""
        self.master.title("AndyO - Slitter, mesa de empalme")

        # Cambiar el ícono de la ventana
        logo_path = "C:/Users/HP/Desktop/Probando Ando/Python/cosas_de_PYTHON/AndyO.ico" 
        icono = ImageTk.PhotoImage(file=logo_path)
        self.master.iconphoto(False, icono)

        # Conectar eventos
        self.master.bind('n', self.borrar_puntos)
        self.master.bind('<Configure>', self.on_resize)  # Evento de redimensionamiento
        self.master.bind("<Button-1>", self.clics)  # Evento de clic en el canvas
        self.master.bind('l', self.rotar_izquierda)  # Evento para rotar a la izquierda
        self.master.bind('r', self.rotar_derecha)    # Evento para rotar a la derecha
        self.master.bind('+', self.zoom_in)          # Evento de zoom in
        self.master.bind('-', self.zoom_out)         # Evento de zoom out


        #! Frame para los controles superiores
        control_frame = tk.Frame(self.master, bg="lightgray", height=30)
        control_frame.pack(side=tk.TOP, fill=tk.X)
        control_frame.pack_propagate(False)  # Evita que el frame ajuste automáticamente su tamaño

        #! Frame para el canvas
        camera_frame = tk.Frame(self.master, highlightthickness=2)
        camera_frame.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)


        # Crear un canvas para mostrar el feed de la webcam
        self.canvas_width = 640
        self.canvas_height = 480
        self.canvas = tk.Canvas(camera_frame, width=self.canvas_width, height=self.canvas_height)
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Crear barra de desplazamiento vertical
        self.v_scrollbar = tk.Scrollbar(camera_frame, orient="vertical", command=self.canvas.yview)
        self.v_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.h_scrollbar = tk.Scrollbar(self.master, orient="horizontal", command=self.canvas.xview)
        self.h_scrollbar.pack(side=tk.BOTTOM, fill=tk.X)

        # Configurar el canvas para que use las barras de desplazamiento
        self.canvas.configure(yscrollcommand=self.v_scrollbar.set, xscrollcommand=self.h_scrollbar.set)

        # Ajustar la región de desplazamiento del canvas
        self.canvas.config(scrollregion=(0, 0, self.canvas_width, self.canvas_height))

        # Actualizar tareas pendientes para calcular el tamaño
        self.master.update_idletasks()

        







        # #!!!! Botón para imprimir tamaños
        # self.button_get_sizes = tk.Button(control_frame, text="Obtener tamaños", command=self.get_sizes)
        # self.button_get_sizes.pack()

        #!!!! Botón + de ZOOM
        self.button_zoom_in = tk.Button(control_frame, text="🔎+", command=self.get_sizes)
        self.button_zoom_in.pack()
        #!!!! Botón - de ZOOM
        self.button_zoom_out = tk.Button(control_frame, text="🔎-", command=self.get_sizes)
        self.button_zoom_out.pack()


        




        # Label y Textbox para scale (tamaño del PATRÓN)
        self.label_scale = tk.Label(control_frame, text="Patrón:", bg="lightgray")
        # self.label_scale.place(x=650, y=10)  # Posición inicial
        self.scale1 = tk.Entry(control_frame, width=5)
        self.scale1.insert(0, str(self.scale))
        # self.scale1.place(x=720, y=10)
        #!Probando
        self.scale1.pack()
        # self.scale1.bind("<Button-1>", self.stop_propagation)


        # Label y Textbox para spacing (Distancia entre líneas del centro - UMBRAL)
        self.label_spacing = tk.Label(control_frame, text="Umbral:", bg="lightgray")
        self.spacing1 = tk.Entry(control_frame, width=5)
        self.spacing1.insert(0, str(self.spacing))
        #!Probando
        self.spacing1.pack()
        # self.spacing1.bind("<Button-1>", self.stop_propagation)
        


        # Botón para actualizar valores
        self.button_update = tk.Button(control_frame, text="OK", command=self.update_values)
        #!Probando
        self.button_update.pack()
        # self.button_update.bind("<Button-1>", self.stop_propagation)



        # Footer
        self.label_info_rotar = tk.Label(self.master, text="Rotar: (L) (R)", bg="lightgray", font=("Helvetica", 8, "bold"))
        self.label_info_rotar.pack()

        self.label_info_limpiar = tk.Label(self.master, text="Limpiar: (N)", bg="lightgray", font=("Helvetica", 8, "bold"))
        self.label_info_limpiar.pack()  # o place, según tu diseño

        self.label_info_zoomInOut = tk.Label(self.master, text="ZoomIN-OUT: (+)(-)", bg="lightgray", font=("Helvetica", 8, "bold"))
        self.label_info_zoomInOut.pack()  # o place, según tu diseño
        
        # self.label_info_zoomOUT = tk.Label(self.master, text="ZoomOUT: (-)", bg="lightgray", font=("Helvetica", 8, "bold"))
        # self.label_info_zoomOUT.pack()  # o place, según tu diseño
        
        self.label_coordenadas = tk.Label(self.master, text="X, Y: (0, 0)", bg="lightgray")
        self.label_coordenadas.pack()  # o place según tu diseño
        
        self.label_punto1 = tk.Label(self.master, text="P1: (0, 0)", bg="lightgray")
        self.label_punto1.pack()  # o place según tu diseño
        
        self.label_punto2 = tk.Label(self.master, text="P2: (0, 0)", bg="lightgray")
        self.label_punto2.pack()  # o place según tu diseño

        # Actualizar tareas pendientes para calcular el tamaño del Label
        self.master.update_idletasks()







    def on_resize(self, event):
        """Ajusta la posición de los elementos al redimensionar la ventana."""
        self.posicionar_desde_borde_derecho()

    def borrar_puntos(self, event):
        """Borra los puntos seleccionados."""
        self.points = []  # Limpiar la lista de puntos
        self.label_punto1.config(text="P1: (0, 0)")  # Limpiar el label del punto 1
        self.label_punto2.config(text="P2: (0, 0)")  # Limpiar el label del punto 2
    
        print("Puntos borrados")

    def posicionar_desde_borde_derecho(self):
        """Posiciona los elementos de la interfaz desde el borde derecho del canvas."""
        self.master.update_idletasks()  # Asegurar que las dimensiones se actualicen
        
        canvas_width = self.master.winfo_width()  # Obtener el ancho del root
        canvas_height = self.master.winfo_height()  # Obtener el alto del root
        
        label_info_zoomInOut_width = self.label_info_zoomInOut.winfo_width()
        # label_info_zoomOUT_width = self.label_info_zoomOUT.winfo_width()
        label_info_rotar_width = self.label_info_rotar.winfo_width()
        info_limpiar_width = self.label_info_limpiar.winfo_width()  # Obtener el alto del root
        label_coordenadas_width = self.label_coordenadas.winfo_width()
        label_punto1_width = self.label_punto1.winfo_width()

        



        #? PROBANDO BOTÓN ZOOM
        button_zoom_in_height = self.button_zoom_in.winfo_height()    # Ancho de botón zoom_in
        button_zoom_out_height = self.button_zoom_out.winfo_height()    # Ancho de botón zoom_in




        self.label_scale.place(x=5, y=4)
        self.scale1.place(x=48, y=5)
        
        self.label_spacing.place(x=85, y=4)
        self.spacing1.place(x=132, y=5)
        
        self.button_update.place(x=175, y=2)

        #? PROBANDO BOTÓN ZOOM
        self.button_zoom_in.place(x=250, y=2)
        self.button_zoom_out.place(x=283, y=2)
        

        #!!!!!!!!!!!! Probando
        self.h_scrollbar.place(x=canvas_width - 80, y=canvas_height - 23)


        self.label_info_rotar.place(x=8, y=canvas_height - 25)  # Posición inicial
        self.label_info_limpiar.place(x=label_info_rotar_width + 20, y=canvas_height - 25)

        self.label_info_zoomInOut.place(x=label_info_rotar_width + info_limpiar_width + 20 + 11, y=canvas_height - 25)  # Posición inicial
        self.label_coordenadas.place(x=label_info_rotar_width + info_limpiar_width + label_info_zoomInOut_width + 20 + 21, y=canvas_height - 25)

        self.label_punto1.place(x=label_info_rotar_width + info_limpiar_width + label_coordenadas_width + label_info_zoomInOut_width + 20 + 11 + 11, y=canvas_height - 25)

        self.label_punto2.place(x=label_info_rotar_width + info_limpiar_width + label_coordenadas_width + label_punto1_width+ label_info_zoomInOut_width + 20 + 11 + 11, y=canvas_height - 25)
        
        
        



        

    def update_values(self):
        """Actualiza los valores de scale y spacing según la entrada del usuario."""
        self.scale = float(self.scale1.get())
        self.spacing = float(self.spacing1.get())


    def dibujando_puntos(self, frame):
        """Dibuja los puntos seleccionados en el frame."""
        if len(self.points) > 0:
            for x, y in self.points:
                cv2.circle(frame, (x, y), 3, (0, 255, 0), 1)

    def rotar_imagen(self, frame, angulo):
        """Rota la imagen según el ángulo dado."""
        (h, w) = frame.shape[:2]  # Altura y ancho del frame
        centro = (w // 2, h // 2)  # Centro de la imagen

        M = cv2.getRotationMatrix2D(centro, angulo, 1.0)
        return cv2.warpAffine(frame, M, (w, h))



    def rotar_izquierda(self, event):
        """Rota la imagen 10 grados a la izquierda."""
        self.angulo += 2  # Decrementa el ángulo
        print(f"Rotando a la izquierda: {self.angulo} grados")

    def rotar_derecha(self, event):
        """Rota la imagen 10 grados a la derecha."""
        self.angulo -= 2  # Incrementa el ángulo
        print(f"Rotando a la derecha: {self.angulo} grados")

    def mostrar_coordenadas(self, event):
        x, y = event.x, event.y
        self.label_coordenadas.config(text=f"X, Y: ({x}, {y})")

    def clics(self, event):
        # Verifica si el widget que disparó el evento no es un Button o Entry
        if isinstance(event.widget, tk.Button) or isinstance(event.widget, tk.Entry):
            return  # Si es un botón o entrada de texto, no hacer nada
        

    # Captura los puntos seleccionados con el mouse y actualiza los labels de los puntos.
        x, y = event.x, event.y
        if len(self.points) < 2:
            self.points.append([x, y])
            if len(self.points) == 1:
                self.setear_p1(x, y)
            elif len(self.points) == 2:
                self.setear_p2(x, y)

    def setear_p1(self, x, y):
        # Actualiza el label del primer punto con las coordenadas seleccionadas.
        self.label_punto1.config(text=f"P1: ({x}, {y})")

    def setear_p2(self, x, y):
        # Actualiza el label del segundo punto con las coordenadas seleccionadas.
        self.label_punto2.config(text=f"P2: ({x}, {y})")





    def zoom_in(self, event):
        """Incrementa el factor de zoom."""
        if self.zoom_factor < self.max_zoom:
            self.zoom_factor += self.zoom_step
        print(f"Zoom In: Factor de zoom = {self.zoom_factor}")

    def zoom_out(self, event):
        """Decrementa el factor de zoom."""
        if self.zoom_factor > self.min_zoom:
            self.zoom_factor -= self.zoom_step
        print(f"Zoom Out: Factor de zoom = {self.zoom_factor}")







    #!!!!! Obtener valores de tamaños
    def get_sizes(self):
        """Obtiene los tamaños del root, canvas, y frame y los imprime."""
        # Tamaño del root
        root_width = self.master.winfo_width()
        root_height = self.master.winfo_height()
        print(f"Tamaño del root: {root_width}x{root_height}")

        # Tamaño del canvas
        canvas_width = self.canvas.winfo_width()
        canvas_height = self.canvas.winfo_height()
        print(f"Tamaño del canvas: {canvas_width}x{canvas_height}")

        # Tamaño del frame (de la cámara)
        ret, frame = self.cap.read()
        if ret:
            frame_height, frame_width = frame.shape[:2]
            print(f"Tamaño del frame: {frame_width}x{frame_height}")
        else:
            print("No se pudo obtener el frame de la cámara.")










    def update_frame(self):
        # Actualiza el feed de la cámara continuamente.
        ret, frame = self.cap.read()
        if not ret:
            return 


        # Redimensionar el frame aplicando el factor de zoom
        height, width = frame.shape[:2]
        new_width = int(width * self.zoom_factor)
        new_height = int(height * self.zoom_factor)
        frame = cv2.resize(frame, (new_width, new_height))

        # Si el frame es más grande que el canvas, recortarlo para centrarse en el medio
        # canvas_width = self.canvas.winfo_width()
        # canvas_height = self.canvas.winfo_height()
        # if new_width > canvas_width or new_height > canvas_height:
        #     x_start = (new_width - canvas_width) // 2
        #     y_start = (new_height - canvas_height) // 2
        #     frame = frame[y_start:y_start + canvas_height, x_start:x_start + canvas_width]



        frame = self.rotar_imagen(frame, self.angulo)
        self.dibujando_puntos(frame)




        # Mensaje si se ha seleccionado un solo punto
        if len(self.points) == 1:
            cv2.putText(frame, f'{self.msg}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0,0,255), 2)
            # print("Puntos: ", self.points)
        
        # Dibuja líneas si se han seleccionado dos puntos
        if len(self.points) == 2:
            p1, p2 = self.points
            # print('Punto1: ', p1)
            # print('Punto2: ', p2)
            pixel_distance = np.linalg.norm(np.array(p2) - np.array(p1))
            x_pixel = (self.spacing * pixel_distance) / self.scale  
            centro_x = frame.shape[1] // 2
            centro_y = frame.shape[0] // 2
            
            # Coordenadas de las líneas
            line1_start = (0, int(centro_y - x_pixel // 2))
            line1_end = (frame.shape[1], int(centro_y - x_pixel // 2))
            line2_start = (0, int(centro_y + x_pixel // 2))
            line2_end = (frame.shape[1], int(centro_y + x_pixel // 2))
            centro_vertical_start = (centro_x, int(centro_y + x_pixel // 3))
            centro_vertical_end = (centro_x, int(centro_y - x_pixel // 3))
            centro_horizontal_start = (int(centro_x - frame.shape[1] // 4), centro_y)
            centro_horizontal_end = (int(centro_x + frame.shape[1] // 4), centro_y)

            # Dibujar líneas
            cv2.line(frame, line1_start, line1_end, (0,0,0), 2)
            cv2.line(frame, line2_start, line2_end, (0,0,0), 2)
            cv2.line(frame, centro_vertical_start, centro_vertical_end, (0,255,0), 1)
            cv2.line(frame, centro_horizontal_start, centro_horizontal_end, (0,255,0), 1)

        # Convertir el frame a formato compatible con tkinter
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(frame)
        imgtk = ImageTk.PhotoImage(image=img)









        #! Ajustar el tamaño del canvas y las barras de desplazamiento
        self.canvas.create_image(0, 0, anchor=tk.NW, image=imgtk)
        self.canvas.image = imgtk  # Guardar la referencia

        # Ajustar el área desplazable del canvas
        self.canvas.config(scrollregion=self.canvas.bbox(tk.ALL))








        # Actualizar el canvas con la nueva imagen
        self.canvas.create_image(0, 0, anchor=tk.NW, image=imgtk)
        self.canvas.imgtk = imgtk  # Guardar la referencia para evitar que la imagen sea recolectada por el garbage collector

        # Llamar nuevamente a update_frame
        self.master.after(10, self.update_frame)

        self.master.bind("<Motion>", self.mostrar_coordenadas)


# Dirección IP de la cámara
# rtsp_url = "rtsp://admin:Daynadayna1301@192.168.1.108:554/cam/realmonitor?channel=4&subtype=0"
# ip = "http://192.168.220.35:4747/video"
# ip = "http://192.168.1.3:4747/video"
# ip = "http://192.168.43.172:4747/video"
ip = 1
# ip = "rtsp://admin:Royo12345@192.168.13.12:80/cam/realmonitor?channel=1&subtype=0"


if __name__ == "__main__":
    root = tk.Tk()                  # Creo ventana principal "root"
    app = UmbralApp(root)           # Llamo a la clase "UmbralApp" y todo lo ejecuto dentro de root
    root.mainloop()                 # Ejecuto continuamente root 
    
    # Liberar la cámara cuando se cierre la ventana
    app.cap.release()
    cv2.destroyAllWindows()