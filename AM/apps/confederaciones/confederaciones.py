import tkinter as tk
from tkinter import ttk, messagebox

class FutbolistaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Información de Futbolistas - Confederaciones Mundiales")
        self.root.geometry("800x600")
        self.root.configure(bg="#1a472a")
        
        # Datos de jugadores por confederación
        self.datos_jugadores = self.crear_datos_jugadores()
        
        # Crear menú
        self.crear_menu()
        
        # Crear interfaz principal
        self.crear_interfaz_principal()
    
    def crear_datos_jugadores(self):
        """Estructura de datos con información de jugadores"""
        return {
            "CONCACAF": {
                "paises": ["México", "Estados Unidos", "Canadá"],
                "jugadores": {
                    "México": [
                        {"nombre": "Hirving Lozano", "edad": 29, "posicion": "Delantero", 
                         "club": "PSV Eindhoven", "goles": 15, "partidos": 68},
                        {"nombre": "Guillermo Ochoa", "edad": 39, "posicion": "Portero", 
                         "club": "Salernitana", "goles": 0, "partidos": 150},
                        {"nombre": "Edson Álvarez", "edad": 27, "posicion": "Mediocampista", 
                         "club": "West Ham", "goles": 3, "partidos": 85}
                    ],
                    "Estados Unidos": [
                        {"nombre": "Christian Pulisic", "edad": 26, "posicion": "Delantero", 
                         "club": "AC Milan", "goles": 31, "partidos": 73},
                        {"nombre": "Weston McKennie", "edad": 26, "posicion": "Mediocampista", 
                         "club": "Juventus", "goles": 13, "partidos": 58},
                        {"nombre": "Tyler Adams", "edad": 26, "posicion": "Mediocampista", 
                         "club": "Bournemouth", "goles": 1, "partidos": 42}
                    ],
                    "Canadá": [
                        {"nombre": "Alphonso Davies", "edad": 24, "posicion": "Defensa", 
                         "club": "Bayern Munich", "goles": 2, "partidos": 52},
                        {"nombre": "Jonathan David", "edad": 25, "posicion": "Delantero", 
                         "club": "Lille", "goles": 28, "partidos": 56},
                        {"nombre": "Cyle Larin", "edad": 29, "posicion": "Delantero", 
                         "club": "Mallorca", "goles": 29, "partidos": 72}
                    ]
                }
            },
            "CONMEBOL": {
                "paises": ["Argentina", "Brasil", "Uruguay"],
                "jugadores": {
                    "Argentina": [
                        {"nombre": "Lionel Messi", "edad": 37, "posicion": "Delantero", 
                         "club": "Inter Miami", "goles": 112, "partidos": 191},
                        {"nombre": "Emiliano Martínez", "edad": 32, "posicion": "Portero", 
                         "club": "Aston Villa", "goles": 0, "partidos": 45},
                        {"nombre": "Julián Álvarez", "edad": 24, "posicion": "Delantero", 
                         "club": "Atlético Madrid", "goles": 9, "partidos": 36}
                    ],
                    "Brasil": [
                        {"nombre": "Vinícius Jr", "edad": 24, "posicion": "Delantero", 
                         "club": "Real Madrid", "goles": 6, "partidos": 38},
                        {"nombre": "Alisson Becker", "edad": 32, "posicion": "Portero", 
                         "club": "Liverpool", "goles": 0, "partidos": 62},
                        {"nombre": "Rodrygo", "edad": 24, "posicion": "Delantero", 
                         "club": "Real Madrid", "goles": 4, "partidos": 26}
                    ],
                    "Uruguay": [
                        {"nombre": "Luis Suárez", "edad": 37, "posicion": "Delantero", 
                         "club": "Inter Miami", "goles": 69, "partidos": 142},
                        {"nombre": "Federico Valverde", "edad": 26, "posicion": "Mediocampista", 
                         "club": "Real Madrid", "goles": 9, "partidos": 67},
                        {"nombre": "Darwin Núñez", "edad": 25, "posicion": "Delantero", 
                         "club": "Liverpool", "goles": 13, "partidos": 32}
                    ]
                }
            },
            "UEFA": {
                "paises": ["España", "Francia", "Inglaterra"],
                "jugadores": {
                    "España": [
                        {"nombre": "Pedri", "edad": 22, "posicion": "Mediocampista", 
                         "club": "Barcelona", "goles": 4, "partidos": 29},
                        {"nombre": "Dani Olmo", "edad": 26, "posicion": "Mediocampista", 
                         "club": "Barcelona", "goles": 10, "partidos": 43},
                        {"nombre": "Rodri", "edad": 28, "posicion": "Mediocampista", 
                         "club": "Manchester City", "goles": 3, "partidos": 59}
                    ],
                    "Francia": [
                        {"nombre": "Kylian Mbappé", "edad": 26, "posicion": "Delantero", 
                         "club": "Real Madrid", "goles": 48, "partidos": 86},
                        {"nombre": "Antoine Griezmann", "edad": 33, "posicion": "Delantero", 
                         "club": "Atlético Madrid", "goles": 44, "partidos": 137},
                        {"nombre": "N'Golo Kanté", "edad": 33, "posicion": "Mediocampista", 
                         "club": "Al-Ittihad", "goles": 2, "partidos": 53}
                    ],
                    "Inglaterra": [
                        {"nombre": "Harry Kane", "edad": 31, "posicion": "Delantero", 
                         "club": "Bayern Munich", "goles": 68, "partidos": 103},
                        {"nombre": "Jude Bellingham", "edad": 21, "posicion": "Mediocampista", 
                         "club": "Real Madrid", "goles": 6, "partidos": 36},
                        {"nombre": "Bukayo Saka", "edad": 23, "posicion": "Delantero", 
                         "club": "Arsenal", "goles": 12, "partidos": 43}
                    ]
                }
            },
            "CAF": {
                "paises": ["Senegal", "Egipto", "Marruecos"],
                "jugadores": {
                    "Senegal": [
                        {"nombre": "Sadio Mané", "edad": 32, "posicion": "Delantero", 
                         "club": "Al-Nassr", "goles": 41, "partidos": 103},
                        {"nombre": "Édouard Mendy", "edad": 32, "posicion": "Portero", 
                         "club": "Al-Ahli", "goles": 0, "partidos": 35},
                        {"nombre": "Kalidou Koulibaly", "edad": 33, "posicion": "Defensa", 
                         "club": "Al-Hilal", "goles": 3, "partidos": 78}
                    ],
                    "Egipto": [
                        {"nombre": "Mohamed Salah", "edad": 32, "posicion": "Delantero", 
                         "club": "Liverpool", "goles": 57, "partidos": 99},
                        {"nombre": "Mohamed Elneny", "edad": 32, "posicion": "Mediocampista", 
                         "club": "Arsenal", "goles": 6, "partidos": 118},
                        {"nombre": "Omar Marmoush", "edad": 25, "posicion": "Delantero", 
                         "club": "Eintracht Frankfurt", "goles": 5, "partidos": 33}
                    ],
                    "Marruecos": [
                        {"nombre": "Achraf Hakimi", "edad": 26, "posicion": "Defensa", 
                         "club": "PSG", "goles": 3, "partidos": 77},
                        {"nombre": "Hakim Ziyech", "edad": 31, "posicion": "Mediocampista", 
                         "club": "Galatasaray", "goles": 19, "partidos": 58},
                        {"nombre": "Youssef En-Nesyri", "edad": 27, "posicion": "Delantero", 
                         "club": "Fenerbahçe", "goles": 21, "partidos": 62}
                    ]
                }
            },
            "AFC": {
                "paises": ["Japón", "Corea del Sur", "Australia"],
                "jugadores": {
                    "Japón": [
                        {"nombre": "Takefusa Kubo", "edad": 23, "posicion": "Mediocampista", 
                         "club": "Real Sociedad", "goles": 9, "partidos": 42},
                        {"nombre": "Kaoru Mitoma", "edad": 27, "posicion": "Delantero", 
                         "club": "Brighton", "goles": 3, "partidos": 25},
                        {"nombre": "Wataru Endo", "edad": 31, "posicion": "Mediocampista", 
                         "club": "Liverpool", "goles": 2, "partidos": 64}
                    ],
                    "Corea del Sur": [
                        {"nombre": "Son Heung-min", "edad": 32, "posicion": "Delantero", 
                         "club": "Tottenham", "goles": 48, "partidos": 131},
                        {"nombre": "Kim Min-jae", "edad": 28, "posicion": "Defensa", 
                         "club": "Bayern Munich", "goles": 2, "partidos": 63},
                        {"nombre": "Lee Kang-in", "edad": 23, "posicion": "Mediocampista", 
                         "club": "PSG", "goles": 4, "partidos": 42}
                    ],
                    "Australia": [
                        {"nombre": "Mathew Ryan", "edad": 32, "posicion": "Portero", 
                         "club": "AZ Alkmaar", "goles": 0, "partidos": 93},
                        {"nombre": "Jackson Irvine", "edad": 31, "posicion": "Mediocampista", 
                         "club": "St. Pauli", "goles": 10, "partidos": 72},
                        {"nombre": "Martin Boyle", "edad": 32, "posicion": "Delantero", 
                         "club": "Hibernian", "goles": 7, "partidos": 35}
                    ]
                }
            }
        }
    
    def crear_menu(self):
        """Crear menú principal"""
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)
        
        # Menú de confederaciones
        menu_confederaciones = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Confederaciones", menu=menu_confederaciones)
        
        for confederacion in self.datos_jugadores.keys():
            menu_confederaciones.add_command(
                label=confederacion, 
                command=lambda c=confederacion: self.mostrar_confederacion(c)
            )
        
        menu_confederaciones.add_separator()
        menu_confederaciones.add_command(label="Salir", command=self.root.quit)
        
        # Menú de ayuda
        menu_ayuda = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Ayuda", menu=menu_ayuda)
        menu_ayuda.add_command(label="Acerca de", command=self.mostrar_acerca_de)
    
    def crear_interfaz_principal(self):
        """Crear interfaz principal con botones"""
        # Título
        titulo = tk.Label(
            self.root, 
            text="⚽ CONFEDERACIONES DE FÚTBOL MUNDIAL ⚽",
            font=("Arial", 20, "bold"),
            bg="#1a472a",
            fg="white",
            pady=20
        )
        titulo.pack()
        
        # Subtítulo
        subtitulo = tk.Label(
            self.root,
            text="Selecciona una confederación para ver información de jugadores",
            font=("Arial", 12),
            bg="#1a472a",
            fg="white"
        )
        subtitulo.pack(pady=10)
        
        # Frame para botones
        frame_botones = tk.Frame(self.root, bg="#1a472a")
        frame_botones.pack(expand=True, pady=20)
        
        # Colores para cada confederación
        colores = {
            "CONCACAF": "#FF6B35",
            "CONMEBOL": "#004E89",
            "UEFA": "#1A659E",
            "CAF": "#F77F00",
            "AFC": "#D62828"
        }
        
        # Crear botones para cada confederación
        for i, (confederacion, color) in enumerate(colores.items()):
            btn = tk.Button(
                frame_botones,
                text=confederacion,
                font=("Arial", 14, "bold"),
                bg=color,
                fg="white",
                width=15,
                height=2,
                command=lambda c=confederacion: self.mostrar_confederacion(c),
                cursor="hand2",
                relief=tk.RAISED,
                bd=3
            )
            btn.grid(row=i//3, column=i%3, padx=15, pady=15)
            
            # Efectos hover
            btn.bind("<Enter>", lambda e, b=btn: b.config(relief=tk.SUNKEN))
            btn.bind("<Leave>", lambda e, b=btn: b.config(relief=tk.RAISED))
        
        # Pie de página
        footer = tk.Label(
            self.root,
            font=("Arial", 9),
            bg="#1a472a",
            fg="lightgray"
        )
        footer.pack(side=tk.BOTTOM, pady=10)
    
    def mostrar_confederacion(self, confederacion):
        """Mostrar ventana con pestañas de países"""
        ventana = tk.Toplevel(self.root)
        ventana.title(f"Confederación {confederacion}")
        ventana.geometry("900x700")
        ventana.configure(bg="#f0f0f0")
        
        # Título de la ventana
        titulo = tk.Label(
            ventana,
            text=f"⚽ {confederacion} ⚽",
            font=("Arial", 18, "bold"),
            bg="#f0f0f0",
            fg="#1a472a"
        )
        titulo.pack(pady=10)
        
        # Crear notebook (pestañas)
        notebook = ttk.Notebook(ventana)
        notebook.pack(expand=True, fill='both', padx=10, pady=10)
        
        # Crear una pestaña por cada país
        datos = self.datos_jugadores[confederacion]
        for pais in datos["paises"]:
            frame_pais = tk.Frame(notebook, bg="white")
            notebook.add(frame_pais, text=pais)
            
            # Título del país
            titulo_pais = tk.Label(
                frame_pais,
                text=f"Jugadores de {pais}",
                font=("Arial", 16, "bold"),
                bg="white",
                fg="#1a472a"
            )
            titulo_pais.pack(pady=15)
            
            # Frame para los jugadores
            frame_jugadores = tk.Frame(frame_pais, bg="white")
            frame_jugadores.pack(expand=True, fill='both', padx=20)
            
            # Mostrar 3 jugadores
            jugadores = datos["jugadores"][pais]
            for i, jugador in enumerate(jugadores):
                self.crear_card_jugador(frame_jugadores, jugador, pais, i)
    
    def crear_card_jugador(self, parent, jugador, pais, index):
        """Crear tarjeta de jugador"""
        # Frame principal del jugador
        frame = tk.Frame(parent, bg="#e8f4f8", relief=tk.RAISED, bd=2)
        frame.pack(pady=10, padx=10, fill='x')
        
        # Frame interno
        frame_contenido = tk.Frame(frame, bg="#e8f4f8")
        frame_contenido.pack(padx=15, pady=15, fill='x')
        
        # Imagen simulada (círculo con iniciales)
        canvas = tk.Canvas(frame_contenido, width=80, height=80, 
                          bg="#1a472a", highlightthickness=0)
        canvas.grid(row=0, column=0, rowspan=3, padx=10)
        
        # Dibujar círculo
        canvas.create_oval(10, 10, 70, 70, fill="#4a7c59", outline="white", width=3)
        
        # Iniciales
        iniciales = "".join([n[0] for n in jugador["nombre"].split()[:2]])
        canvas.create_text(40, 40, text=iniciales, font=("Arial", 20, "bold"), 
                          fill="white")
        
        # Hacer clickeable el canvas
        canvas.bind("<Button-1>", lambda e: self.mostrar_detalles_jugador(jugador, pais))
        canvas.bind("<Enter>", lambda e: canvas.config(cursor="hand2"))
        canvas.bind("<Leave>", lambda e: canvas.config(cursor=""))
        
        # Nombre (clickeable)
        nombre_label = tk.Label(
            frame_contenido,
            text=jugador["nombre"],
            font=("Arial", 14, "bold"),
            bg="#e8f4f8",
            fg="#1a472a",
            cursor="hand2"
        )
        nombre_label.grid(row=0, column=1, sticky='w', padx=10)
        nombre_label.bind("<Button-1>", lambda e: self.mostrar_detalles_jugador(jugador, pais))
        
        # Posición y club
        info_label = tk.Label(
            frame_contenido,
            text=f"{jugador['posicion']} | {jugador['club']}",
            font=("Arial", 11),
            bg="#e8f4f8",
            fg="#555"
        )
        info_label.grid(row=1, column=1, sticky='w', padx=10)
        
        # Estadísticas básicas
        stats_label = tk.Label(
            frame_contenido,
            text=f"Edad: {jugador['edad']} años | Partidos: {jugador['partidos']} | Goles: {jugador['goles']}",
            font=("Arial", 10),
            bg="#e8f4f8",
            fg="#777"
        )
        stats_label.grid(row=2, column=1, sticky='w', padx=10)
        
        # Botón ver detalles
        btn_detalles = tk.Button(
            frame_contenido,
            text="Ver Detalles",
            font=("Arial", 10),
            bg="#1a472a",
            fg="white",
            command=lambda: self.mostrar_detalles_jugador(jugador, pais),
            cursor="hand2"
        )
        btn_detalles.grid(row=0, column=2, rowspan=3, padx=20)
    
    def mostrar_detalles_jugador(self, jugador, pais):
        """Mostrar ventana con detalles completos del jugador"""
        ventana_detalles = tk.Toplevel(self.root)
        ventana_detalles.title(f"Detalles - {jugador['nombre']}")
        ventana_detalles.geometry("500x400")
        ventana_detalles.configure(bg="white")
        
        # Frame principal
        frame_principal = tk.Frame(ventana_detalles, bg="white")
        frame_principal.pack(expand=True, fill='both', padx=30, pady=30)
        
        # Imagen más grande
        canvas = tk.Canvas(frame_principal, width=120, height=120, 
                          bg="white", highlightthickness=0)
        canvas.pack(pady=10)
        canvas.create_oval(10, 10, 110, 110, fill="#1a472a", outline="#4a7c59", width=4)
        iniciales = "".join([n[0] for n in jugador["nombre"].split()[:2]])
        canvas.create_text(60, 60, text=iniciales, font=("Arial", 30, "bold"), 
                          fill="white")
        
        # Nombre
        tk.Label(
            frame_principal,
            text=jugador['nombre'],
            font=("Arial", 20, "bold"),
            bg="white",
            fg="#1a472a"
        ).pack(pady=10)
        
        # País
        tk.Label(
            frame_principal,
            text=f"🏴 {pais}",
            font=("Arial", 12),
            bg="white",
            fg="#555"
        ).pack()
        
        # Separador
        tk.Frame(frame_principal, height=2, bg="#ddd").pack(fill='x', pady=15)
        
        # Información detallada
        info_frame = tk.Frame(frame_principal, bg="white")
        info_frame.pack(pady=10)
        
        detalles = [
            ("Edad:", f"{jugador['edad']} años"),
            ("Posición:", jugador['posicion']),
            ("Club Actual:", jugador['club']),
            ("Partidos Jugados:", jugador['partidos']),
            ("Goles Anotados:", jugador['goles'])
        ]
        
        for i, (etiqueta, valor) in enumerate(detalles):
            frame_fila = tk.Frame(info_frame, bg="white")
            frame_fila.pack(fill='x', pady=5)
            
            tk.Label(
                frame_fila,
                text=etiqueta,
                font=("Arial", 11, "bold"),
                bg="white",
                fg="#1a472a",
                width=18,
                anchor='w'
            ).pack(side=tk.LEFT)
            
            tk.Label(
                frame_fila,
                text=valor,
                font=("Arial", 11),
                bg="white",
                fg="#555",
                anchor='w'
            ).pack(side=tk.LEFT)
        
        # Botón cerrar
        tk.Button(
            frame_principal,
            text="Cerrar",
            font=("Arial", 11),
            bg="#1a472a",
            fg="white",
            command=ventana_detalles.destroy,
            cursor="hand2",
            width=15
        ).pack(pady=20)
    
    def mostrar_acerca_de(self):
        """Mostrar información acerca del programa"""
        messagebox.showinfo(
            "Acerca de",
            "Sistema de Información de Futbolistas\n\n"
            "Versión 1.0\n\n"
            "Este programa muestra información de jugadores\n"
            "de las cinco confederaciones de fútbol mundial:\n"
            "• CONCACAF\n"
            "• CONMEBOL\n"
            "• UEFA\n"
            "• CAF\n"
            "• AFC\n\n"
            "© 2024 Todos los derechos reservados"
        )

# Crear y ejecutar la aplicación
if __name__ == "__main__":
    root = tk.Tk()
    app = FutbolistaApp(root)
    root.mainloop()