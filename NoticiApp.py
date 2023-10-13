import tkinter as tk
from tkinter import ttk
from ttkbootstrap import Style #Incorporamos bootstrap para dar estilo a la app
from noticia import Noticia
import webbrowser #Importamos webbrowser para abrir el buscador al clickar en "ver noticia"
from api import obtener_noticias

class NoticiApp:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("NoticiApp - Aplicación de Noticias en Tiempo Real")
        self.ventana.geometry("800x600")
        self.ventana.configure(highlightbackground="#007BFF", highlightthickness=3) #Estilo para los bordes de la ventana

        estilo = Style(theme="cosmo") #Aplicamos el estilo "cosmo"

        estilo.configure("TFrame", background="#f0f0f0") #Le damos estilo al marco

      
        estilo.configure("TLabel", font=("Helvetica", 24, "bold")) #Estilo para etiquetas

        self.titulo_label = ttk.Label(ventana, text="Noticias en Tiempo Real - Argentina", style="TLabel")
        self.titulo_label.pack(pady=20)

        estilo.configure("TLabel", font=("Helvetica", 18))
        self.categoria_label = ttk.Label(ventana, text="Selecciona una categoría:", style="TLabel")
        self.categoria_label.pack(pady=15)

        categorias = ["General", "Negocios", "Entretenimiento", "Salud", "Ciencia", "Deportes", "Tecnología"]
        self.categoria_seleccionada = tk.StringVar()
        self.categoria_seleccionada.set(categorias[0])

        
        estilo.configure("TCombobox", background="#007BFF", font=("Arial", 16), selectbackground="#007BFF", fieldbackground="white") #Estilo para el menu desplegable
        self.menu_categoria = ttk.Combobox(ventana, textvariable=self.categoria_seleccionada, values=categorias, style="TCombobox")
        self.menu_categoria.pack(pady=15)


        self.noticias_marco = ttk.Frame(ventana, style="TFrame")
        self.noticias_marco.pack(padx=20, pady=20, fill="both", expand=True)

  
        self.noticias_lista = tk.Listbox(self.noticias_marco, bg="#f0f0f0", selectbackground="#007BFF", font=("Arial", 14), bd=0, relief="flat") #Le damos estilo al listbox
        self.noticias_lista.pack(fill="both", expand=True)

        boton_frame = ttk.Frame(ventana, style="TFrame")
        boton_frame.pack(pady=20)

        
        estilo.configure("TButton", background="#007BFF", font=("Arial", 16), padding=12) #Estilo para los botones
        estilo.map("TButton", background=[("active", "#0056b3")])

        self.cargar_noticias_btn = ttk.Button(boton_frame, text="Cargar Noticias", command=self.cargar_noticias, style="TButton") #Boton de carga de noticias
        self.cargar_noticias_btn.grid(row=0, column=0, padx=20)

        self.ver_noticia_btn = ttk.Button(boton_frame, text="Ver Noticia", command=self.ver_noticia, style="TButton") #Boton para ver noticias
        self.ver_noticia_btn.grid(row=0, column=1, padx=20)

        self.salir_btn = ttk.Button(boton_frame, text="Salir", command=ventana.quit, style="TButton") #Boton para salir de la app
        self.salir_btn.grid(row=0, column=2, padx=20)

        self.noticias = []

    def cargar_noticias(self): 
        categoria_espanol = self.categoria_seleccionada.get() #Obtenemos la categoria seleccionada en español

        
        categorias = { #Mapeamos las categorías seleccionadas 
            "General": "general",
            "Negocios": "business",
            "Entretenimiento": "entertainment",
            "Salud": "health",
            "Ciencia": "science",
            "Deportes": "sports",
            "Tecnología": "technology"
        }
        categoria = categorias[categoria_espanol]

        noticias_nuevas = obtener_noticias(api_key='113757565e644e8b822c764b453ae188', categoria=categoria) #Obtenemos las noticias

        self.noticias_lista.delete(0, tk.END)  #Limpiamos la lista de noticias antes de cargar nuevas noticias

        
        self.noticias = [] #Lista para almacenar objetos Noticia

        
        for i, noticia in enumerate(noticias_nuevas): #Agregamos las nuevas noticias a la lista y a la lista de noticias interna
            titulo = noticia['title']
            descripcion = noticia['description']
            enlace = noticia['url']

            self.noticias_lista.insert(tk.END, f"{i+1}. {titulo}")
            # Almacenar objetos Noticia con título, descripción y enlace
            nueva_noticia = Noticia(titulo, descripcion, enlace)
            self.noticias.append(nueva_noticia)

        self.ventana.update()  
    def ver_noticia(self):
        
        seleccion = self.noticias_lista.curselection()

        if seleccion:
            indice = seleccion[0]
            noticia = self.noticias[indice]

            
            webbrowser.open_new(noticia.enlace) #Abrimos el enlace en el navegador web predeterminado

if __name__ == "__main__":
    import tkinter as tk

    ventana = tk.Tk()
    app = NoticiApp(ventana)
    ventana.mainloop()
