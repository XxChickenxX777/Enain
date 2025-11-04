import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.graphics import Color, Rectangle

# Opcional: Establecer el tamaño de la ventana
Window.size = (300, 500)

# Colores de la calculadora (como en la foto gris/naranja)
COLOR_DISPLAY_BG = (0.2, 0.2, 0.2, 1)    # Gris Oscuro para el display
COLOR_OPERATOR = (1.0, 0.6, 0.0, 1)      # Naranja para operadores
COLOR_FUNCTION = (0.45, 0.45, 0.45, 1)   # Gris Oscuro/Dígito para AC, +/-, % (Columna 1-3)
COLOR_DIGIT = (0.45, 0.45, 0.45, 1)      # Gris Medio para dígitos

class Calculadora(BoxLayout):
    def __init__(self, **kwargs):
        super(Calculadora, self).__init__(orientation='vertical', **kwargs)
        self.calculo = ''
        self.ultimo_fue_operador = False 

        # Fondo negro para el Layout principal (simula el espacio entre botones)
        with self.canvas.before:
            Color(0, 0, 0, 1)
            self.rect = Rectangle(size=self.size, pos=self.pos)
        self.bind(size=self._update_rect, pos=self._update_rect)

        # 1. Input/Pantalla de la calculadora
        self.display = TextInput(
            text='0', 
            readonly=True, 
            font_size=60, 
            halign='right',
            background_color=COLOR_DISPLAY_BG, 
            foreground_color=(1, 1, 1, 1), 
            size_hint=(1, 0.25), 
            padding=[10, 10, 10, 10]
        )
        self.add_widget(self.display)

        # 2. Layout para los botones (Grid 5 filas x 4 columnas)
        self.botones_layout = GridLayout(
            cols=4, 
            spacing=1, # Espacio mínimo entre botones
            size_hint=(1, 0.75) 
        )
        self.add_widget(self.botones_layout)

        # Definición de los botones por filas (Primeras 4 filas)
        botones_superiores = [
            # Fila 1
            ('AC', self.limpiar, COLOR_FUNCTION), ('+/-', self.cambiar_signo, COLOR_FUNCTION), ('%', self.porcentaje, COLOR_FUNCTION), ('÷', self.agregar_operador, COLOR_OPERATOR),
            # Fila 2
            ('7', self.agregar_texto, COLOR_DIGIT), ('8', self.agregar_texto, COLOR_DIGIT), ('9', self.agregar_texto, COLOR_DIGIT), ('×', self.agregar_operador, COLOR_OPERATOR),
            # Fila 3
            ('4', self.agregar_texto, COLOR_DIGIT), ('5', self.agregar_texto, COLOR_DIGIT), ('6', self.agregar_texto, COLOR_DIGIT), ('-', self.agregar_operador, COLOR_OPERATOR),
            # Fila 4
            ('1', self.agregar_texto, COLOR_DIGIT), ('2', self.agregar_texto, COLOR_DIGIT), ('3', self.agregar_texto, COLOR_DIGIT), ('+', self.agregar_operador, COLOR_OPERATOR),
        ]

        # Creación y adición de las primeras 4 filas
        for texto, funcion, color in botones_superiores:
            boton = Button(
                text=texto, 
                font_size=30, 
                background_normal='', 
                background_color=color,
                color=(1, 1, 1, 1)
            )
            boton.bind(on_press=funcion)
            self.botones_layout.add_widget(boton)
            
        # 3. Creación y adición de la ÚLTIMA FILA (0, ., =, Espacio Negro)

        # Botón '0' (Ocupa 2 columnas)
        boton_cero = Button(
            text='0', 
            font_size=30, 
            background_normal='', 
            background_color=COLOR_DIGIT,
            color=(1, 1, 1, 1),
            size_hint_x=2 # ¡Ocupa 2 espacios!
        )
        boton_cero.bind(on_press=self.agregar_texto)
        self.botones_layout.add_widget(boton_cero)
        
        # Botón '.' (Ocupa 1 columna)
        boton_punto = Button(
            text='.', 
            font_size=30, 
            background_normal='', 
            background_color=COLOR_DIGIT,
            color=(1, 1, 1, 1),
        )
        boton_punto.bind(on_press=self.agregar_texto)
        self.botones_layout.add_widget(boton_punto)

        # Botón '=' (Ocupa 1 columna, color NARANJA)
        boton_igual = Button(
            text='=', 
            font_size=30, 
            background_normal='', 
            background_color=COLOR_OPERATOR,
            color=(1, 1, 1, 1)
        )
        boton_igual.bind(on_press=self.calcular)
        self.botones_layout.add_widget(boton_igual)
        
        # Espacio final Negro
        # Este es el truco para que el botón '=' esté centrado y el espacio final sea negro.
        # Quitamos el último widget añadido (boton_igual) para re-añadirlo junto al espacio.
        self.botones_layout.remove_widget(boton_igual)
        
        # Redefinición de la última fila para que '=' y el Espacio sean un solo elemento ancho.
        # El botón '=' ocupa 1 columna (posición 3)
        self.botones_layout.add_widget(boton_igual)

        # Espacio Negro de Relleno (Posición 4, Ocupa 1 columna)
        boton_fantasma = Button(
            text='', 
            background_color=(0, 0, 0, 1), # Negro
            background_normal='', 
            disabled=True # No debe ser interactivo
        )
        self.botones_layout.add_widget(boton_fantasma)


    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size

    # --- Lógica de la calculadora (omito los detalles ya que la lógica no ha cambiado) ---

    def agregar_texto(self, instance):
        texto = instance.text
        if self.display.text in ('0', 'Error de Sintaxis', 'División por Cero'):
            self.display.text = texto if texto != '.' else '0.'
        elif texto == '.' and '.' in self.display.text.split(self._obtener_operador_actual() or ' ')[-1]:
            return 
        else:
            self.display.text += texto
        
        self.calculo = self.display.text
        self.ultimo_fue_operador = False

    def agregar_operador(self, instance):
        operador = instance.text
        op_map = {'÷': '/', '×': '*'}
        op_python = op_map.get(operador, operador)

        if self.calculo and self.calculo[-1] not in '+-*/×÷%':
            self.display.text += operador
            self.calculo += op_python
            self.ultimo_fue_operador = True
        elif self.ultimo_fue_operador:
            self.display.text = self.display.text[:-1] + operador
            self.calculo = self.calculo[:-1] + op_python

    def limpiar(self, instance):
        self.display.text = '0'
        self.calculo = ''
        self.ultimo_fue_operador = False
    
    def cambiar_signo(self, instance):
        if self.display.text != '0':
            try:
                valor = float(self.display.text)
                nuevo_valor = -valor
                self.display.text = str(nuevo_valor)
                self.calculo = self.display.text
            except ValueError:
                pass
                
    def porcentaje(self, instance):
        try:
            valor = float(self.display.text)
            nuevo_valor = valor / 100
            self.display.text = str(nuevo_valor)
            self.calculo = self.display.text
        except ValueError:
            pass
            
    def _obtener_operador_actual(self):
        for op in ['+', '-', '*', '/']:
            if op in self.calculo:
                return op
        return None

    def calcular(self, instance):
        try:
            expresion = self.calculo.replace('×', '*').replace('÷', '/') 
            resultado = str(eval(expresion))
            
            if '.' in resultado and len(resultado.split('.')[-1]) > 10:
                resultado = f"{float(resultado):.10f}"
                
            self.display.text = resultado
            self.calculo = resultado
        except ZeroDivisionError:
            self.display.text = 'División por Cero'
            self.calculo = ''
        except Exception:
            self.display.text = 'Error de Sintaxis'
            self.calculo = ''
        self.ultimo_fue_operador = False

class CalculadoraApp(App):
    def build(self):
        self.title = 'Calculadora Kivy'
        return Calculadora()

if __name__ == '__main__':
    CalculadoraApp().run()