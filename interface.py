import PySimpleGUI as sg

#  date, customer_name, customer_number, tire_brand, tire_model,
#  tire_size, car_model, license_plate, check_number, manager
#  https://www.udemy.com/course/pysimplegui/


def interface():
    layout = [
        [sg.Text('Дата продажи'), sg.InputText(size=(10, 2), key='date')],
        [sg.Text('ФИО клиента'), sg.InputText(size=(40, 2), key='cutomer_name')],
        [sg.Text('Телефон клиента'), sg.InputText(size=(20, 2), key='customer_number')],
        [sg.Text('Бренд шин'), sg.Combo(['pirelli', 'nokian', 'cordiant'], size=(20, 2), key='tire_brand')],
        [sg.Output(size=(88, 20))],
        [sg.Submit(), sg.Cancel()]
    ]
    window = sg.Window('File Compare', layout)
    while True:                             # The Event Loop
        event, values = window.read()
        # print(event, values) #debug
        if event in (None, 'Exit', 'Cancel'):
            break

interface()