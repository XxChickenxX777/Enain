from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.window import Window
import math

Window.clearcolor = (0.95, 0.95, 0.95, 1)

class PiramideFactorialApp(App):
    """
    Una aplicación de Kivy que genera una pirámide de factoriales
    basada en un número ingresado por el usuario.
    """

    def build(self):
        """
        Construye la interfaz de usuario de la aplicación.
        """
        layout = BoxLayout(orientation='vertical', padding=25, spacing=15)

        titulo = Label(
            text='Pirámide de Factoriales',
            font_size=28,
            bold=True,
            color=(0.1, 0.2, 0.3, 1),
            size_hint_y=None,
            height=50
        )
        layout.add_widget(titulo)

        self.entrada_numero = TextInput(
            hint_text='Ingresa un número (máximo 11)',
            multiline=False,
            input_filter='int',
            font_size=20,
            size_hint_y=None,
            height=50,
            halign='center'
        )
        layout.add_widget(self.entrada_numero)

        boton_generar = Button(
            text='Generar Pirámide',
            font_size=22,
            size_hint_y=None,
            height=55,
            background_color=(0.2, 0.6, 0.8, 1),
            color=(1, 1, 1, 1)
        )
        boton_generar.bind(on_press=self.generar_piramide)
        layout.add_widget(boton_generar)

        self.etiqueta_resultado = Label(
            text='Aquí se mostrará el resultado',
            font_size=20,
            color=(0.1, 0.1, 0.1, 1),
            halign='center',
            valign='top'
        )
        layout.add_widget(self.etiqueta_resultado)

        return layout

    def generar_piramide(self, instance):
        """
        Esta función se ejecuta cuando se presiona el botón.
        Valida la entrada y calcula la pirámide factorial.
        """
        try:
            
            num = int(self.entrada_numero.text)

            
            if not (1 <= num <= 11):
                self.etiqueta_resultado.text = '[color=ff0000]Error:\nEl número debe estar entre 1 y 11.[/color]'
                self.etiqueta_resultado.markup = True 
                return

            
            texto_piramide = ""
            for i in range(1, num + 1):
                
                expresion = "×".join(map(str, range(1, i + 1)))
                
                
                resultado_factorial = math.factorial(i)
                
                
                texto_piramide += f"{expresion} = {resultado_factorial}\n"

            
            self.etiqueta_resultado.text = texto_piramide
            self.etiqueta_resultado.markup = False

        except ValueError:
            
            self.etiqueta_resultado.text = '[color=ff0000]Error:\nPor favor, ingresa un número válido.[/color]'
            self.etiqueta_resultado.markup = True

if __name__ == '__main__':
    PiramideFactorialApp().run()