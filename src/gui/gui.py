from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QMenu, QLabel, QProgressBar
from PyQt6.QtCore import QTimer
from PyQt6.QtGui import QGuiApplication, QAction

from config import *

class Gui():
    def __init__(self):
        self.app = QApplication([])
        self.window = QWidget()
        self.window.setWindowTitle(f"{WINDOW_TITLE}")
        
        screen = QGuiApplication.primaryScreen()
        size = screen.availableSize()
        self.screen_width = size.width()
        self.screen_height = size.height()
        self.window.resize(self.screen_width if IS_FULLSCREEN else WIDTH, self.screen_height if IS_FULLSCREEN else HEIGHT)
        
        self.main_layout = QHBoxLayout()
        
        self.create_main_selection()
        self.create_selection_info()
        self.create_start_button()
        self.create_start_info()
        self.create_progress_bar()
        
        self.window.setLayout(self.main_layout)
        self.window.show()

    def create_main_selection(self):
        self.main_selection_button = QPushButton("Selection", self.window)
        self.main_selection_button.move(MAIN_PADDING, MAIN_PADDING)
        self.main_selection_button.clicked.connect(self.toggle_menu)

    def create_selection_info(self):
        self.selection_info = QLabel("Nothing Selected", self.window)
        self.selection_info.move(2 * MAIN_PADDING + self.main_selection_button.width(), MAIN_PADDING)
        self.selection_info.resize(self.selection_info.sizeHint())

    def create_start_button(self):
        self.start_button = QPushButton("Start", self.window)
        self.start_button.move(3 * MAIN_PADDING + self.main_selection_button.width() + self.selection_info.width(), MAIN_PADDING)
        self.start_button.clicked.connect(self.start)

    def create_start_info(self):
        self.start_info = QLabel("", self.window)
        self.start_info.move(4 * MAIN_PADDING + self.main_selection_button.width() + self.selection_info.width() + self.start_button.width(), MAIN_PADDING)

    def create_progress_bar(self):
        self.progress_bar = QProgressBar(self.window)
        self.progress_bar.setRange(0, 100)
        self.progress_bar.setValue(0)
        self.progress_bar.move(MAIN_PADDING, 4 * MAIN_PADDING)
        self.progress_bar.resize(2 * (3 * MAIN_PADDING + self.main_selection_button.width() + self.selection_info.width() + self.start_button.width()), self.progress_bar.height())
        self.progress_bar.hide()

    def start(self):
        if self.selection_info.text() != "Nothing Selected":
            with open(TARGET_FILE_NAME, "w") as file:
                file.write(self.selected)
                
            self.start_info.setText(f"File '{TARGET_FILE_NAME}' created with content: {self.selected}")
            self.start_info.resize(self.start_info.sizeHint())
            self.progress_bar.show()
            self.progress_bar.setValue(0)
            
            self.start_button.setEnabled(False)
            self.main_selection_button.setEnabled(False)
            
            self.progress = 0
            self.timer = QTimer()
            self.timer.timeout.connect(self.update_progress)
            self.timer.start(110)
        else:
            self.start_info.setText("No option selected yet.")

    def update_progress(self):
        """Update the progress bar over time."""
        self.progress += 1
        self.progress_bar.setValue(self.progress)
        match self.progress:
            case 2: self.start_info.setText("Initializing Core Modules...")
            case 7: self.start_info.setText("Booting Up Virtual Environment...")
            case 12: self.start_info.setText("Loading System Dependencies...")
            case 14: self.start_info.setText("Mainframe SQL Injection...")
            case 19: self.start_info.setText("Validating Security Protocols...")
            case 20: self.start_info.setText("Compiling Neural Frameworks...")
            case 25: self.start_info.setText("Optimizing Execution Paths...")
            case 29: self.start_info.setText("Fetching Remote Resources...")
            case 33: self.start_info.setText("Decoding Data Structures...")
            case 38: self.start_info.setText("Mapping Network Topology...")
            case 39: self.start_info.setText("Calibrating Analytical Engine...")
            case 48: self.start_info.setText("Reconstructing Data Frames...")
            case 53: self.start_info.setText("Engaging Predictive Model...")
            case 58: self.start_info.setText("Executing Task Scheduler...")
            case 63: self.start_info.setText("Generating Output Streams...")
            case 63: self.start_info.setText("Recurse Looping SQL Injection Wrapper Setup...")
            case 75: self.start_info.setText("Refining Computational Nodes...")
            case 76: self.start_info.setText("Aligning Processing Threads...")
            case 80: self.start_info.setText("Synchronizing Cloud Instances...")
            case 83: self.start_info.setText("Finalizing Logical Deductions...")
            case 88: self.start_info.setText("Assembling Execution Plan...")
            case 92: self.start_info.setText("Performing Last System Check...")
            case 96: self.start_info.setText("Wrapping Up Operations...")
            case 97: self.start_info.setText("Almost There")
        
        if self.progress >= 100:
            self.timer.stop()
            self.start_button.setEnabled(True)
            self.main_selection_button.setEnabled(True)
            self.progress_bar.hide()
            self.clear()

    def clear(self):
        """Hide all UI elements after process finishes."""
        self.selection_info.hide()
        self.main_selection_button.hide()
        self.start_button.hide()
        self.start_info.hide()
        
        self.setup_main_ui()
    
    def setup_main_ui(self):
        self.quit_button = QPushButton("Quit", self.window)
        self.quit_button.move(self.screen_width - MAIN_PADDING, self.screen_height - MAIN_PADDING)
        self.quit_button.isEnabled()
    
    
    def toggle_menu(self):
        menu = QMenu(self.main_selection_button)

        for name in SELECTION:
            action = QAction(SELECTION_TRANSLATION.get(name, name), self.main_selection_button)
            action.triggered.connect(lambda checked, n=name: self.button_clicked(n))
            menu.addAction(action)

        menu.exec(self.main_selection_button.mapToGlobal(self.main_selection_button.rect().bottomLeft()))

    def button_clicked(self, name):
        self.selected = name
        self.selection_info.setText(f"Selected: {SELECTION_TRANSLATION.get(name, name)}")

    def run(self):
        self.app.exec()

if __name__ == "__main__":
    app = Gui()
    app.run()
