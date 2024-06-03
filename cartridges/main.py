
import sys 
import add_defective
import add_Working
import add_Refilled
import add_On_clade
from PyQt5 import QtCore
from PyQt5.QtSql import QSqlDatabase, QSqlQuery, QSqlTableModel
from PyQt5.QtWidgets import QWidget, QApplication,QHeaderView
from PyQt5.QtCore import *
import MainWindow 

#  ##  #########################################ГЛАВНОЕ ОКНО ################################################
class PrinterMain(MainWindow.MainPrinter):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.current_def = 0
        self.current_ref =0
        self.current_work = 0
        
        
        self.pb_add_defective.clicked.connect(self.add_Defective_button)
        self.pb_add_working.clicked.connect(self.add_Working_Button)
        self.pb_add_refueled.clicked.connect(self.add_Refilled_button)
        self.pushButton_add_on_clade.clicked.connect(self.add_Onclade_button)    
        self.tableView_working.clicked.connect(self.work_clicked)
        self.tableView_defective.clicked.connect(self.dp_clicked)
        self.tableView_defective.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableView_working.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableView_refueled.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableView_working.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        
    
        db = QSqlDatabase.addDatabase("QPSQL")
        db.setUserName("postgres")
        db.setPassword("12345678")
        db.setPort(5432)
        db.setDatabaseName("postgres")
        db.setHostName("localhost")
        db.open()

        self.update_def()
        self.update_work()
        self.update_ref()
       
        query = QSqlTableModel()
        sql = "SELECT COUNT(*) FROM public.Defective "
        query.setTable("Defective")
        query.select()
        query.removeColumn(0)
        self.tableView_defective.setModel(query)
        self.current_def=self.tableView_defective.model().index(0,0).data()
        query.setHeaderData(0, QtCore.Qt.Horizontal,"Имя принтера")
        query.setHeaderData(1, QtCore.Qt.Horizontal,"ломка")
        query.setHeaderData(2, QtCore.Qt.Horizontal,"недостаток")
    
    
        query2 = QSqlTableModel()
        sql = "SELECT * FROM public.Refilled"
        query2.setTable("Refilled")
        query2.select()
        query2.removeColumn(0)
        self.tableView_refueled.setModel(query2)
        query2.setHeaderData(0, QtCore.Qt.Horizontal,"Имя принтера")
        query2.setHeaderData(1, QtCore.Qt.Horizontal,"Диагностика")
        query2.setHeaderData(2, QtCore.Qt.Horizontal,"очистка")
        query2.setHeaderData(3, QtCore.Qt.Horizontal,"Тестирование устройство")
        query2.setHeaderData(4, QtCore.Qt.Horizontal,"необходимый")
        
       
    
        query3 = QSqlTableModel()
        sql = "SELECT * FROM public.Working"
        query3.setTable("Working")
        query3.select()
        query3.removeColumn(0)
        self.tableView_working.setModel(query3)
        self.current_def =self.tableView_working.model().index(0,0).data()
        query3.setHeaderData(0, QtCore.Qt.Horizontal,"Имя принтера")
        query3.setHeaderData(1, QtCore.Qt.Horizontal,"место установление")

 
        query4 = QSqlTableModel()
        sql = "SELECT * FROM public.On_clade"
        query4.setTable("On_clade")
        query4.select()
        query4.removeColumn(0)
        self.tableView_on_clade.setModel(query4)
        query4.setHeaderData(0, QtCore.Qt.Horizontal,"Имя принтера")
        query4.setHeaderData(1, QtCore.Qt.Horizontal,"серийный номер")
        query4.setHeaderData(2, QtCore.Qt.Horizontal,"порт номера ")
        
        

#####################################################Кнопка добавление ##############################
    def add_Defective_button(self):
        self.add_dt = Defectiveadd(self.update_def)
        self.add_dt.show()

    
    def add_Working_Button(self):
        self.add_w = Workingadd(self.current_def,self.update_work)
        self.add_w.show()

    def add_Refilled_button(self):
        self.add_rd =Refilledadd(self.current_work,self.update_ref)
        self.add_rd.show()

    def add_Onclade_button(self):
        self.add_clade =Oncladeadd(self.update_Onclade)
    def dp_clicked(self):
        row = self.tableView_defective.selectedIndexes()[0].row()
        self.current_dep = self.tableView_defective.model().index(row, 0).data()

    def work_clicked(self):
        row = self.tableView_working.selectedIndexes()[0].row()
        self.current_ward = self.tableView_working.model().index(row, 0).data()

    def rd_clicked(self):
        row = self.tableView_refueled.selectedIndexes()[0].row()
        self.current_ward = self.tableView_refueled.model().index(row, 0).data()

    
    def update_def(self):
        query = QSqlTableModel()
        query.setTable("Defective")
        query.select()
        self.tableView_defective.setModel(query)
    
    def update_work(self):
        query2 = QSqlTableModel()
        query2.setTable("Working")
        query2.select()
        self.tableView_working.setModel(query2)

    def update_ref(self):
        query3 = QSqlTableModel()
        query3.setTable("Refilled")
        query3.select()
        self.tableView_working.setModel(query3)
    def update_Onclade(self):
        query4 = QSqlTableModel()
        query4.setTable("On_clade")
        query4.select()
        self.tableView_working.setModel(query4)

####### Конец не основного окна #################
class Defectiveadd(add_defective.Ui_Form):
    def init(self,update_def):
        super().__init__()
        self.setupUi(self)
        
        self.update_def =update_def
       
        self.pushButton_add_pr.clicked.connect(self.add_b_defective)
        self.pushButton_cansel_pr.clicked.connect(self.exit_defect)

    def exit_defect(self):
        self.close()

    def add_b_defective(self):
        if self.lineEdit_name_pr.text() and self.lineEdit_break.text() and self.lineEdit_flaw.text():
            query_dt = QSqlQuery()
            query_dt.exec(f"INSERT INTO public.Defective(name_printer, breaking, flaw) VALUES ('{self.lineEdit_name_pr.text()}', '{self.lineEdit_break.text()}', '{self.lineEdit_flaw.text()}')")
            self.update_def()

class Workingadd(add_Working.Ui_Form):
    def __init__(self,def_id,update_work):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.add_work_button)
        self.pushButton_2.clicked.connect(self.exit_ward)
      
        self.dep_id = def_id
        self.update_work = update_work

    def exit_ward(self):
        self.close()
    
    def add_work_button(self):
        if self.lineEdit.text() and self.lineEdit_2.text():
            query_wk = QSqlQuery()
            query_wk.exec(f"INSERT INTO publc.Working (name_printer3,place_establishment) VALUES  ('{self.lineEdit.text()}', '{self.lineEdit_2.text()}')")
            self.update_work()


class Refilledadd(add_Refilled.Ui_Form):
    def __init__(self,work_id,update_ref):
        super().__init__()
        self.setupUi(self)
        
        self.work_id = work_id
        self.update_ref = update_ref
        self.pushButton_cansel_refilled.clicked.connect(self.exit_refilled)
        self.pb_add_refilled.clicked.connect(self.add_refilled)
        

    def exit_refilled(self):
        self.close()
    
    def add_refilled(self):
            if self.lineEdit_name_printer2.text() and self.lineEdit_diagnostics.text() and self.lineEdit_clearing.text() and self.lineEdit_testing_device.text() and self.lineEdit_necessary.text():
                query_rt = QSqlQuery()
                query_rt.exec(f"INSERT INTO public.Refilled (name_printer2,diagnostics,clearing,testing_device,necessary) VALUES  ('{self.lineEdit_name_printer2.text()}', '{self.lineEdit_diagnostics.text()}','{self.lineEdit_clearing.text()}','{self.lineEdit_testing_device.text()}',{self.lineEdit_necessary.text()})")
                self.update_ref()

class Oncladeadd(add_On_clade.Ui_Form):
    def __init__(self,update_Onclade):
        super().__init__()
        self.setupUi(self)

        self.update_Onclade =update_Onclade
        self.pushButton_add_onclade.clicked.connect(self.add_Onclade)
        self.pushButton_exit_onclade.clicked.connect(self.exit_onclade)

    def exit_onclade(self):
        self.close()
    def add_Onclade(self):
        query_rt = QSqlQuery()
        query_rt.exec(f"INSERT INTO public.On_clade (name_printer4,serial_number,port_number) VALUES  ('{self.lineEdit_nameprinter4.text()}', '{self.lineEdit_serial_number.text()}','{self.lineEdit_port_number.text()}')")
        


        
if __name__ == '__main__':
    app =QApplication(sys.argv)
    window =PrinterMain()
    window.show()
    app.exec_()