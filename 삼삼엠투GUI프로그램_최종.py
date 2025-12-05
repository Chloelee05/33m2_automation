import sys
import threading
import os
import logging
import datetime
from zoneinfo import ZoneInfo

from PySide6.QtWidgets import QApplication, QWidget, QMessageBox
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QVBoxLayout

from utils import get_online_time
from crawler import crawl
from logging_handler import LogEmitter, QTextBrowserHandler

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        # .ui 파일 로드 준비
        base_path = getattr(sys, '_MEIPASS', os.path.dirname(__file__))
        ui_path   = os.path.join(base_path, 'budongsan.ui')
        ui_file   = QFile(ui_path)
        if not ui_file.open(QFile.ReadOnly):
            raise RuntimeError(f"UI 파일을 열 수 없습니다: {ui_path}")

        # QUiLoader로 위젯 생성
        loader = QUiLoader()
        self.ui = loader.load(ui_file)       # ← 반환된 위젯을 self.ui에 저장
        ui_file.close()

        # QMainWindow 중앙 위젯으로 배치
        layout = QVBoxLayout(self)
        layout.addWidget(self.ui)
        self.setWindowTitle("삼삼엠투 크롤링 자동화 프로그램")

        # 디자이너에서 설정한 기본 크기로 창 크기 조정
        self.resize(self.ui.size())


        # 창 설정
        self.setWindowIcon(QIcon("budongsan_icon.png"))
        self.set_expiration_date()

        # 버튼 시그널 연결
        self.ui.keyword_btn.clicked.connect(self.keyword_page_open)
        self.ui.start_btn.clicked.connect(self.start_crawling)
        self.ui.reset_btn.clicked.connect(self.reset_fields)
        self.ui.quit_btn.clicked.connect(self.quit_application)

        # 기타 초기화
        self.keywords = []
        self.setup_logging()

    def set_expiration_date(self):
        expiration_date = datetime.datetime(2045, 1, 1, tzinfo=ZoneInfo("Asia/Seoul"))
        online_time = get_online_time()
        today = online_time or datetime.datetime.now(ZoneInfo("Asia/Seoul"))

        if today > expiration_date:
            self.ui.expire_date.setText("프로그램 사용 기한이 만료되었습니다.")
            self.ui.start_btn.setEnabled(False)
        else:
            remaining_days = (expiration_date - today).days
            self.ui.expire_date.setText(
                f"{expiration_date.strftime('%Y-%m-%d')} (남은 일수: {remaining_days}일)"
            )

    def setup_logging(self):
        self.log_emitter = LogEmitter()
        self.log_emitter.log_signal.connect(self.update_status)

        handler = QTextBrowserHandler(self.log_emitter)
        handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))

        logging.getLogger().addHandler(handler)
        logging.getLogger().setLevel(logging.INFO)

    def keyword_page_open(self):
        keyword_input = self.ui.keyword.text().strip()
        if not keyword_input:
            QMessageBox.warning(self, "입력 오류", "키워드를 입력해주세요.")
            return

        self.keywords = [kw.strip() for kw in keyword_input.split(',') if kw.strip()]
        if not self.keywords:
            QMessageBox.warning(self, "입력 오류", "유효한 키워드를 입력해주세요.")
            return

        QMessageBox.information(self, "키워드 설정", f"설정된 키워드: {', '.join(self.keywords)}")

    def start_crawling(self):
        if not self.keywords:
            QMessageBox.warning(self, "시작 오류", "먼저 키워드를 설정해주세요.")
            return

        self.ui.start_btn.setEnabled(False)
        self.ui.keyword_btn.setEnabled(False)
        self.ui.textBrowser.clear()

        threading.Thread(target=self.run_crawling, daemon=True).start()

    def run_crawling(self):
        try:
            logging.info(f"Starting crawl for keywords: {', '.join(self.keywords)}")

            # 이미지 기본 폴더
            base_image_dir = "images"
            os.makedirs(base_image_dir, exist_ok=True)

            # 엑셀 출력 폴더
            os.makedirs("output", exist_ok=True)

            # 🚀 keyword 리스트 전체를 통째로 crawl()에 전달
            crawl(self.keywords, base_image_dir, "output")

            logging.info("모든 키워드 크롤링 완료")
            self.update_status("모든 키워드 크롤링 완료")

        except Exception as e:
            logging.error(f"Error crawling: {e}", exc_info=True)
            self.update_status("Error crawling")

        self.enable_buttons()


    def update_status(self, message):
        self.ui.textBrowser.append(message)

    def enable_buttons(self):
        self.ui.start_btn.setEnabled(True)
        self.ui.keyword_btn.setEnabled(True)

    def reset_fields(self):
        self.ui.keyword.setText('')
        self.ui.textBrowser.clear()
        self.keywords = []

    def quit_application(self):
        sys.exit()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("budongsan_icon.png"))
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
