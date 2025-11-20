from kivy.app import App
from kivy.lang import Builder




KV_FILE = 'box_layout.kv'




class BoxLayoutDemoApp(App):
def build(self):
self.title = 'BoxLayout Demo – Greeter'
self.root = Builder.load_file(KV_FILE)
return self.root


def handle_greet(self):
name = self.root.ids.input_name.text.strip()
self.root.ids.output_label.text = f"Hello {name}" if name else "Hello"


def handle_clear(self):
self.root.ids.input_name.text = ''
self.root.ids.output_label.text = ''




if __name__ == '__main__':
BoxLayoutDemoApp().run()