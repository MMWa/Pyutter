from typing import List, Any

from pyutter.core.primitive import ButtonWidget, Style, Function
from pyutter.widgets.layout import Container


class OutlineButton(ButtonWidget):
    def __init__(self, children: List[Any], id=None, style: Style = None, action: Function = None):
        style = style if style is not None else Style()

        super().__init__(children, id, style, action, base_style_class="btn")


class FilledButton(ButtonWidget):
    def __init__(self, children: List[Any], id=None, style: Style = None, action: Function = None):
        style = style if style is not None else Style()
        super().__init__(children, id, style, action, base_style_class="btn btn-primary")


class LinkButton(ButtonWidget):
    def __init__(self, children: List[Any], id=None, style: Style = None, action: Function = None):
        style = style if style is not None else Style()
        super().__init__(children, id, style, action, base_style_class="btn btn-link")


class ButtonGroup(Container):
    def __init__(self, children: List[Any], id=None, style: Style = None):
        style = style if style is not None else Style()
        super().__init__(children, id, style, base_style_class="btn-group")


class ButtonGroupBlock(Container):
    def __init__(self, children: List[Any], id=None, style: Style = None):
        style = style if style is not None else Style()
        super().__init__(children, id, style, base_style_class="btn-group btn-group-block")
