from PySide6.QtGui import QAction, QKeySequence
from PySide6.QtWidgets import QMainWindow


class MainWindow(QMainWindow):
    def __init__(self, widget) -> None:
        super().__init__()
        self.setWindowTitle("Earthquakes information")
        self.setCentralWidget(widget)
        
        # Define menus
        self.menu = self.menuBar()
        self.file_menu = self.menu.addMenu("File")

        # Define actions
        exit_action = QAction("Exit", self)
        exit_action.setShortcut(QKeySequence.Quit)  # type: ignore
        exit_action.triggered.connect(self.close)

        self.file_menu.addAction(exit_action)

        # Status bar
        self.status = self.statusBar()
        self.status.showMessage("Data loaded and plotted")

        # Set window dimension
        geometry = self.screen().availableGeometry()
        self.setFixedSize(
            geometry.width() * 0.8, geometry.height() * 0.7  # type: ignore
        )
