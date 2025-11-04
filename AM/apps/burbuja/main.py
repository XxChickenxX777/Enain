from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
KV = '''
BoxLayout:
    orientation: 'vertical'
    padding: 30
    spacing: 15

    Label:
        text: 'Introduce números separados por comas:'
        size_hint_y: None
        height: 30
        font_size: '18sp'

    TextInput:
        id: input_text
        hint_text: 'Ej: 5, -2, 10, 1'
        multiline: False
        font_size: '20sp'

    Spinner:
        id: sort_mode
        text: 'Ascendente'
        values: ['Ascendente', 'Descendente']
        size_hint_y: None
        height: '48dp'
        font_size: '18sp'


    Button:
        text: 'Ordenar Números'
        font_size: '20sp'
        size_hint_y: None
        height: '48dp'
        on_press: app.sort_numbers()

    Label:
        id: output_label
        text: 'Resultado...'
        font_size: '22sp'
        size_hint_y: 2
'''

class SortApp(App):

    def build(self):
        return Builder.load_string(KV)

    def sort_numbers(self):
        """
        Esta función se ejecuta cuando se presiona el botón.
        """
        try:
            input_str = self.root.ids.input_text.text
            mode = self.root.ids.sort_mode.text
            output_label = self.root.ids.output_label

            numbers_str_list = input_str.split(',')
            if not all(s.strip() for s in numbers_str_list if s):
                raise ValueError("Entrada inválida o vacía.")

            numbers = [int(num.strip()) for num in numbers_str_list]

            if mode == 'Ascendente':
                numbers.sort()
            else:
                numbers.sort(reverse=True)

            output_label.text = ", ".join(map(str, numbers))

        except ValueError:
            self.root.ids.output_label.text = "Error: Asegúrate de introducir solo números separados por comas."
        except Exception as e:
            self.root.ids.output_label.text = f"Ha ocurrido un error inesperado: {e}"


if __name__ == '__main__':
    SortApp().run()