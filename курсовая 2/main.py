from PyQt5 import *
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtSql import QSqlDatabase, QSqlQuery, QSqlTableModel
import main1
import add_department
import add_ward
import add_patient

##ОСНОВНОЕ ОКНО##
class MainWindow(main1.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.current_dep = 0
        self.current_ward = 0

        self.pushButton_Department_add.clicked.connect(self.add_Department_button)
        self.pushButton_Ward_add.clicked.connect(self.add_Ward_Button)
        self.pushButton_Patient_add.clicked.connect(self.add_patient_Button)
        self.tableView_Department.clicked.connect(self.dp_clicked)
        self.tableView_Patient.clicked.connect(self.ward_clicked)

        db = QSqlDatabase.addDatabase('QPSQL')
        db.setHostName('localhost')
        db.setPort(5432)
        db.setDatabaseName('Hospital')
        db.setUserName('postgres')
        db.setPassword('student')
        db.open()

        self.update_dep()
        self.update_ward()
        self.update_patient()

        query = QSqlTableModel()
        sql = "SELECT * FROM public.procedure"
        query.setTable("procedure")
        query.select()
        self.tableView_Procedure.setModel(query)

    def add_Department_button(self):
        self.add_d = Add_Department(self.update_dep)
        self.add_d.show()

    def add_Ward_Button(self):
        self.add_w = Add_Ward(self.current_dep, self.update_ward)
        self.add_w.show()

    def add_patient_Button(self):
        self.add_p = Add_Patient(self.current_ward, self.update_patient)
        self.add_p.show()

    def dp_clicked(self):
        row = self.tableView_Department.selectedIndexes()[0].row()
        self.current_dep = self.tableView_Department.model().index(row, 0).data()

    def ward_clicked(self):
        row = self.tableView_Ward.selectedIndexes()[0].row()
        self.current_ward = self.tableView_Ward.model().index(row, 0).data()

    def update_dep(self):
        query = QSqlTableModel()
        query.setTable("department")
        query.select()
        self.tableView_Department.setModel(query)

    def update_ward(self):
        query = QSqlTableModel()
        query.setTable("ward")
        query.select()
        self.tableView_Ward.setModel(query)

    def update_patient(self):
        query = QSqlTableModel()
        query.setTable("patient")
        query.select()
        self.tableView_Patient.setModel(query)

##КОНЕЦ ОСНОВНОГО  ОКНА##

class Add_Department(add_department.Ui_MainWindow):
    def __init__(self, update_dep):
        super().__init__()
        self.setupUi(self)

        self.update_dep = update_dep

        self.pushButton_exit_Department.clicked.connect(self.exit_department)
        self.pushButton_add_base_Department.clicked.connect(self.add_b_department)

    def exit_department(self):
        self.close()

    def add_b_department(self):
        query = QSqlQuery()
        query.exec(f"INSERT INTO public.department (number ,name) VALUES ('{self.lineEdit_add_Department.text()}', '{self.lineEdit_2_add_Department.text()}')")
        self.update_dep()

class Add_Ward(add_ward.Ui_MainWindow):
    def __init__(self, dep_id, update_ward):
        super().__init__()
        self.setupUi(self)

        self.dep_id = dep_id
        self.update_ward = update_ward

        self.pushButton_exit_Ward.clicked.connect(self.exit_ward)
        self.pushButton_add_Ward.clicked.connect(self.add_w_ward)

    def exit_ward(self):
        self.close()

    def add_w_ward(self):
        query = QSqlQuery()
        query.exec(f"INSERT INTO public.ward (number, capacity, department_id) VALUES ('{self.lineEdit_add_Ward.text()}', '{self.lineEdit_2_add_Ward.text()}', '{self.dep_id}')")
        self.update_ward()

class Add_Patient(add_patient.Ui_MainWindow):
    def __init__(self, ward_id, update_patient):
        super().__init__()
        self.setupUi(self)

        self.ward_id = ward_id
        self.update_patient = update_patient
        self.pushButton_add_patient.clicked.connect(self.add_patient)

    def add_patient(self):
        query = QSqlQuery()
        query.exec(f"INSERT INTO public.patient (fullName, dateArrive, dateDisharge, diagnosis, ward_id) VALUES ('{self.lineEdit_FullName_patient.text()}', '{self.dateEdit_dateArrive_patient.text()}','{self.dateEdit_dateDisharge_patient}','{self.lineEdit_diagnosis_patient}' ,'{self.ward_id}')")
        self.update_patient()
        
app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()