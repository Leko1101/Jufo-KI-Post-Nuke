from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QMenu, QLabel

from PyQt6.QtGui import QGuiApplication, QAction
from config import *



class Gui():
    def __init__(self):
        self.app = QApplication([])
        self.window = QWidget()
        self.window.setWindowTitle(f"{WINDOW_TITLE}")
        
        screen = QGuiApplication.primaryScreen()
        size = screen.availableSize()
        screen_width = size.width()
        screen_height = size.height()
        self.window.resize(screen_width if IS_FULLSCREEN else WIDTH, screen_height if IS_FULLSCREEN else HEIGHT)
        
        
        self.main_layout = QHBoxLayout()
        
        self.create_main_selection()
        self.create_selection_info()
        self.create_start_button()
        self.create_start_info()
        
        self.window.setLayout(self.main_layout)
        self.window.show()
    
    def create_main_selection(self) -> None:
        self.main_selection_button = QPushButton("Selection", self.window)
        self.main_selection_button.move(MAIN_PADDING, MAIN_PADDING)
        self.main_selection_button.clicked.connect(lambda: self.toggle_menu())
    
    def create_selection_info(self) -> None:
        self.selection_info = QLabel("Nothing Selected", self.window)
        self.selection_info.move(2*MAIN_PADDING + self.main_selection_button.width(), MAIN_PADDING)
        self.selection_info.resize(self.selection_info.sizeHint())
    
    def create_start_button(self) -> None:
        self.start_button = QPushButton("Start", self.window)
        self.start_button.move(3*MAIN_PADDING + self.main_selection_button.width() + self.selection_info.width() , MAIN_PADDING)
        self.start_button.clicked.connect(lambda: self.start())
    
    def create_start_info(self) -> None:
        self.start_info = QLabel("", self.window)
        self.start_info.move(4*MAIN_PADDING + self.main_selection_button.width() + self.selection_info.width() + self.start_button.width(), MAIN_PADDING)
        self.start_info.resize(self.start_info.sizeHint())
    
    def start(self):
        if self.selection_info.text() != "Nothing Selected":
            with open(TARGET_FILE_NAME, "w") as file:
                file.write(self.selected)
            
            self.start_info.setText(f"File '{TARGET_FILE_NAME}' created with content: {self.selected}")
            self.start_info.resize(self.start_info.sizeHint())
        else:
            self.start_info.setText("No option selected yet.")
            self.start_info.resize(self.start_info.sizeHint())
        
        
        
    
    def toggle_menu(self) -> None:
        menu = QMenu(self.main_selection_button)
        
        for name in SELECTION:
            action = QAction(SELECTION_TRANSLATION.get(name, name), self.main_selection_button)
            action.triggered.connect(self.create_button_click_lambda(name))
            menu.addAction(action)
        
        menu.exec(self.main_selection_button.mapToGlobal(self.main_selection_button.rect().bottomLeft()))
    
    def create_button_click_lambda(self, name):
        return lambda: self.button_clicked(name)
    
    def button_clicked(self, name) -> None:
        self.selected = name
        self.selection_info.setText(f"Selected: {SELECTION_TRANSLATION.get(name, name)}")
        self.selection_info.resize(self.selection_info.sizeHint())
    
    def run(self) -> None:
        self.app.exec()

if __name__ == "__main__":
    app: Gui = Gui()
    app.run()
