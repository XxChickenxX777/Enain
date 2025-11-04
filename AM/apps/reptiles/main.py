import kivy
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.utils import get_color_from_hex
from kivy.core.window import Window

Window.size = (400, 650)

kv_string = """
#:import get_color_from_hex kivy.utils.get_color_from_hex

# --- Pantalla del Menú Principal ---
<MenuScreen>:
    name: 'menu'
    BoxLayout:
        orientation: 'vertical'
        padding: 25
        spacing: 20
        canvas.before:
            Color:
                rgba: get_color_from_hex('#2C3E50') # Fondo azul oscuro
            Rectangle:
                pos: self.pos
                size: self.size
        Label:
            text: 'Órdenes de Reptiles'
            font_size: '30sp'
            size_hint_y: 0.2
            bold: True
            color: get_color_from_hex('#ECF0F1')
        Button:
            text: 'Crocodrilios'
            font_size: '22sp'
            on_press: root.manager.current = 'crocodilia'
            background_color: get_color_from_hex('#16A085') # Verde
        Button:
            text: 'Quelonios'
            font_size: '22sp'
            on_press: root.manager.current = 'testudines'
            background_color: get_color_from_hex('#27AE60') # Verde más oscuro
        Button:
            text: 'Squamatas'
            font_size: '22sp'
            on_press: root.manager.current = 'squamata'
            background_color: get_color_from_hex('#D35400') # Naranja
        Button:
            text: 'Tuátara (Rinocéfalos)'
            font_size: '22sp'
            on_press: root.manager.current = 'rhynchocephalia'
            background_color: get_color_from_hex('#8E44AD') # Morado

# --- Plantilla Base para las Pantallas de Información ---
<InfoScreenBase>:
    BoxLayout:
        orientation: 'vertical'
        padding: 15
        spacing: 10
        canvas.before:
            Color:
                rgba: get_color_from_hex('#34495E') # Fondo gris-azul
            Rectangle:
                pos: self.pos
                size: self.size
        
        # Título de la pantalla (se cambiará desde Python)
        Label:
            id: title_label
            text: 'Orden'
            font_size: '26sp'
            size_hint_y: 0.1
            bold: True
            color: get_color_from_hex('#ECF0F1')

        # Área de Scroll para el contenido
        ScrollView:
            size_hint_y: 0.8
            do_scroll_x: False
            # Usamos un GridLayout para que el scroll funcione bien
            GridLayout:
                id: content_box  # ID para añadir widgets desde Python
                cols: 1
                size_hint_y: None
                height: self.minimum_height
                padding: 10
                spacing: 20
        
        # Botón para regresar al menú
        Button:
            text: 'Volver al Menú'
            font_size: '18sp'
            size_hint_y: 0.1
            background_color: get_color_from_hex('#C0392B') # Rojo
            on_press: root.manager.current = 'menu'

# --- Definición del Widget de Información (para cada especie) ---
<InfoWidget>:
    orientation: 'vertical'
    size_hint_y: None
    height: self.minimum_height
    # Título de la especie
    Label:
        text: root.titulo
        font_size: '20sp'
        bold: True
        size_hint_y: None
        height: '30dp'
        color: get_color_from_hex('#F1C40F') # Amarillo
        halign: 'left'
        valign: 'middle'
        text_size: self.width, None
    # Información de la especie
    Label:
        text: root.info
        font_size: '16sp'
        text_size: self.width - 15, None # Para que el texto se ajuste (wrap)
        size_hint_y: None
        height: self.texture_size[1] # Ajustar altura al texto
        color: get_color_from_hex('#ECF0F1') # Blanco claro
        halign: 'left'
        valign: 'top'

# --- Reglas para las pantallas específicas ---
# Estas clases están definidas en Python, pero el KV las reconoce.
<CrocodiliaScreen>:
<TestudinesScreen>:
<SquamataScreen>:
<RhynchocephaliaScreen>:
"""


class InfoWidget(BoxLayout):
    titulo = StringProperty('')
    info = StringProperty('')
class MenuScreen(Screen):
    pass

class InfoScreenBase(Screen):
    info_cargada = False
    
    def on_enter(self):
        """ Se llama cada vez que se muestra la pantalla. """
        if not self.info_cargada:
            self.cargar_info_especies()
            self.info_cargada = True
    
    def cargar_info_especies(self):
        """ Método vacío que será sobrescrito por las clases hijas. """
        pass
    
    def agregar_especie(self, titulo, info):
        """ Función ayudante para añadir un nuevo InfoWidget. """
        widget_info = InfoWidget(titulo=titulo, info=info)
        self.ids.content_box.add_widget(widget_info)

# --- Pantallas de Especies ---

class CrocodiliaScreen(InfoScreenBase):
    def cargar_info_especies(self):
        self.ids.title_label.text = 'Orden: Crocodilia'
        self.agregar_especie('Cocodrilo del Nilo', '(Crocodylus niloticus)\nGran reptil africano, conocido por su tamaño y agresividad. Habita en ríos, lagos y marismas de agua dulce.')
        self.agregar_especie('Aligátor Americano', '(Alligator mississippiensis)\nEncontrado en el sureste de EE.UU., prefiere agua dulce. Es el reptil oficial de 3 estados (Florida, Luisiana y Misisipi).')
        self.agregar_especie('Gavial', '(Gavialis gangeticus)\nNativo de la India, reconocible por su hocico extremadamente largo y delgado, perfectamente adaptado para capturar peces.')

class TestudinesScreen(InfoScreenBase):
    def cargar_info_especies(self):
        self.ids.title_label.text = 'Orden: Testudines (Quelonios)'
        self.agregar_especie('Tortuga Verde', '(Chelonia mydas)\nGran tortuga marina herbívora. Se encuentra en mares tropicales y subtropicales de todo el mundo y migra largas distancias.')
        self.agregar_especie('Tortuga de Galápagos', '(Chelonoidis nigra)\nComplejo de especies de tortuga terrestre gigante, endémica de las Islas Galápagos. Famosa por su extraordinaria longevidad.')
        self.agregar_especie('Tortuga Laúd', '(Dermochelys coriacea)\nEs la tortuga marina más grande. Su caparazón no es óseo, sino de tejido conectivo grueso, similar al cuero. Es una gran buceadora.')

class SquamataScreen(InfoScreenBase):
    def cargar_info_especies(self):
        self.ids.title_label.text = 'Orden: Squamata (Escamosos)'
        self.agregar_especie('Dragón de Komodo', '(Varanus komodoensis)\nEl lagarto más grande del mundo, endémico de algunas islas de Indonesia. Posee una mordedura venenosa y un sentido del olfato muy desarrollado.')
        self.agregar_especie('Cobra Real', '(Ophiophagus hannah)\nLa serpiente venenosa más larga del mundo. Es única en su género (Ophiophagus), que significa "comedora de serpientes".')
        self.agregar_especie('Iguana Verde', '(Iguana iguana)\nGran lagarto arbóreo y herbívoro, muy común en América Central y del Sur. Es conocida por su "papada" y su cresta dorsal.')

class RhynchocephaliaScreen(InfoScreenBase):
    def cargar_info_especies(self):
        self.ids.title_label.text = 'Orden: Rhynchocephalia'
        self.agregar_especie('Tuátara', '(Sphenodon punctatus)\nEl único superviviente de este antiguo orden. Se considera un "fósil viviente" y es endémico de Nueva Zelanda.')
        self.agregar_especie('Características Únicas', 'No son lagartos. Poseen un "tercer ojo" (ojo parietal) sensible a la luz en la parte superior de la cabeza y una doble fila de dientes en la mandíbula superior.')
        self.agregar_especie('Estado de Conservación', 'Este orden es extremadamente vulnerable. Las poblaciones de tuátaras (solo 1 o 2 especies) están protegidas y se limitan a islas libres de depredadores introducidos.')

# --- Clase Principal de la Aplicación ---
class ReptileApp(App):
    def build(self):
        # Cargar el string KV
        Builder.load_string(kv_string)
        
        # Crear el ScreenManager
        sm = ScreenManager()
        sm.add_widget(MenuScreen(name='menu'))
        sm.add_widget(CrocodiliaScreen(name='crocodilia'))
        sm.add_widget(TestudinesScreen(name='testudines'))
        sm.add_widget(SquamataScreen(name='squamata'))
        sm.add_widget(RhynchocephaliaScreen(name='rhynchocephalia'))
        
        return sm

# --- Correr la Aplicación ---
if __name__ == '__main__':
    ReptileApp().run()