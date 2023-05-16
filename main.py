from kivymd.app import MDApp
from libs.uix.root import Root
from libs.uix.root import Root
from kivy.metrics import dp



class Demo3App(MDApp):
        mheight = dp(170)
        def build(self):
            pass
            self.root = Root()
            self.root.set_current("today")

        def __init__(self, **kwargs):
            super().__init__(**kwargs)


Demo3App().run()