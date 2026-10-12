from PySide6.QtWidgets import QMainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Soundboard")
        area = self.screen().availableGeometry()
        width = area.width() * 0.65
        height = area.height() * 0.7
        self.resize(int(width), int(height))
        self.move(area.center() - self.rect().center())
        
