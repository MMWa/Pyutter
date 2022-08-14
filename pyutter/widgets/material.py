from typing import List, Any

from pyutter.core.primitive import Style, Widget, TextWidget
from pyutter.widgets.layout import Container


class Card(Container):
    def __init__(self, children: List[Any], id=None, style: Style = None):
        style = style if style is not None else Style()
        super().__init__(children, id, style, base_style_class="card")


class CardBody(Container):
    def __init__(self, children: List[Any], id=None, style: Style = None):
        style = style if style is not None else Style()
        super().__init__(children, id, style, base_style_class="card-body")


class CardImage(Container):
    def __init__(self, children: List[Any], id=None, style: Style = None):
        style = style if style is not None else Style()
        super().__init__(children, id, style, base_style_class="card-image")


class CardHeader(Container):
    def __init__(self, children: List[Any], id=None, style: Style = None):
        style = style if style is not None else Style()
        super().__init__(children, id, style, base_style_class="card-header")


class CardFooter(Container):
    def __init__(self, children: List[Any], id=None, style: Style = None):
        style = style if style is not None else Style()
        super().__init__(children, id, style, base_style_class="card-footer")


class Chip(TextWidget):
    def __init__(self, children: List[Any], id=None, style: Style = None):
        style = style if style is not None else Style()
        super().__init__("span", children, id, style, base_style_class="chip")


# TODO: add avatar

class Toast(Container):
    def __init__(self, children: List[Any], toast_type=None, id=None, style: Style = None):
        style = style if style is not None else Style()
        # toast-primary, toast-success, toast-warning or toast-error
        toast_type = " " + toast_type if toast_type is not None else ""
        super().__init__(children, id, style, base_style_class="toast" + toast_type)


class AppBar(Widget):
    def __init__(self, children: List[Any], id=None, style: Style = None):
        style = style if style is not None else Style()
        style['box-shadow'] = '0 4px 8px 0 rgba(0,0,0,0.2)'
        style['display'] = 'flex'
        style['height'] = f'64px'
        style['width'] = f'100%'
        style['background'] = 'white'
        style['min-width'] = 'auto'
        # style['position'] = 'fixed'

        # style['box-shadow']= "var(--bs-sm)"
        super().__init__('div', children, id, style)


class Panel(Container):
    def __init__(self, children: List[Any], id=None, style: Style = None):
        style = style if style is not None else Style()
        super().__init__(children, id, style, base_style_class="panel")


class PanelHeader(Container):
    def __init__(self, children: List[Any], id=None, style: Style = None):
        style = style if style is not None else Style()
        super().__init__(children, id, style, base_style_class="panel-header")


class PanelTitle(Container):
    def __init__(self, children: List[Any], id=None, style: Style = None):
        style = style if style is not None else Style()
        super().__init__(children, id, style, base_style_class="panel-title")


class PanelNav(Container):
    def __init__(self, children: List[Any], id=None, style: Style = None):
        style = style if style is not None else Style()
        super().__init__(children, id, style, base_style_class="panel-nav")


class PanelBody(Container):
    def __init__(self, children: List[Any], id=None, style: Style = None):
        style = style if style is not None else Style()
        super().__init__(children, id, style, base_style_class="panel-body")


class PanelFooter(Container):
    def __init__(self, children: List[Any], id=None, style: Style = None):
        style = style if style is not None else Style()
        super().__init__(children, id, style, base_style_class="panel-footer")
