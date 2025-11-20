from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

KV_FILE = 'convert_miles_km.kv'
MILES_TO_KM = 1.60934


class MilesToKmApp(App):
    km_text = StringProperty('0.0 km')

    def build(self):
        self.title = 'Convert Miles → Kilometres'
        self.root = Builder.load_file(KV_FILE)
        return self.root

    def update_result(self, miles_text: str):
        """Update km_text immediately when input changes; invalid → 0.0."""
        miles = self._to_float(miles_text)
        km = miles * MILES_TO_KM
        self.km_text = f"{km:.3f} km"

    def handle_increment(self, delta: int):
        """Increment miles box by ±1. Invalid/blank treated as 0 before adding."""
        current = self._to_int(self.root.ids.miles_input.text)
        new_val = current + int(delta)
        self.root.ids.miles_input.text = str(new_val)
        self.update_result(self.root.ids.miles_input.text)

    @staticmethod
    def _to_float(text: str) -> float:
        try:
            return float(text)
        except (TypeError, ValueError):
            return 0.0

    @staticmethod
    def _to_int(text: str) -> int:
        try:
            return int(float(text))
        except (TypeError, ValueError):
            return 0


if __name__ == '__main__':
    MilesToKmApp().run()