# logging_handler.py

from PySide6.QtCore import QObject, Signal
import logging

class LogEmitter(QObject):
    log_signal = Signal(str)

class QTextBrowserHandler(logging.Handler):
    def __init__(self, emitter):
        super().__init__()
        self.emitter = emitter

    def emit(self, record):
        msg = self.format(record)
        self.emitter.log_signal.emit(msg)
