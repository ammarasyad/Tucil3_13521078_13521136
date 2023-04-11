import sys
import networkx as nx
import matplotlib.pyplot as plt
import plot
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QFileDialog, QComboBox
from PyQt5 import uic

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # Graph
        self.G = nx.DiGraph()
        
        # Load UI
        uic.loadUi("guiiiii.ui", self)
        
        # Create a Matplotlib figure and canvas
        self.fig = plt.figure()
        self.canvas = FigureCanvas(self.fig)
        self.canvas.setStyleSheet('background-color: blue')
        
        #Choose File Button
        self.chooseButton = self.findChild(QPushButton, "pushButton")
        self.chooseButton.clicked.connect(self.browseFile)
        
        #Visualize Button
        self.visualButton = self.findChild(QPushButton, "pushButton_2")
        self.visualButton.clicked.connect(self.visualizePlot)
        
        #Save Image Button
        self.saveButton = self.findChild(QPushButton, "pushButton_3")
        
        #Starting Box
        self.startingCombo = self.findChild(QComboBox, "comboBox")
        
        #Destination Box
        self.destinationCombo = self.findChild(QComboBox, "comboBox_2")
        
        # Add the Matplotlib canvas and button to the window
        layout = self.findChild(QVBoxLayout, "verticalLayout_6")
        layout.addWidget(self.canvas)
        """ widget = self.findChild(QWidget, "verticalWidget_2")
        widget.addWidget(self.canvas)
        self.setCentralWidget(widget) """
        
    def browseFile(self):
        global filename
        filename, _ = QFileDialog.getOpenFileName(self, "Open File", "c:", "Text files (*.txt)")
        
    def visualizePlot(self):
        self.G.clear()
        graphMatrix = plot.parseFile(filename)
        self.G.add_weighted_edges_from(plot.getEdge(graphMatrix))
        self.addNode(plot.getNode(graphMatrix))
        self.plot_graph()
        
    def plot_graph(self):
        self.fig.clear()
        pos = nx.spring_layout(self.G)
        weight = nx.get_edge_attributes(self.G, 'weight')
        nx.draw(self.G, pos=pos, with_labels=True, font_weight='bold', ax=self.fig.add_subplot(111))
        nx.draw_networkx_edge_labels(self.G, pos, weight)
        self.canvas.draw()
        
    def addNode(self, nodes):
        self.startingCombo.clear()
        self.destinationCombo.clear()
        for node in nodes:
            self.startingCombo.addItem(str(node))
            self.destinationCombo.addItem(str(node))
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())