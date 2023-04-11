import sys
import networkx as nx
import matplotlib.pyplot as plt
import plot
import ucs
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QFileDialog, QComboBox, QLabel
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
        # TODO: Implement save image
        
        #Starting Box
        self.startingCombo = self.findChild(QComboBox, "comboBox")
        
        #Destination Box
        self.destinationCombo = self.findChild(QComboBox, "comboBox_2")
        
        #Search Route Button
        self.searchButton = self.findChild(QPushButton, "pushButton_4")
        self.searchButton.clicked.connect(self.searchRoute)
        
        #Route Solution Label
        self.route = self.findChild(QLabel, "label_3")
        
        #Distance Solution Label
        self.distance = self.findChild(QLabel, "label_4")
        
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
            
    def searchRoute(self):
        matrix = plot.parseFile(filename)
        ucsearch = ucs.UCS(matrix)
        routeSolution, distanceSolution = ucsearch.search(int(self.startingCombo.currentText()), int(self.destinationCombo.currentText()))
        self.printSolution(routeSolution)
        self.printDistance(distanceSolution)
        
    def printSolution(self, solution):
        solStr = ""
        for s in solution:
            solStr += str(s) + " "
        self.route.setText("Route: " + solStr)
        
    def printDistance(self, distance):
        self.distance.setText("Distance: " + str(distance))
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())