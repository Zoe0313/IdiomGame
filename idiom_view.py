import sys
from PyQt5.QtWidgets import QApplication,QMainWindow
from idiom_ui import Ui_Form
from idiom_game import *

class IdiomView(QMainWindow,Ui_Form):
    def __init__(self,*args,**kwargs):
        super(IdiomView, self).__init__(*args,**kwargs)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.user_answer)
        self.cancelButton.clicked.connect(self.user_cancel)
        self.init_game()

    def init_game(self):
        readall()
        self.pc_ask()

    def pc_ask(self):
        t = pc_question()
        if t:
            memory.add(t)
            self.set_info("电脑出题:%s"%t)
            self.set_pc_question(t)
            self.pushButton.setEnabled(True)
            self.lineEdit.setText("")
        else:
            self.set_warning("题库已空")
            self.pushButton.setEnabled(False)

    def pc_reply(self,idiom):
        p = pc_answer(idiom)
        if p:
            memory.add(p)
            self.set_info("电脑接龙:%s"%p)
            self.set_pc_question(p)
            self.pushButton.setEnabled(True)
            self.lineEdit.setText("")
        else:
            self.set_result("电脑没接上，你赢了！")
            self.pushButton.setEnabled(False)
            self.pc_ask()

    def pc_think(self,idiom):
        p = pc_answer(idiom)
        if p:
            memory.add(p)
            self.set_info("电脑自问自答:%s"%p)
            self.set_pc_question(p)
            self.pushButton.setEnabled(True)
            self.lineEdit.setText("")
        else:
            self.set_result("电脑也没接上")
            self.pushButton.setEnabled(False)
            self.pc_ask()

    def set_pc_question(self,idiom):
        self.lblIdiom.setText(idiom)

    def set_info(self,text):
        self.textBrowser.append('<font color="green">%s</font>'%text)

    def set_result(self,text):
        self.textBrowser.append('<font color="yellow">%s</font>'%text)

    def set_warning(self,text):
        self.textBrowser.append('<font color="red">%s</font>'%text)

    def set_answer(self,text):
        self.textBrowser.append('<font color="white">%s</font>'%text)

    def user_answer(self):
        p = self.lineEdit.text()
        if idiom_exists(p) == False:
            self.set_warning("该成语不存在")
            return

        if p in memory:
            self.set_warning("该成语已被使用过")
            return

        t = self.lblIdiom.text()
        if idiom_test(t, p) == False:
            self.set_warning("回答错误")
            return

        memory.add(p)
        self.set_answer(p)
        self.pc_reply(p)

    def user_cancel(self):
        t = self.lblIdiom.text()
        self.pc_think(t)

if __name__=='__main__':
    app = QApplication(sys.argv)
    widget = IdiomView()
    widget.show()
    sys.exit(app.exec_())