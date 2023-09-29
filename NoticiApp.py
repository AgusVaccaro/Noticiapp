import tkinter as tk


class NoticiApp: #Creamos la clase NoticiApp
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("NoticiApp - Aplicación de Noticias en Tiempo Real")
        self.ventana.geometry("800x600")

        #Color de fondo principal
        fondo_principal = "#C6E8E3"

        self.ventana.configure(bg=fondo_principal)

        #Fuente de texto personalizada
        fuente_personalizada = ("Ginebra", 14)

        self.titulo_label = tk.Label(ventana, text="Noticias en Tiempo Real - Argentina", font=("Lucida Bright", 18), bg=fondo_principal)
        self.titulo_label.pack(pady=10)

        #Lista desplegable para seleccionar la categoría
        self.categoria_label = tk.Label(ventana, text="Selecciona una categoría:", font=fuente_personalizada, bg=fondo_principal)
        self.categoria_label.pack(pady=5)

        categorias = ["General", "Negocios", "Entretenimiento", "Salud", "Ciencia", "Deportes", "Tecnología"] #Definimos las categorias
        self.categoria_seleccionada = tk.StringVar()
        self.categoria_seleccionada.set(categorias[0])

        self.menu_categoria = tk.OptionMenu(ventana, self.categoria_seleccionada, *categorias)
        self.menu_categoria.config(font=fuente_personalizada)
        self.menu_categoria.pack()

        self.noticias_marco = tk.Frame(ventana, bg=fondo_principal)
        self.noticias_marco.pack(padx=20, pady=20, fill="both", expand=True)

        self.noticias_lista = tk.Listbox(self.noticias_marco, selectbackground="lightblue", font=fuente_personalizada)
        self.noticias_lista.pack(fill="both", expand=True)

        #Estilo personalizado para botones
        estilo_boton = {
            "font": fuente_personalizada,
            "bg": "#007ACC",  #Color de fondo del botón
            "fg": "white",  #Color de texto del botón
            "activebackground": "#005FA3",  #Color cuando se presiona el botón
            "activeforeground": "white"  #Color del texto cuando se presiona el botón
        }

        self.cargar_noticias_btn = tk.Button(ventana, text="Cargar Noticias", command=self.cargar_noticias, **estilo_boton) #Botón para cargar las noticias
        self.cargar_noticias_btn.pack(pady=10)

        self.ver_noticia_btn = tk.Button(ventana, text="Ver Noticia", command=self.ver_noticia, **estilo_boton) #Botón para ver la noticia
        self.ver_noticia_btn.pack(pady=10)

        self.salir_btn = tk.Button(ventana, text="Salir", command=ventana, **estilo_boton) #Botón para salir de la aplicación
        self.salir_btn.pack()

        self.noticias = []

    def cargar_noticias(self):
        pass

    def ver_noticia(self):
        pass

if __name__ == "__main__":
    import tkinter as tk

    ventana = tk.Tk()
    app = NoticiApp(ventana)
    ventana.mainloop()