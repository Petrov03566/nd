import add_Working,delete_defective
from PyQt5.QtWidgets import *
from PyQt5.QtSql import *

class WorkingAdd(add_Working.Add_Working):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.add_work_button)
        
    
    def add_work_button(self):
        if self.lineEdit.text() and self.lineEdit_2.text():
            query_wk = QSqlQuery()
            query_wk.exec(f"INSERT INTO public.Working (id, name_printer3,place_establishment) VALUES  ('{self.lineEdit.text()}', '{self.lineEdit_2.text()}',')")


class DeleteWork(delete_defective.Delete_Defective):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.pB_no_defective.clicked.connect(self.no_delete_button)

    def no_delete_button(self):
        self.close
    

    