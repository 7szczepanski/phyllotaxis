from kivy.graphics import *
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ListProperty, ObjectProperty
from kivy.graphics.vertex_instructions import (Rectangle, Ellipse, Line)
import math

n = 0
c = 5


class PhyllotaxiswApp(App):
    def build(self):
        return boxOustide()


class boxOustide(BoxLayout):
    def __init__(self):
        super(boxOustide, self).__init__()
        with self.canvas:
            global n
            global c
            window_center_x = self.get_center_x() * 8
            window_center_y = self.get_center_y() * 6
            post = c * 3500
            for i in range(15200):
                a = n * 137.5
                r = c * math.sqrt(n)
                x = r * math.cos(a) + window_center_x
                y = r * math.sin(a) + window_center_y
                Color(n % .999, .999, .999, mode='hsv')
                Ellipse(pos=(x, y), size=(5, 5))
                n += 1


if __name__ == "__main__":
    PhyllotaxiswApp().run()