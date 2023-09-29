import tkinter as tk

class NoticiApp: #Creamos la clase NoticiApp
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("NoticiApp - Aplicación de Noticias en Tiempo Real")
        self.ventana.geometry("800x600")

        self.titulo_label = tk.Label(ventana, text="Noticias en Tiempo Real - Argentina", font=("Arial", 18))
        self.titulo_label.pack(pady=10)

        self.categoria_label = tk.Label(ventana, text="Selecciona una categoría:", font=("Arial", 14))
        self.categoria_label.pack(pady=5)

        categorias = ["General", "Negocios", "Entretenimiento", "Salud", "Ciencia", "Deportes", "Tecnología"] #Definimos las categorias
        self.categoria_seleccionada = tk.StringVar()
        self.categoria_seleccionada.set(categorias[0])

        self.menu_categoria = tk.OptionMenu(ventana, self.categoria_seleccionada, *categorias)
        self.menu_categoria.pack()

        self.noticias_marco = tk.Frame(ventana) 
        self.noticias_marco.pack(padx=20, pady=20, fill="both", expand=True)

        self.noticias_lista = tk.Listbox(self.noticias_marco, font=("Arial", 12), selectbackground="lightblue")
        self.noticias_lista.pack(fill="both", expand=True)

        self.cargar_noticias_btn = tk.Button(ventana, text="Cargar Noticias", font=("Arial", 14), command=self.cargar_noticias) #Botón para cargar las noticias
        self.cargar_noticias_btn.pack(pady=10)

        self.ver_noticia_btn = tk.Button(ventana, text="Ver Noticia", font=("Arial", 14), command=self.ver_noticia) #Botón para ver la noticia
        self.ver_noticia_btn.pack(pady=10)  

        self.salir_btn = tk.Button(ventana, text="Salir", font=("Arial", 14), command=ventana) #Botón para salir de la aplicación
        self.salir_btn.pack()

        self.noticias = []

    def cargar_noticias(self):
        pass

    def ver_noticia(self):
        pass

    def salir(self):
        pass

if __name__ == "__main__":
    import tkinter as tk

    ventana = tk.Tk()
    app = NoticiApp(ventana)
    ventana.mainloop()
