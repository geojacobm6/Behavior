from fbs_runtime.application_context import ApplicationContext

from time_tracker import WidgetTimeTracker

import sys


class AppContext(ApplicationContext):

    def run(self):
        # window = QMainWindow()
        # window.setWindowTitle("Behavior1")
        # window.resize(500, 500)
        # layout = QVBoxLayout()
        # layout.addWidget(QPushButton('Top'))
        # layout.addWidget(QPushButton('Bottom'))
        # # window.setLayout(layout)
        # window.show()
        # gallery = WidgetGallery()
        # gallery.show()

        tt = WidgetTimeTracker()
        tt.show()

        return self.app.exec_()


if __name__ == '__main__':
    appctxt = AppContext()
    exit_code = appctxt.run()
    sys.exit(exit_code)