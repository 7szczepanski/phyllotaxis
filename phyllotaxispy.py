from kivy.graphics import *
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics.vertex_instructions import Rectangle
from kivy.graphics.instructions import CanvasBase
import random
from kivy.clock import Clock
import math
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.uix.slider import Slider

Window_WIDTH = 800
Window_HEIGHT = 800
Window.size = (Window_WIDTH, Window_HEIGHT)


class Canv_window(Widget):
    counter1 = 0
    wartosc_slider = 0
    def update1(self,dt):
        self.counter1 += 1



    def calc(self,o):
        with self.canvas:

            window_center_x = self.get_center_x()
            window_center_y = self.get_center_y()
            n = self.counter1
            #print("n = ",n)
            c = 6
            a = n * 137.5
            r = c * math.sqrt(n)
            x = r * math.cos(math.degrees(a)) + window_center_x
            y = r * math.sin(math.degrees(a)) + window_center_y


            Color((a-r) % .99, .999, .999, mode='hsv')
            if x <= Window_WIDTH+1 and y < Window_HEIGHT+1 and x >= -1 and y >= -1:
                #print(" x = ", x , "y = ", y)
                Ellipse(pos=(x, y), size=((n% 6.99999),n% 6.99999))




class PhyllotaxisApp(App):
    def build(self):
        foo = Canv_window()
        Clock.schedule_interval(foo.calc, 1 / 90)
        Clock.schedule_interval(foo.update1,1 / 90)
        return foo




if __name__ == "__main__":
    PhyllotaxisApp().run()