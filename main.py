import get_dev_ip

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.uix.widget import Widget

Builder.load_file('design.kv')

class MyLayout(Widget):
    def press(self):
        get_list = get_dev_ip.find_dev('its_ok')
        line_for_print = ''
        for i in get_list:
            line_for_print += str(i) + '   '

        self.ids.label_out.text = line_for_print

class MyApp(App):
    def build(self):
        bl = BoxLayout(orientation= 'vertical', spacing= 5, padding = [10])

        bl.add_widget(Label(text = 'lable one',
                            font_size = 35,
                            on_press= self.press_button))
        bl.add_widget( Button(text= 'Finding',
                              on_press= self.butt_find,
                              font_size= 40,
                              background_color= [0.1, 0.1, 1]))
        bl.add_widget( Button(text= 'Кнопка 2',
                              on_press= self.press_button,
                              font_size= 40,
                              background_color= [0.1, 0.1, 1]))

        return MyLayout()

    def press_button(self,instance):
        print(instance)

    def  butt_find(self, instance):
        print(get_dev_ip.find_dev('its_ok'))




def main():
    MyApp().run()

if __name__ == '__main__':
    main()