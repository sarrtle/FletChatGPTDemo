"""
Color scheme for this application.
"""

# pylint: disable=missing-function-docstring
# pylint: disable=invalid-name


class ColorConfig:
    """
    Configuration class for managing color schemes.
    """

    def __init__(self, mode: str = "light"):
        self._mode = mode  # Default mode

    @property
    def mode(self):
        return self._mode

    @mode.setter
    def mode(self, mode: str):
        if mode not in ["light", "dark"]:
            raise ValueError(f"Mode must be 'light' or 'dark'. Your mode: {mode}")
        self._mode = mode

    @property
    def PRIMARY(self):
        return "#CED4DA" if self._mode == "light" else "#A7AFB6"

    @property
    def BACKGROUND_COLOR(self):
        return "#F0F8FF" if self._mode == "light" else "#16161D"

    @property
    def TEXT_COLOR_MESSAGE_BUBBLE(self):
        return "#363433" if self._mode == "light" else "#16161D"

    @property
    def TEXT_COLOR(self):
        return "#363433" if self._mode == "light" else "#d3d3d3"

    @property
    def INPUT_FIELDS_ICONS_COLOR(self):
        return "#CED4DA" if self._mode == "light" else "#A7AFB6"

    @property
    def CODE_THEME(self):
        return "paraiso-light" if self._mode == "light" else "atom-one-dark"

    @property
    def CONTAINER_COLOR(self):
        return "#CED4DA" if self._mode == "light" else "#242930"


color_config = ColorConfig()
