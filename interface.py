import PySimpleGUI as sg
import get_base_parameters
#  date, customer_name, customer_number, tire_brand, tire_model,
#  tire_size_width, tire_size_profile, tire_size_diameter, car_model, license_plate, check_number, manager
#  https://www.udemy.com/course/pysimplegui/
#  https://pypi.org/project/PySimpleGUI/2.7.0/

base_parameters = list(get_base_parameters.get_base_parameters())
def interface():
    depended_model = base_parameters[5]['Pirelli']
    sg.theme('Dark black1')
    layout = [
        [sg.Text('Дата продажи', size=(12, 1)), sg.InputText(size=(40, 1), key='date')],
        [sg.Text('ФИО клиента', size=(12, 1)), sg.InputText(size=(40, 1), key='cutomer_name')],
        [sg.Text('Тел. клиента', size=(12, 1)), sg.InputText(size=(40, 1), key='customer_number')],
        [sg.Text('Ширина', size=(12, 1)), sg.Combo(base_parameters[1], size=(5, 10), key='tire_size_width'),
        sg.Text('Проф.', size=(5, 1)), sg.Combo(base_parameters[2], size=(5, 10), key='tire_size_profile'),
        sg.Text('Диам.', size=(5, 1)), sg.Combo(base_parameters[3], size=(5, 10), key='tire_size_diameter')],
        [sg.Text('Бренд', size=(12, 1)), sg.Combo(base_parameters[4], size=(7, 10), enable_events=True, key='tire_brand'),
        sg.Text('Модель', size=(6, 1)), sg.Combo(depended_model, size=(19, 10), key='tire_model')],
        [sg.Text('Модель авто', size=(12, 1)), sg.InputText(size=(40, 10), key='car_model')],
        [sg.Text('Номер авто', size=(12, 1)), sg.InputText(size=(40, 10), key='license_plate')],
        [sg.Text('Номер чека', size=(12, 1)), sg.InputText(size=(40, 10), key='check_number')],
        [sg.Text('Менеджер', size=(12, 1)), sg.Combo(base_parameters[0], size=(38, 12), key='manager')],

        [sg.Submit('Зарегистрировать'), sg.Cancel('Отмена')]
    ]
    window = sg.Window('Анкета бесплатного шиномонтажа', layout)
    while True:                             # The Event Loop
        event, values = window.read()
        # print(event, values) #debug
        if event in ('tire_brand'):
            depended_model = base_parameters[5]['Tunga']

        if event in (None, 'Exit', 'Отмена'):
            break

interface()