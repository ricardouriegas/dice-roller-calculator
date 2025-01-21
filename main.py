import os
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QVBoxLayout, QLabel, QSlider, QSpinBox, QScrollArea
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap
import random

class Dice:
    def __init__(self, sides):
        self.sides = sides
        self.value = random.randint(1, sides)
    
    def __str__(self):
        return os.path.join(os.path.dirname(__file__), f"images/dice{self.value}.png")

class DiceRoller1(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)
        
        self.label = QLabel("Number of Dice:")
        self.layout.addWidget(self.label)

        self.label_sum = QLabel("Sum: 0")
        self.layout.addWidget(self.label_sum)

        self.label_product = QLabel("Product: 1")
        self.layout.addWidget(self.label_product)
        
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
        
        self.setWindowTitle('Dice Roller')
        self.resize(400, 300)
        self.show()

    def draw_dice(self):
        for i in reversed(range(self.dice_layout.count())):
            self.dice_layout.itemAt(i).widget().setParent(None)

        self.dice_values = []

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

        sum, product = self.calculate()
        self.label_sum.setText(f"Sum: {sum}")
        self.label_product.setText(f"Product: {product}")
        self.label.setText(f"Number of Dice: {self.slider.value()}")

    def calculate(self):
        sum = 0
        product = 1
        for value in self.dice_values:
            sum += value
            product *= value
        return sum, product

class DiceRoller2(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)
        
        self.label = QLabel("Instructions")
        self.label.setWordWrap(True)
        self.layout.addWidget(self.label)

        self.label_sides = QLabel("Sides on a Dice:")
        self.layout.addWidget(self.label_sides)
        self.spin_box_sides = QSpinBox()
        self.spin_box_sides.setMinimum(1)
        self.spin_box_sides.setMaximum(100)
        self.spin_box_sides.setValue(6)
        self.layout.addWidget(self.spin_box_sides)

        self.label_num_dice = QLabel("Number of Dice:")
        self.layout.addWidget(self.label_num_dice)
        self.spin_box_num_dice = QSpinBox()
        self.spin_box_num_dice.setMinimum(1)
        self.spin_box_num_dice.setMaximum(100)
        self.spin_box_num_dice.setValue(1)
        self.layout.addWidget(self.spin_box_num_dice)

        self.label_dice = QLabel("Dice:")
        self.layout.addWidget(self.label_dice)

        self.label_sum = QLabel("Sum: 0")
        self.layout.addWidget(self.label_sum)

        self.label_product = QLabel("Product: 1")
        self.layout.addWidget(self.label_product)

        calculate_button = QPushButton('Start')
        calculate_button.clicked.connect(self.sum_and_product)
        self.layout.addWidget(calculate_button)

        self.setWindowTitle('Non-Conventional Dice Roller')
        self.resize(400, 300)
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
        self.label_dice.setText(f'Dices: {", ".join(str(dice.value) for dice in dices)}')

class Menu(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Menu')
        self.setGeometry(100, 100, 400, 400)
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        self.label = QLabel('Main Menu')
        self.layout.addWidget(self.label)

        self.part1_button = QPushButton('Part 1')
        self.part1_button.clicked.connect(self.run_part1)
        self.layout.addWidget(self.part1_button)

        self.part2_button = QPushButton('Part 2')
        self.part2_button.clicked.connect(self.run_part2)
        self.layout.addWidget(self.part2_button)

        self.show()

    def run_part1(self):
        self.dice_roller1 = DiceRoller1()

    def run_part2(self):
        self.dice_roller2 = DiceRoller2()

app = QApplication(sys.argv)
menu = Menu()
sys.exit(app.exec())
