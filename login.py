from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.image import Image

class MyApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', spacing=10)

        label1 = Image(source='C:/Users/aluno.sesipaulista/Downloads/Logo-Imagen(1).jpg')

        usuario_label = Label(text="Usuário: ", font_size=30)
        usuario_input = TextInput()

        layout1 = BoxLayout(orientation="horizontal", spacing=10)
        layout1.add_widget(usuario_label)
        layout1.add_widget(usuario_input)

        senha_label = Label(text="Senha: ", font_size=30)
        senha_input = TextInput(password=True)

        layout2 = BoxLayout(orientation="horizontal", spacing=10)
        layout2.add_widget(senha_label)
        layout2.add_widget(senha_input)

        usuario_label3 = Button(text="Login", font_size=30, size_hint=(1, 0.4), halign='center')
        usuario_input3 = Button(text="Cadastro", font_size=30, size_hint=(1, 0.4), halign='center')

        layout3 = BoxLayout(orientation="horizontal", spacing=10)
        layout3.add_widget(usuario_label3)
        layout3.add_widget(usuario_input3)

        info_label = Button(text="Esqueceu a senha?", font_size=20, size_hint=(1, 0.4), halign='center')

        layout.add_widget(label1)
        layout.add_widget(layout1)
        layout.add_widget(layout2)
        layout.add_widget(layout3)
        layout.add_widget(info_label)

        return layout

if __name__ == "__main__":
    MyApp().run()
