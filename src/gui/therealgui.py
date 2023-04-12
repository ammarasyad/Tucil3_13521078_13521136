import sys

from PyQt5.QtCore import Qt

import networkx as nx
import matplotlib.pyplot as plt
import plot
import src.algorithm.ucs as ucs
import src.algorithm.a_star as a_star

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow, QVBoxLayout, QWidget, QPushButton, QFileDialog, QComboBox, QLabel
from PyQt5 import uic

class ErrorDialog(QDialog):
    def __init__(self, e):
        super().__init__()
        self.setWindowTitle("Error")
        self.setWindowTitle("Error")
        self.setFixedSize(300, 180)
        self.layout = QVBoxLayout()

        message = QLabel("Error: " + str(e))
        message.setAlignment(Qt.AlignCenter)
        message2 = QLabel("Please choose a valid file")
        message2.setAlignment(Qt.AlignCenter)

        self.layout.addWidget(message)
        self.layout.addWidget(message2)
        self.setLayout(self.layout)
        self.show()

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
        self.saveButton.clicked.connect(self.savePlot)
        
        #Starting Box
        self.startingCombo = self.findChild(QComboBox, "comboBox")
        
        #Destination Box
        self.destinationCombo = self.findChild(QComboBox, "comboBox_2")
        
        #Algorithm Box
        self.algorithmCombo = self.findChild(QComboBox, "comboBox_3")
        
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
        try:
            graphMatrix = plot.parseFile(filename)
        except Exception as e:
            ErrorDialog(e).exec_()
            return
        self.G.add_nodes_from(plot.getNode(graphMatrix))
        self.G.add_weighted_edges_from(plot.getEdge(graphMatrix))
        self.addCombo(plot.getNode(graphMatrix))
        self.plot_graph()
        
    def savePlot(self):
        dialog = QFileDialog()
        dialog.setDefaultSuffix('png')
        file_name, _ = dialog.getSaveFileName(self, "Save Graph", "","PNG Image (*.png)")
        
        if file_name:
            self.canvas.print_png(file_name)
    
    def plot_graph(self):
        self.fig.clear()
        global pos
        pos = nx.shell_layout(self.G)
        weight = nx.get_edge_attributes(self.G, 'weight')
        nx.set_edge_attributes(self.G, values=1.0, name='zorder')
        nx.draw(self.G, pos=pos, with_labels=True, font_weight='bold', ax=self.fig.add_subplot(111))
        nx.draw_networkx_edge_labels(self.G, pos, weight)
        self.canvas.draw()
        
    def addCombo(self, nodes):
        self.startingCombo.clear()
        self.destinationCombo.clear()
        self.algorithmCombo.clear()
        self.algorithmCombo.addItem("Uniform Cost Search")
        self.algorithmCombo.addItem("A*")
        for node in nodes:
            self.startingCombo.addItem(str(node))
            self.destinationCombo.addItem(str(node))
            
    def searchRoute(self):
        matrix = plot.parseFile(filename)
        
        getRoute = False
        routeSolution = []
        if self.algorithmCombo.currentIndex() == 0:
            #Search Solution with UCS
            ucsearch = ucs.UCS(matrix)
            routeSolution, distanceSolution = ucsearch.search(int(self.startingCombo.currentText()), int(self.destinationCombo.currentText()))
            if routeSolution != []:
                getRoute = True
        else:
            #Search Solution with A*
            graph = a_star.Graph(matrix, int(self.startingCombo.currentText())-1, int(self.destinationCombo.currentText())-1)
            if graph.calculate() != None:
                arouteSolution, distanceSolution = graph.calculate()
                getRoute = True
                for node in arouteSolution:
                    routeSolution.append(int(node.label)+1)

        if getRoute:
            #Print Result                
            self.visualizeSolution(routeSolution)
            self.printSolution(routeSolution)
            self.printDistance(distanceSolution)
        else:
            self.route.setText("Route: No Solution" )
            self.distance.setText("Distance: ")
        
    def visualizeSolution(self, solution):
        for u, v in self.G.edges():
            self.G[u][v]['color'] = 'k'
                
        i = 0
        edge_solution = []
        for i in range(len(solution)-1):
            edge_solution.append([solution[i], solution[i+1]])
            
        self.fig.clear()
        weight = nx.get_edge_attributes(self.G, 'weight')
        edge_colors = ['r' if [u,v] in edge_solution else 'k' for u, v in self.G.edges]
        width = [2 if [u,v] in edge_solution else 1 for u, v in self.G.edges]
        
        nx.draw(self.G, pos=pos, with_labels=True, font_weight='bold', ax=self.fig.add_subplot(111), edge_color=edge_colors, width= width)
        nx.draw_networkx_edge_labels(self.G, pos, weight)
        self.canvas.draw()
        
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