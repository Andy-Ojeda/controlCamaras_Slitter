
#! Aplicación que crea Umbral según selección del Mouse.
#? En pantalla muestra la cámara y textBoxes para configurar la pieza (patrón) a medir para crear un Umbral 
#?    con referencia a él. Por ejemplo, según la pieza (patrón) de 10mm crea un Umbral de 3mm.  
 
import cv2
import numpy as np
import tkinter as tk
from PIL import Image, ImageTk
import threading
from msg import imprimir_mensaje
import os
import json


class UmbralApp:

    def __init__(self, master):

        
        self.base_path = "C:/Royo/Slitter/Torchas"

        # Dirección IP de la cámara
        # rtsp_url = "rtsp://admin:Daynadayna1301@192.168.1.108:554/cam/realmonitor?channel=4&subtype=0"
        # self.ip = "http://192.168.43.172:4747/video"
        # self.url = 1
        # self.ip = 1
        self.ip = "192.168.13.13"       # Torcha 1
        # self.ip = "192.168.13.12"       # Torcha 2


        self.subTitulo = "Torcha_2"
        self.titulo = "AndyO - Slitter"

        self.master = master
        
        self.mensaje_error = False

        # Estado inicial para la cámara
        self.cap = None
        self.reconnect_button = None

        self.points = []
        self.scale = 10.0               # 10mm (PATRÓN DE MEDICIÓN)
        self.spacing = 3.0              # 3mm (TAMAÑO DEL UMBRAL)
        self.linea_de_inicio = 47.0     # 47mm (Distancia desde prensa a primer linea del umbral)
        

        self.desplazamiento_y = 0
        self.desplaz_x = 0
        self.anguloIzq = 0
        self.anguloDer = 0

        # Variables de zoom
        self.zoom_factor = 1.0
        self.zoom_step = 0.1  # Ajusta este valor para definir la cantidad de zoom por paso
        self.max_zoom = 3.0    # Zoom máximo
        self.min_zoom = 0.0    # Zoom mínimo

        self.msg = 'Seleccione en forma Vertical'
        self.angulo = 0
        
        self.frame_actual = None
        
        self.capturando = True  # Variable de control para detener el hilo

        
        imprimir_mensaje()


        self.setup_ui()  # Configurar la interfaz gráfica
        # self.mostrar_pantalla_negra()

        self.connect_camera()
    
    
    def connect_camera(self):
        # Intentar abrir la cámara
        self.cap = cv2.VideoCapture(self.url)
        if not self.cap.isOpened():
            print("Error: No se pudo abrir la cámara.")
            self.mostrar_pantalla_negra()
        
        self.update_frame()  # Iniciar el ciclo de actualización del frame


    def setup_ui(self):
        # self.url = f"rtsp://admin:Royo12345@{self.ip}:80/cam/realmonitor?channel=1&subtype=0"
        self.url = 1
        self.cargar_datos()
        """Configura la interfaz gráfica de la aplicación."""

        self.master.title(self.titulo)

        # Cambiar el ícono de la ventana
        logo_path = os.path.join(self.base_path, 'AndyO.ico')
        icono = ImageTk.PhotoImage(file=logo_path)
        self.master.iconphoto(False, icono)

        arrow_left = self.cargar_imagen('arrow_left.png')
        arrow_right = self.cargar_imagen('arrow_right.png')
        rotate_left = self.cargar_imagen('rotate-left.png')
        rotate_right = self.cargar_imagen('rotate-right.png')




        #! Frame para los controles superiores
        control_frame = tk.Frame(self.master, bg="lightgray", height=30)
        control_frame.pack(side=tk.TOP, fill=tk.X)
        control_frame.pack_propagate(False)  # Evita que el frame ajuste automáticamente su tamaño

        #! Frame para el canvas
        camera_frame = tk.Frame(self.master, highlightthickness=2)
        camera_frame.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        #! Frame para el Menú
        self.menu_frame = tk.Frame(self.master, highlightthickness=2, bg="orange")
        self.menu_frame.pack_propagate(False)  # Evitar que el frame se ajuste automáticamente al contenido
        self.menu_frame.pack_forget()  # Ocultar el menú al inicio

        self.menu_frame.configure(height=100) 


        #! Crear un Label a la izquierda
        label = tk.Label(control_frame, text=f"{self.subTitulo}", padx=5, bg="lightgray", font=("Arial", 12))
        label.pack(side="left", padx=3, pady=2)



        self.titulo_menu = tk.Label(self.menu_frame, text="Configuración:", font=("Arial", 16), anchor="center", bg="orange")
        self.titulo_menu.pack(pady=5)
        

        self.label_ip = tk.Label(self.menu_frame, text=f"IP: {self.ip}", font=("Arial", 10), bg="orange")
        self.label_ip.pack(pady=2)
        self.label_ip.place(x=10 , y=10)

        guardar_button = tk.Button(self.menu_frame, text="Guardar", command=self.guardar_datos)
        guardar_button.pack()
        guardar_button.place(x=150 , y=10)



       #! Boton de Menú
        self.menu_button = tk.Button(control_frame, text="☰", command=self.toggle_menu)
        self.menu_button.pack(anchor="ne", padx=3, pady=2)
        

        # Crear un canvas para mostrar el feed de la webcam
        self.canvas_width = 640
        self.canvas_height = 480
        self.canvas = tk.Canvas(camera_frame, width=self.canvas_width, height=self.canvas_height, bg="black")
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)



        #!!!! Hilo para la captura de frames
        self.captura_thread = threading.Thread(target=self.capturar_frames, daemon=True)
        self.captura_thread.start()




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

    

        # Botón + de ZOOM
        self.button_zoom_in = tk.Button(control_frame, text="🔎+", command=self.zoom_in)
        self.button_zoom_in.pack()
        # Botón - de ZOOM
        self.button_zoom_out = tk.Button(control_frame, text="🔎-", command=self.zoom_out)
        self.button_zoom_out.pack()



        # Botones para mover las líneas hacia arriba y abajo
        self.boton_arriba = tk.Button(control_frame, text="🔺", command=self.mover_arriba)
        self.boton_arriba.pack(side=tk.LEFT)
        self.boton_arriba['state'] = 'disabled'
        
        self.boton_abajo = tk.Button(control_frame, text="🔻", command=self.mover_abajo)
        self.boton_abajo.pack(side=tk.LEFT)
        self.boton_abajo['state'] = 'disabled'

        # Botones para MOVER las líneas a la izquierda y derecha
        self.boton_izquierda = tk.Button(control_frame, image=arrow_left, command=self.mover_Umbral_izquierda)
        self.boton_izquierda.image = arrow_left  
        self.boton_izquierda.pack(side=tk.LEFT)
        self.boton_izquierda['state'] = 'disabled'
        
        self.boton_derecha = tk.Button(control_frame, image=arrow_right, command=self.mover_Umbral_derecha)
        self.boton_derecha.image = arrow_right  
        self.boton_derecha.pack(side=tk.LEFT)
        self.boton_derecha['state'] = 'disabled'

        # Botones para ROTAR las líneas a la izquierda y derecha
        self.boton_rotar_izquierda = tk.Button(control_frame, image=rotate_left, command=self.rotar_Umbral_izquierda)
        self.boton_rotar_izquierda.image = rotate_left  
        self.boton_rotar_izquierda.pack(side=tk.LEFT)
        self.boton_rotar_izquierda['state'] = 'disabled'
        
        self.boton_rotar_derecha = tk.Button(control_frame, image=rotate_right, command=self.rotar_Umbral_derecha)
        self.boton_rotar_derecha.image = rotate_right  
        self.boton_rotar_derecha.pack(side=tk.LEFT)
        self.boton_rotar_derecha['state'] = 'disabled'

        # Label y Textbox para scale (tamaño del PATRÓN)
        self.label_scale = tk.Label(self.menu_frame, text="Patrón:", bg="lightgray")
        self.scale1 = tk.Entry(self.menu_frame, width=5)
        self.scale1.insert(0, str(self.scale))
        self.scale1.pack()
        
        # Label y Textbox para spacing (Distancia entre líneas del centro - UMBRAL)
        self.label_spacing = tk.Label(self.menu_frame, text="Umbral:", bg="lightgray")
        self.spacing1 = tk.Entry(self.menu_frame, width=5)
        self.spacing1.insert(0, str(self.spacing))
        self.spacing1.pack()
        
        # Botón para actualizar valores
        self.button_update = tk.Button(self.menu_frame, text="OK", command=self.update_values)
        self.button_update.pack()

        # Label y Textbox para primera Linea (Distancia entre Prensa - UMBRAL)
        self.label_lineaUno = tk.Label(self.menu_frame, text="Linea de Inicio:", bg="lightgray")
        self.spacing_linea_de_inicio = tk.Entry(self.menu_frame, width=5)
        self.spacing_linea_de_inicio.insert(0, str(self.linea_de_inicio))
        self.spacing_linea_de_inicio.pack()

        #Label Zoom_Factor
        self.label_info_ZOOM = tk.Label(control_frame, text=f"x{self.zoom_factor}", bg="lightgray")
        self.label_info_ZOOM.pack()

        # Footer
        self.label_info_rotar = tk.Label(self.master, text="Rotar: (L) (R)", bg="lightgray", font=("Helvetica", 8, "bold"))
        self.label_info_rotar.pack()

        self.label_info_limpiar = tk.Label(self.master, text="Limpiar: (N)", bg="lightgray", font=("Helvetica", 8, "bold"))
        self.label_info_limpiar.pack()  # o place, según tu diseño

        self.label_punto1 = tk.Label(self.master, text="P1: (0, 0)", bg="lightgray")
        self.label_punto1.pack()  # o place según tu diseño
        
        self.label_punto2 = tk.Label(self.master, text="P2: (0, 0)", bg="lightgray")
        self.label_punto2.pack()  # o place según tu diseño


        # Conectar eventos
        self.master.bind('n', self.borrar_puntos)
        self.master.bind('<Configure>', self.on_resize)  # Evento de redimensionamiento
        self.master.bind("<Button-1>", self.clics)  # Evento de clic en el canvas
        self.master.bind('l', self.rotar_izquierda)  # Evento para rotar a la izquierda
        self.master.bind('r', self.rotar_derecha)    # Evento para rotar a la derecha
        self.master.bind('+', self.zoom_in)          # Evento de zoom in
        self.master.bind('-', self.zoom_out)         # Evento de zoom out

        self.master.protocol("WM_DELETE_WINDOW", self.on_closing)
    



    
    def guardar_datos(self):
        # Crear un diccionario con los datos que deseas guardar
        datos = {
            "titulo": self.titulo,
            "subtitulo": self.subTitulo,
            "ip": self.ip,
            "patron": self.scale,
            "umbral": self.spacing,
            "distancia_inicial": self.linea_de_inicio 
        }
        
        try:
            ruta_archivo = os.path.join(self.base_path, 'configuracion.json')
            with open(ruta_archivo, 'w') as archivo:
                json.dump(datos, archivo, indent=4)
            print(f"Datos guardados exitosamente en {ruta_archivo}.")
        except Exception as e:
            print(f"Error al guardar los datos: {e}")


    def cargar_datos(self):
        try:
            # Leer los datos desde el archivo de texto
            ruta_archivo = os.path.join(self.base_path, 'configuracion.json')
            with open(ruta_archivo, 'r') as archivo:
                datos = json.load(archivo)
            
            self.ip = datos.get("ip", "192.168.13.1")
            self.titulo = datos.get("titulo", "AndyO - Slitter")
            self.subTitulo = datos.get("subtitulo", "Torcha")
            self.scale = datos.get("patron", 10.0) 
            self.spacing = datos.get("umbral", 3.0)
            self.linea_de_inicio = datos.get("distancia_inicial", 47.0) 


            print("Datos cargados exitosamente.")
        except FileNotFoundError:
            print("Archivo de configuración no encontrado. Usando valores predeterminados.")


    def cargar_imagen(self, filename, size=(20, 20)):
        path = os.path.join(self.base_path, filename)
        image = Image.open(path)
        return ImageTk.PhotoImage(image.resize(size))




    #! Probando ----------------------------------
    def mostrar_pantalla_negra(self):
        # Rellenar el canvas con negro
        self.canvas.create_rectangle(0, 0, self.canvas_width, self.canvas_height, fill="black")
         # Agregar el texto "Sin Señal" en el medio de la pantalla
        self.canvas.create_text(self.canvas_width // 2, self.canvas_height // 2, text="Sin Señal", fill="red", font=("Helvetica", 24))
        if self.reconnect_button is None:
            self.reconnect_button = tk.Button(self.canvas, text="Reconectar", command=self.reconnect_camera)
            self.reconnect_button.place(x=self.canvas_width // 2 - 50, y=(self.canvas_height // 2) + 30)
        else:
            self.reconnect_button.place_forget()  # Asegúrate de que el botón no esté visible antes
    #!-----------------------------------------------

    def hide_reconnect_button(self):
        # Ocultar el botón de reconexión si está visible
        if self.reconnect_button is not None:
            self.reconnect_button.place_forget()
            self.reconnect_button = None


    def reconnect_camera(self):
        print("Reconectando cámara...1")  # Para depuración
    
        # Intentar reconectar la cámara
        self.connect_camera()
        print("Reconectando cámara...2")  # Para depuración
    
        # self.reconnect_button.pack_forget()
        self.hide_reconnect_button()
        print("Reconectando cámara...3")  # Para depuración
    
        # self.reconnect_button = None


    def mover_arriba(self):
        # Ajusta el valor de desplazamiento
        self.desplazamiento_y -= 1

    def mover_abajo(self):
        # Ajusta el valor de desplazamiento
        self.desplazamiento_y += 1

    def mover_Umbral_izquierda(self):
        # Ajusta el ángulo de rotación
        self.desplaz_x -= 5
       
    def mover_Umbral_derecha(self):
        # Ajusta el ángulo de rotación
        self.desplaz_x += 5
       
    def rotar_Umbral_izquierda(self):
        # Ajusta el ángulo de rotación
        self.anguloIzq += 1
        self.anguloDer -= 1
       
    def rotar_Umbral_derecha(self):
        # Ajusta el ángulo de rotación
        self.anguloIzq -= 1
        self.anguloDer += 1



    def on_resize(self, event):
        """Ajusta la posición de los elementos al redimensionar la ventana."""
        self.posicionar_desde_borde_derecho()

    def borrar_puntos(self, event):
        """Borra los puntos seleccionados."""
        self.points = []  # Limpiar la lista de puntos
        self.label_punto1.config(text="P1: (0, 0)")  # Limpiar el label del punto 1
        self.label_punto2.config(text="P2: (0, 0)")  # Limpiar el label del punto 2
    
        self.label_punto1.config(bg="lightgrey")
        self.label_punto2.config(bg="lightgrey")
        
        self.boton_arriba['state'] = 'disabled'
        self.boton_abajo['state'] = 'disabled'
        self.boton_izquierda['state'] = 'disabled'
        self.boton_derecha['state'] = 'disabled'
        self.boton_rotar_izquierda['state'] = 'disabled'
        self.boton_rotar_derecha['state'] = 'disabled'
            
        print("Puntos borrados")

    def posicionar_desde_borde_derecho(self):
        """Posiciona los elementos de la interfaz desde el borde derecho del canvas."""
        self.master.update_idletasks()  # Asegurar que las dimensiones se actualicen
        
        canvas_width = self.master.winfo_width()  # Obtener el ancho del root
        canvas_height = self.master.winfo_height()  # Obtener el alto del root
        
        label_info_rotar_width = self.label_info_rotar.winfo_width()
        info_limpiar_width = self.label_info_limpiar.winfo_width()  # Obtener el alto del root
        label_punto1_width = self.label_punto1.winfo_width()

        self.label_scale.place(x=5, y=50)
        self.scale1.place(x=51, y=51)
        
        self.label_spacing.place(x=94, y=50)
        self.spacing1.place(x=143, y=51)

        self.label_lineaUno.place(x=186 , y=50)
        self.spacing_linea_de_inicio.place(x=273 , y=51)
        
        self.button_update.place(x=325, y=48)

        self.label_info_ZOOM.place(x=320, y=4)

        # PROBANDO BOTÓN ZOOM
        self.button_zoom_in.place(x=250, y=2)
        self.button_zoom_out.place(x=283, y=2)

        self.boton_arriba.place(x=390, y=2)
        self.boton_abajo.place(x=415, y=2)
        self.boton_izquierda.place(x=445, y=2)
        self.boton_derecha.place(x=474, y=2)
        self.boton_rotar_izquierda.place(x=508, y=2)
        self.boton_rotar_derecha.place(x=538, y=2)
        

        # Probando
        self.h_scrollbar.place(x=canvas_width - 80, y=canvas_height - 23)

        self.label_info_rotar.place(x=8, y=canvas_height - 25)  # Posición inicial
        self.label_info_limpiar.place(x=label_info_rotar_width + 20, y=canvas_height - 25)
        self.label_punto1.place(x=label_info_rotar_width + info_limpiar_width + 20 + 11, y=canvas_height - 25)
        self.label_punto2.place(x=label_info_rotar_width + info_limpiar_width + label_punto1_width + 20 + 11, y=canvas_height - 25)
        

    def update_values(self):
        """Actualiza los valores de scale y spacing según la entrada del usuario."""
        self.scale = float(self.scale1.get())
        self.spacing = float(self.spacing1.get())
        self.linea_de_inicio = float(self.spacing_linea_de_inicio.get())


    # def dibujando_puntos(self, frame):
    #     """Dibuja los puntos seleccionados en el frame."""
    #     if len(self.points) > 0:
    #         for x, y in self.points:
    #             cv2.circle(frame, (x, y), 3, (0, 255, 0), 1)

    def rotar_imagen(self, frame, angulo):
        """Rota la imagen según el ángulo dado."""
        (h, w) = frame.shape[:2]  # Altura y ancho del frame
        centro = (w // 2, h // 2)  # Centro de la imagen

        M = cv2.getRotationMatrix2D(centro, angulo, 1.0)
        return cv2.warpAffine(frame, M, (w, h))



    def rotar_izquierda(self, event):
        """Rota la imagen 10 grados a la izquierda."""
        self.angulo += 1  # Decrementa el ángulo
        print(f"Rotando a la izquierda: {self.angulo} grados")

    def rotar_derecha(self, event):
        """Rota la imagen 10 grados a la derecha."""
        self.angulo -= 1  # Incrementa el ángulo
        print(f"Rotando a la derecha: {self.angulo} grados")

    # def mostrar_coordenadas(self, event):
    #     x, y = event.x, event.y
    #     self.label_coordenadas.config(text=f"X, Y: ({x}, {y})")

    def clics(self, event):
        # Verifica si el widget que disparó el evento no es un Button o Entry o ScrollBar
        if isinstance(event.widget, (tk.Button, tk.Entry, tk.Scrollbar)):
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





    def zoom_in(self, event=None):
        """Incrementa el factor de zoom."""
        if self.zoom_factor < self.max_zoom:
            self.zoom_factor += self.zoom_step
        print(f"Zoom In: Factor de zoom = {self.zoom_factor}")
        self.label_info_ZOOM.config(text=f"x{self.zoom_factor:.1f}")  # Limpiar el label del punto 1
        

    def zoom_out(self, event=None):
        """Decrementa el factor de zoom."""
        if self.zoom_factor > self.min_zoom:
            self.zoom_factor -= self.zoom_step
        print(f"Zoom Out: Factor de zoom = {self.zoom_factor}")
        self.label_info_ZOOM.config(text=f"x{self.zoom_factor:.1f}")  # Limpiar el label del punto 1


    def toggle_menu(self, event=None):
        # Mostrar u ocultar el menú lateral
        if self.menu_frame.winfo_ismapped():
            self.menu_frame.pack_forget()  # Ocultar el menú
        else:
            self.menu_frame.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)  # Mostrar el menú
            




    def capturar_frames(self):
        # Este método se ejecuta en un hilo separado para capturar frames continuamente
        while self.capturando:
            if self.cap is not None:

                ret, frame = self.cap.read()
                if ret:
                    self.frame_actual = frame
                else:
                    self.frame_actual = None
            else:
                if self.mensaje_error == False:
                    print("Error: La cámara no se inicializó correctamente.")
                    self.mensaje_error = True
                    # self.capturando = False
                    # break



    def update_frame(self):
        # Actualiza el feed de la cámara continuamente.
        # ret, frame = self.cap.read()
        if self.frame_actual is None:
            self.mostrar_pantalla_negra()
            # return 
        else:
            frame = self.frame_actual.copy()

            # Redimensionar el frame aplicando el factor de zoom
            height, width = frame.shape[:2]
            new_width = int(width * self.zoom_factor)
            new_height = int(height * self.zoom_factor)
            frame = cv2.resize(frame, (new_width, new_height))


            frame = self.rotar_imagen(frame, self.angulo)

            # self.dibujando_puntos(frame)

            

            # Convertir el frame a formato compatible con tkinter
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(frame)
            imgtk = ImageTk.PhotoImage(image=img)




            # Ajustar el tamaño del canvas y las barras de desplazamiento
            self.canvas.create_image(0, 0, anchor=tk.NW, image=imgtk)
            self.canvas.image = imgtk  # Guardar la referencia


            # Limpiar líneas anteriores en el canvas
            self.canvas.delete("lines")


            # Mensaje si se ha seleccionado un solo punto
            if len(self.points) == 1:
                cv2.putText(frame, f'{self.msg}', (30, 80), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0,0,255), 2)
                # print("Puntos: ", self.points)
                self.label_punto1.config(bg="lightgreen")


            # Dibuja líneas si se han seleccionado dos puntos
            if len(self.points) == 2:
                self.label_punto2.config(bg="lightgreen")

                self.boton_arriba['state'] = 'normal'           # Enabled button
                self.boton_abajo['state'] = 'normal'
                self.boton_izquierda['state'] = 'normal'
                self.boton_derecha['state'] = 'normal'
                self.boton_rotar_izquierda['state'] = 'normal'
                self.boton_rotar_derecha['state'] = 'normal'
                
                p1, p2 = self.points
                pixel_distance = np.linalg.norm(np.array(p2) - np.array(p1))    # Distancia en pixeles entre los dos puntos 
                x_pixel = (self.spacing * pixel_distance) / self.scale          # 3mm convertidos a pixeles
                
                #! LINEA EXTRA...!!
    #           10mm -------- pixel_distance
    #           47mm -------- x_pixel(distance)

                x_pixel_1er_linea = (self.linea_de_inicio * pixel_distance) / self.scale


                #Probando
                canvas_width = self.canvas.winfo_width()
                canvas_height = self.canvas.winfo_height()
                
                centro_x = canvas_width // 2 + self.desplaz_x
                centro_y = canvas_height // 2 + self.desplazamiento_y
                
                # Coordenadas de las líneas
                primera_linea_start = (0+self.desplaz_x , int(centro_y - (x_pixel // 2) - x_pixel_1er_linea) + self.anguloIzq)
                primera_linea_end = (canvas_width+self.desplaz_x , int(centro_y - (x_pixel // 2) - x_pixel_1er_linea) + self.anguloDer)

                line1_start = (0 + self.desplaz_x, int(centro_y - x_pixel // 2) + self.anguloIzq)
                line1_end = (canvas_width + self.desplaz_x, int(centro_y - x_pixel // 2) + self.anguloDer)
                line2_start = (0 + self.desplaz_x, int(centro_y + x_pixel // 2) + self.anguloIzq)
                line2_end = (canvas_width + self.desplaz_x, int(centro_y + x_pixel // 2) + self.anguloDer)


                #Probando con frame
                frame_height, frame_width = frame.shape[:2]
                # print(f"Tamaño del frame: {frame_width}x{frame_height}")

                centro_vertical_start = (frame_width // 2, 0)
                centro_vertical_end = (frame_width // 2, frame_height)
                centro_horizontal_start = (0, frame_height // 2)
                centro_horizontal_end = (frame_width, frame_height // 2)
            




                # Dibujar líneas en el canvas
                self.canvas.create_line(primera_linea_start, primera_linea_end, fill="red", width=3, tags="lines")

                self.canvas.create_line(line1_start, line1_end, fill="black", width=2, tags="lines")
                self.canvas.create_line(line2_start, line2_end, fill="black", width=2, tags="lines")
                self.canvas.create_line(centro_vertical_start, centro_vertical_end, fill="green", width=2, tags="lines")
                self.canvas.create_line(centro_horizontal_start, centro_horizontal_end, fill="green", width=2, tags="lines")






            # Ajustar el área desplazable del canvas
            self.canvas.config(scrollregion=self.canvas.bbox(tk.ALL))



            # Llamar nuevamente a update_frame
            self.master.after(5, self.update_frame)
            # self.update_frame()

            # self.master.bind("<Motion>", self.mostrar_coordenadas)




    def on_closing(self):
        # Detener la captura y liberar la cámara al cerrar la aplicación
        self.capturando = False  # Detener el hilo de captura
        if self.cap is not None:
            self.cap.release()
        self.master.destroy()




if __name__ == "__main__":
    root = tk.Tk()                  # Creo ventana principal "root"
    app = UmbralApp(root)           # Llamo a la clase "UmbralApp" y todo lo ejecuto dentro de root
    root.mainloop()                 # Ejecuto continuamente root 
    
    
    # Liberar la cámara cuando se cierre la ventana
    # app.cap.release()
    cv2.destroyAllWindows()