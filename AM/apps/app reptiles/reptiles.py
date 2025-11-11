import tkinter as tk
from tkinter import ttk
import webbrowser

class VentanaReptiles(tk.Toplevel):
    def __init__(self, master, titulo, especies):
        super().__init__(master)
        self.title(titulo)
        self.geometry("600x400")
        self.config(bg="#eaf2ef")

        ttk.Label(self, text=titulo, font=("Arial", 16, "bold")).pack(pady=10)

        # Crear 3 frames (widgets tipo "fragment")
        for especie in especies:
            frame = ttk.LabelFrame(self, text=especie["nombre"], padding=10)
            frame.pack(fill="x", padx=20, pady=10)

            ttk.Label(frame, text=especie["descripcion"], wraplength=500, justify="left").pack(pady=5)
            ttk.Button(frame, text="Ver más en Wikipedia",
                       command=lambda url=especie["url"]: webbrowser.open(url)).pack()


class Aplicacion(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Clasificación de Reptiles 🦎")
        self.geometry("400x300")
        self.config(bg="#dff6dd")

        # Barra de menú
        barra_menu = tk.Menu(self)
        self.config(menu=barra_menu)

        menu_reptiles = tk.Menu(barra_menu, tearoff=0)
        barra_menu.add_cascade(label="Órdenes", menu=menu_reptiles)

        # Diccionario con datos
        self.reptiles = {
            "Crocodilios": [
                {"nombre": "Cocodrilo del Nilo", "descripcion": "Uno de los reptiles más grandes de África. Habita en ríos y lagos.", "url": "https://es.wikipedia.org/wiki/Crocodylus_niloticus"},
                {"nombre": "Caimán del Orinoco", "descripcion": "Reptil endémico del río Orinoco, en peligro crítico de extinción.", "url": "https://es.wikipedia.org/wiki/Crocodylus_intermedius"},
                {"nombre": "Aligátor americano", "descripcion": "Habita en el sureste de Estados Unidos, especialmente en Florida.", "url": "https://es.wikipedia.org/wiki/Alligator_mississippiensis"}
            ],
            "Quelonios": [
                {"nombre": "Tortuga marina verde", "descripcion": "Tortuga herbívora que habita mares tropicales.", "url": "https://es.wikipedia.org/wiki/Chelonia_mydas"},
                {"nombre": "Tortuga de Galápagos", "descripcion": "Famosa por su gran tamaño y longevidad.", "url": "https://es.wikipedia.org/wiki/Chelonoidis_nigra"},
                {"nombre": "Tortuga de caja", "descripcion": "Vive en zonas terrestres de América del Norte, con caparazón abovedado.", "url": "https://es.wikipedia.org/wiki/Terrapene_carolina"}
            ],
            "Squamatas": [
                {"nombre": "Iguana verde", "descripcion": "Reptil herbívoro de América Central y del Sur.", "url": "https://es.wikipedia.org/wiki/Iguana_iguana"},
                {"nombre": "Serpiente pitón real", "descripcion": "Serpiente constrictora de África occidental.", "url": "https://es.wikipedia.org/wiki/Python_regius"},
                {"nombre": "Camaleón común", "descripcion": "Conocido por su capacidad de cambiar de color.", "url": "https://es.wikipedia.org/wiki/Chamaeleo_chamaeleon"}
            ],
            "Rinocéfalos": [
                {"nombre": "Tuatara", "descripcion": "Único representante vivo de su orden, endémico de Nueva Zelanda.", "url": "https://es.wikipedia.org/wiki/Sphenodon_punctatus"},
                {"nombre": "Tuatara del norte", "descripcion": "Subespecie que habita islas del norte de Nueva Zelanda.", "url": "https://es.wikipedia.org/wiki/Sphenodon_punctatus"},
                {"nombre": "Tuatara del sur", "descripcion": "Se encuentra en islas más frías al sur de Nueva Zelanda.", "url": "https://es.wikipedia.org/wiki/Sphenodon_guntheri"}
            ]
        }

        # Añadir opciones al menú
        for orden in self.reptiles:
            menu_reptiles.add_command(label=orden, command=lambda o=orden: self.abrir_ventana(o))

        # Botones principales
        ttk.Label(self, text="Órdenes de Reptiles", font=("Arial", 14, "bold")).pack(pady=20)
        for orden in self.reptiles:
            ttk.Button(self, text=orden, command=lambda o=orden: self.abrir_ventana(o)).pack(pady=5, ipadx=10)

    def abrir_ventana(self, orden):
        VentanaReptiles(self, orden, self.reptiles[orden])


if __name__ == "__main__":
    app = Aplicacion()
    app.mainloop()
