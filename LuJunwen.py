class Monitor:
    """
    A class to represent a monitor with a specific model, width, and height.

    Attributes:
    ----------
    model : str
        The model of the monitor.
    width : int
        The width of the monitor in pixels.
    height : int
        The height of the monitor in pixels.
    """

    def __init__(self, model: str, width: int, height: int):
        """
        Initializes a new Monitor instance.

        Parameters:
        ----------
        model : str
            The model of the monitor.
        width : int
            The width of the monitor in pixels.
        height : int
            The height of the monitor in pixels.
        """
        self.model = model
        self.width = width
        self.height = height

    def get_resolution(self) -> tuple:

        return self.width, self.height

    def get_total_pixels(self) -> int:

        return self.width * self.height
