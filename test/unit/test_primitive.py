import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from pyutter.core.primitive import Text, ButtonWidget, Function


def test_widget():
    x = Text()
    props = x()
    assert isinstance(props, dict)
    assert props['tag'] == 'plain'


def test_text():
    x = Text()
    computed_properties = x.__properties__()
    assert computed_properties['tag'] == "plain"
    assert computed_properties['traits']["render"] == 1
    assert "text" in computed_properties['traits'].keys()
    print(x.__properties__())
    print(x.__properties__().keys())


def test_button_widget_with_action():
    x = ButtonWidget([])
    computed_properties = x.__properties__()
    assert computed_properties['traits']["render"] == 1
    assert "actionId" not in computed_properties['traits'].keys()
    assert "actionVars" not in computed_properties['traits'].keys()
    assert "actionEvent" not in computed_properties['traits'].keys()


def test_action_button_widget():
    mock_callable = lambda: 4
    f = Function(mock_callable)
    x = ButtonWidget([], action=f)
    computed_properties = x.__properties__()

    props = x()
    assert isinstance(props, dict)
    assert computed_properties['traits']["render"] == 1
    assert "actionId" in computed_properties['traits'].keys()
    assert computed_properties['traits']["actionId"] == f.id
    assert "actionVars" in computed_properties['traits'].keys()
    assert "actionEvent" in computed_properties['traits'].keys()


def test_textwidget_child_handling():
    from pyutter.core.primitive import TextWidget, Text, State

    widget_child = Text(text="inside")
    state_child = State(name="count", value=1)
    tw = TextWidget(child=[widget_child, state_child, "raw"])

    # existing Widget and State instances should not be wrapped in Text
    assert tw.child[0] is widget_child
    assert tw.child[1] is state_child
    assert isinstance(tw.child[2], Text)
