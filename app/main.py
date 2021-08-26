from models.hospital import Hospital
from repos.hospitals import Hospitals
from models.doctor import Doctor
from repos.doctors import Doctors


if __name__ == '__main__':
    try:
        data_manager = Doctors(Doctor())
        data_manager.add_doctor_dialog()
        data_manager.display_all_doctors()
    except RecursionError as rte:
        print(rte)
    print('done')
