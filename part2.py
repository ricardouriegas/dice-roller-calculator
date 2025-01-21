# Virtual Dice Roller using qt6
# the first part of the program make the sum and product of 1 to 100 dices

# the second part let u choose the sides of the dice and the number of dices


import os
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QSlider, QSpinBox, QScrollArea, QSizePolicy
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap
import random

instructions = 'Use the following virtual dice roller to mimic dice that have a different number of faces from the conventional 6-faced die. The most common physical dice have 4, 6, 8, 10, 12, and 20 faces respectively, with 6-faced die comprising the majority of dice. This virtual dice roller can have any number of faces and can generate random numbers simulating a dice roll based on the number of faces and dice.'

# dice class
class Dice:
    def __init__(self, sides):
        self.sides = sides
        self.value = random.randint(1, sides)

    def getVal(self):
        return self.value
    
    def __str__(self):
        return str(self.value)


# second part
class DiceRoller(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.layout = QVBoxLayout()
        
        # label for instructions like the page
        self.label = QLabel(instructions)
        self.label.setWordWrap(True)
        self.layout.addWidget(self.label)

        # input for Sides on a Dice
        self.label_sides = QLabel("Sides on a Dice:")
        self.layout.addWidget(self.label_sides)
        self.spin_box_sides = QSpinBox()
        self.spin_box_sides.setMinimum(1)
        self.spin_box_sides.setMaximum(100)
        self.spin_box_sides.setValue(6)
        self.layout.addWidget(self.spin_box_sides)

        # input for Number of Dice
        self.label_num_dice = QLabel("Number of Dice:")
        self.layout.addWidget(self.label_num_dice)
        self.spin_box_num_dice = QSpinBox()
        self.spin_box_num_dice.setMinimum(1)
        self.spin_box_num_dice.setMaximum(100)
        self.spin_box_num_dice.setValue(1)
        self.layout.addWidget(self.spin_box_num_dice)

        # label for the dices
        self.label_dice = QLabel("Dice:")
        self.layout.addWidget(self.label_dice)

        # label for the sum of the dice
        self.label_sum = QLabel("Sum: 0")
        self.layout.addWidget(self.label_sum)

        # label for the product of the dice
        self.label_product = QLabel("Product: 1")
        self.layout.addWidget(self.label_product)

        # button to calculate the sum and product of the dice
        calculate_button = QPushButton('Start')
        calculate_button.clicked.connect(self.sum_and_product)
        self.layout.addWidget(calculate_button)

        self.setLayout(self.layout)
        self.setWindowTitle('Non-Conventional Dice Roller')
        self.resize(400, 300)  # initial size of the window
        self.show()

    def sum_and_product(self):
        sides = self.spin_box_sides.value()
        num_dice = self.spin_box_num_dice.value()

        sum_dice = 0
        product_dice = 1
        dices = []

        for _ in range(num_dice):
            dice = Dice(sides)
            dices.append(dice)
            sum_dice += dice.value
            product_dice *= dice.value
        self.label_sum.setText(f'Sum: {sum_dice}')
        self.label_product.setText(f'Product: {product_dice}')
        self.label_dice.setText(f'Dices: {", ".join(str(dice.getVal()) for dice in dices)}')



app = QApplication(sys.argv)
window = DiceRoller()
window.show()
sys.exit(app.exec())
