import pytest
from PySide2 import QtCore
import app

@pytest.fixture
def app(qtbot):
    test_app = app.ApplicationWindow()
    qtbot.addWidget(test_app)

    return test_app

def test_labels(app):
    assert app.label1.text() == "Enter the function equation:"
    assert app.label2.text() =="Enter the minimum value:"
    assert app.label3.text() == "Enter the maximum value:"

@pytest.mark.parametrize("value, valid", [
    ('x%2', False), ('x^2 + x&2', False), ('x*y', False),
    ('y+3', False), ('z^2 +5 +4', False), ('x+42', True),
    ('x^2 + 2*x + 4', True), ( '3*x^4 - 3*x + 5', True),
    ('', False), 
])
def test_equationTextBox_after_click(app, qtbot, value, valid):
    app.textBox1.setText(value)
    assert app.checkTextBox1Status() == valid

@pytest.mark.parametrize("value, valid", [
    ('10' , True ) , ('-5', True ), ('0' , True ),
    ('4.5', True), ('0.22' , True), ('da', False),
    ('' , False), ('$%' , False) , ('57%' , False)
])
def test_MinValueTextBox_after_click(app, qtbot, value, valid):
    app.textBox2.setText(value)
    assert app.checkTextBox2Status() == valid


@pytest.mark.parametrize("value, valid", [
    ('10' , True ) , ('-5', True ), ('0' , True ),
    ('4.5', True), ('0.22' , True), ('da', False),
    ('' , False), ('$%' , False) , ('57%' , False)
])
def test_MaxValueTextBox_after_click(app, qtbot, value, valid):
    app.textBox3.setText(value)
    assert app.checkTextBox3Status() == valid