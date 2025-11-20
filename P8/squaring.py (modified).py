from kivy.app import App
from kivy.lang import Builder

KV_FILE = 'squaring.kv'


class SquaringApp(App):
    def build(self):
        self.title = 'Square Number'
        self.root = Builder.load_file(KV_FILE)
        return self.root

    def handle_calculate(self, text_value: str):
        """Calculate n^2 from the provided text, with safe conversion."""
        try:
            n = float(text_value)
        except (TypeError, ValueError):
            n = 0.0
        result = n ** 2
        self.root.ids.output_label.text = str(result)


if __name__ == '__main__':
    SquaringApp().run()