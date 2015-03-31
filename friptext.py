import sys
from PyQt5.QtWidgets import (QWidget, QPushButton, QMessageBox,
                             QTextEdit, QGridLayout, QApplication)


class MainWindows(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 按钮
        self.frip_button = QPushButton('反转', self)
        self.frip_text = QTextEdit(self)
        self.frip_options = QPushButton('关于', self)
        self.frip_horizion = QPushButton('竖转', self)
        self.frip_backup = QPushButton('复原', self)
        self.frip_button.setStyleSheet('font-size: 10pt;')
        self.frip_horizion.setStyleSheet('font-size: 10pt;')
        self.frip_backup.setStyleSheet('font-size: 10pt;')
        self.frip_options.setStyleSheet('font-size: 10pt;')
        self.frip_text.setStyleSheet('font-size: 11pt;')
        # 备份
        self.backup = ''
        # 布局
        frip_grid = QGridLayout()
        frip_grid.setSpacing(10)
        frip_grid.addWidget(self.frip_text, 1, 0, 5, 1)
        frip_grid.addWidget(self.frip_button, 1, 1)
        frip_grid.addWidget(self.frip_horizion, 2, 1)
        frip_grid.addWidget(self.frip_backup, 3, 1)
        frip_grid.addWidget(self.frip_options, 4, 1)
        # Clipboard
        # self.frip_board = QApplication.clipboard()
        # 按钮信号映射
        self.frip_button.clicked.connect(self.frip_method)
        self.frip_horizion.clicked.connect(self.horizon)
        self.frip_options.clicked.connect(self.about)
        self.frip_backup.clicked.connect(self.makebackup)
        # 应用布局和规划窗口
        self.setLayout(frip_grid)
        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('fripText')
        self.show()

    def frip_method(self):
        # 反转文本框里的内容
        self.before = self.frip_text.toPlainText()
        transfer = self.before[::-1].split('\n')
        after = ''
        for i in transfer[::-1]:
            after = after + i + '\n'
        self.frip_text.setText(after[:-1])

    def horizon(self):
        # 垂直文本框里的内容
        self.before = self.frip_text.toPlainText()
        line = self.before.split('\n')[::-1]
        long = 0
        # 获取最长文本长度,并以此为横排的行数
        for l in line:
            if long <= len(l):
                long = len(l)
        # 查询内部有没有半角字符，有的话后面加上空格保持对齐
        chard = "abcdefghijklmnopqrstuvwxyz;'[]{}\|,./<>?1234567890-=`!@#$%^&*()_+"
        after = ''
        # 字符反转，颠倒行和列
        for i in range(long):
            out = ''
            for j in range(0, len(line)):
                if i < len(line[j]):
                    if line[j][i] in chard:
                        out += line[j][i] + ' '
                    else:
                        out += line[j][i]
                else:
                    out += '  '
            out += '\n'
            after += out
        self.frip_text.setText(after)

    def makebackup(self):
        # 复原原本的文本内容
        self.frip_text.setText(self.before)

    def about(self):
        QMessageBox.about(self, '关于 fripText',
                          '反转字符串的弱智程序\n\nplumz.me')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    fripapp = MainWindows()
    sys.exit(app.exec_())
