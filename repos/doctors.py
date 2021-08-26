from models.doctor import Doctor


class Doctors(object):

    def __init__(self, doctor_model: Doctor):
        self._doctor_model = doctor_model

    def add_doctor_dialog(self) -> None:
        """ Консольный диалог добавления доктора в базу """
        print('Введите данные доктора для добавления: ')
        name = input('ФИО: ')
        phone = input('Телефон: ')
        self._doctor_model.add_doctor(name, phone)
        print('Доктор добавлен в базу')

    def display_all_doctors(self) -> None:
        """ Вывод в консоль списка докторов """
        doctors_list = self._doctor_model.get_all_doctors()
        count = 0
        for d in doctors_list:
            count += 1
            print(f'{count}. {d[1]} {d[2]}')
