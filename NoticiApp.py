import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedStyle
from noticia import Noticia
from api import obtener_noticias
from tkinter import messagebox
import webbrowser

class NoticiApp:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("NoticiApp - Aplicación de Noticias en Tiempo Real")
        self.ventana.geometry("800x700")
        self.ventana.iconbitmap(default='NOTICIAPP.ico') #Icono de la app

        estilo = ThemedStyle(self.ventana)
        estilo.set_theme("breeze")

        banner_frame = ttk.Frame(ventana)
        banner_frame.pack(fill="x")
        banner_label = ttk.Label(banner_frame, text="NoticiApp", foreground="#007BFF", font=("Lato", 20, "bold"))
        banner_label.pack(pady=10)

        self.titulo_label = ttk.Label(ventana, text="Noticias en Tiempo Real - Argentina")
        self.titulo_label.config(font=("Lato", 32, "bold"))
        self.titulo_label.pack(pady=20)

        self.categoria_label = ttk.Label(ventana, text="Selecciona una categoría:")
        self.categoria_label.config(font=("Lato", 16))
        self.categoria_label.pack(pady=10)

        categorías = ["General", "Negocios", "Entretenimiento", "Salud", "Ciencia", "Deportes", "Tecnología"]
        self.categoria_seleccionada = tk.StringVar()
        self.categoria_seleccionada.set(categorías[0])

        self.menu_categoria = ttk.Combobox(ventana, textvariable=self.categoria_seleccionada, values=categorías)
        self.menu_categoria.config(font=("Lato", 14))
        self.menu_categoria.pack(pady=10)

        self.noticias_marco = ttk.Frame(ventana)
        self.noticias_marco.pack(padx=20, pady=20, fill="both", expand=True)

        self.noticias_lista = tk.Listbox(self.noticias_marco, bg="#f7f7f7", selectbackground="#007BFF", font=("Lato", 14), bd=0, relief="flat")
        self.noticias_lista.pack(fill="both", expand=True)

        self.noticias_lista.bind("<Double-1>", self.ver_noticia)

        boton_frame = ttk.Frame(ventana)
        boton_frame.pack(pady=20)

        estilo.configure("TButton",
                         padding=10,
                         relief="ridge",
                         font=("Lato", 16),
                         background="#007BFF",
                         foreground="#007BFF",
                         borderwidth=1
                         )

        estilo.map("TButton",
                   background=[("active", "#0056b3")],
                   relief=[("active", "sunken")],
                   borderwidth=[("active", 2)]
                   )

        self.cargar_noticias_btn = ttk.Button(boton_frame, text="Cargar Noticias", command=self.cargar_noticias)
        self.cargar_noticias_btn.pack(side="left", padx=20)

        self.ver_noticia_btn = ttk.Button(boton_frame, text="Ver Noticia", command=self.ver_noticia)
        self.ver_noticia_btn.pack(side="left", padx=20)
        
        self.salir_btn = ttk.Button(boton_frame, text="Salir", command=self.confirmar_salida)
        self.salir_btn.pack(side="left", padx=20)

        self.noticias = []

    def confirmar_salida(self):
        respuesta = messagebox.askyesno("Confirmar salida", "¿Está seguro que desea salir?")
        if respuesta:
            self.ventana.quit()

    def cargar_noticias(self):
        categoria_espanol = self.categoria_seleccionada.get()

        categorias = {
            "General": "general",
            "Negocios": "business",
            "Entretenimiento": "entertainment",
            "Salud": "health",
            "Ciencia": "science",
            "Deportes": "sports",
            "Tecnología": "technology"
        }
        categoria = categorias[categoria_espanol]

        noticias_nuevas = obtener_noticias(api_key='113757565e644e8b822c764b453ae188', categoria=categoria)

        self.noticias_lista.delete(0, tk.END)

        self.noticias = []

        for i, noticia in enumerate(noticias_nuevas):
            titulo = noticia['title']
            description = noticia.get('description')
            enlace = noticia['url']
            content = noticia['content']

            self.noticias_lista.insert(tk.END, f"{i + 1}. {titulo}")

            nueva_noticia = Noticia(titulo, description, enlace, content)
            self.noticias.append(nueva_noticia)

        self.ventana.update()

    def ver_noticia(self, event=None):
        seleccion = self.noticias_lista.curselection()

        if seleccion:
            indice = seleccion[0]
            noticia = self.noticias[indice]
            webbrowser.open_new(noticia.enlace)
        else:
            messagebox.showinfo("Mensaje", "Debes seleccionar una noticia de la lista.")

if __name__ == "__main__":
    ventana = tk.Tk()
    app = NoticiApp(ventana)
    ventana.mainloop()
