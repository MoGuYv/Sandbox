from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label

KV_FILE = 'dynamic_labels.kv'


class DynamicLabelsApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Data (model): you can change these names or load from a file
        self.names = [
            'Alice', 'Bob', 'Charlie', 'Dora', 'Ethan',
        ]

    def build(self):
        self.title = 'Dynamic Labels'
        self.root = Builder.load_file(KV_FILE)
        for name in self.names:
            self.root.ids.main.add_widget(Label(text=name))
        return self.root


if __name__ == '__main__':
    DynamicLabelsApp().run()