# Virtual Dice Roller using qt6
# the first part of the program make the sum and product of 1 to 100 dices

# the second part let u choose the sides of the dice and the number of dices


import os
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QSlider, QSpinBox, QScrollArea
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap
import random

# dice class
class Dice:
    def __init__(self, sides):
        self.sides = sides
        self.value = random.randint(1, sides)
    
    def __str__(self):
        return os.path.join(os.path.dirname(__file__), f"images/dice{self.value}.png")


# first part
class DiceRoller(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.layout = QVBoxLayout()
        
        self.label = QLabel("Number of Dice:")
        self.layout.addWidget(self.label)

        self.label = QLabel("Sum: 0")
        self.layout.addWidget(self.label)

        self.label = QLabel("Product: 1")
        self.layout.addWidget(self.label)
        
        self.slider = QSlider(Qt.Orientation.Horizontal)
        self.slider.setMinimum(1)
        self.slider.setMaximum(100)
        self.slider.setValue(1)
        self.slider.valueChanged.connect(self.draw_dice)
        self.layout.addWidget(self.slider)
        
        self.scroll_area = QScrollArea()
        self.dice_container = QWidget()
        self.dice_layout = QVBoxLayout()
        self.dice_container.setLayout(self.dice_layout)
        self.scroll_area.setWidget(self.dice_container)
        self.scroll_area.setWidgetResizable(True)
        self.layout.addWidget(self.scroll_area)
        
        self.setLayout(self.layout)
        self.setWindowTitle('Dice Roller')
        self.resize(400, 300)  # initial size of the window
        self.show()

    def draw_dice(self):
        # Clear the previous dices
        for i in reversed(range(self.dice_layout.count())):
            self.dice_layout.itemAt(i).widget().setParent(None)

        self.dice_values = []

        # Draw the new dices
        for i in range(self.slider.value()):
            dice = Dice(6)
            self.dice_values.append(dice.value)
            dice_label = QLabel()
            pixmap = QPixmap(str(dice))
            if pixmap.isNull():
                dice_label.setText(f"Failed to load image: {str(dice)}")
            else:
                dice_label.setPixmap(pixmap)
            self.dice_layout.addWidget(dice_label)

        # calculate the sum and product
        sum, product = self.calculate()
        self.layout.itemAt(1).widget().setText(f"Sum: {sum}")
        self.layout.itemAt(2).widget().setText(f"Product: {product}")

        # update the number of dices
        self.layout.itemAt(0).widget().setText(f"Number of Dice: {self.slider.value()}")

    def calculate(self):
        sum = 0
        product = 1
        for value in self.dice_values:
            sum += value
            product *= value
        return sum, product

app = QApplication(sys.argv)
window = DiceRoller()
window.show()
sys.exit(app.exec())
