from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView

# Lista donde se guardarán los estudiantes
estudiantes = []

class RegistroApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        form = GridLayout(cols=2, row_force_default=True, row_default_height=40)
        self.t_boleta = TextInput(multiline=False)
        self.t_nombre = TextInput(multiline=False)
        self.t_grupo = TextInput(multiline=False)
        self.t_carrera = TextInput(multiline=False)

        form.add_widget(Label(text='Boleta:'))
        form.add_widget(self.t_boleta)
        form.add_widget(Label(text='Nombre:'))
        form.add_widget(self.t_nombre)
        form.add_widget(Label(text='Grupo:'))
        form.add_widget(self.t_grupo)
        form.add_widget(Label(text='Carrera:'))
        form.add_widget(self.t_carrera)

        self.layout.add_widget(form)

        btns = BoxLayout(size_hint_y=None, height=50, spacing=5)
        btns.add_widget(Button(text='Alta', on_press=self.alta))
        btns.add_widget(Button(text='Baja', on_press=self.baja))
        btns.add_widget(Button(text='Modificar', on_press=self.modificar))
        btns.add_widget(Button(text='Consultar', on_press=self.consultar))

        self.layout.add_widget(btns)

        self.resultado = Label(text='Aquí aparecerán los resultados.', size_hint_y=None, height=40)
        self.layout.add_widget(self.resultado)

        return self.layout

    def alta(self, instance):
        estudiante = {
            'boleta': self.t_boleta.text,
            'nombre': self.t_nombre.text,
            'grupo': self.t_grupo.text,
            'carrera': self.t_carrera.text
        }
        estudiantes.append(estudiante)
        self.resultado.text = 'Estudiante agregado correctamente.'

    def baja(self, instance):
        boleta = self.t_boleta.text
        for e in estudiantes:
            if e['boleta'] == boleta:
                estudiantes.remove(e)
                self.resultado.text = 'Estudiante eliminado.'
                return
        self.resultado.text = 'Boleta no encontrada.'

    def modificar(self, instance):
        boleta = self.t_boleta.text
        for e in estudiantes:
            if e['boleta'] == boleta:
                e['nombre'] = self.t_nombre.text
                e['grupo'] = self.t_grupo.text
                e['carrera'] = self.t_carrera.text
                self.resultado.text = 'Datos modificados.'
                return
        self.resultado.text = 'Boleta no encontrada.'

    def consultar(self, instance):
        boleta = self.t_boleta.text
        for e in estudiantes:
            if e['boleta'] == boleta:
                self.resultado.text = f"Nombre: {e['nombre']} | Grupo: {e['grupo']} | Carrera: {e['carrera']}"
                return
        self.resultado.text = 'Boleta no encontrada.'

if __name__ == '__main__':
    RegistroApp().run()
