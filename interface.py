import PySimpleGUI as sg
import get_base_parameters
import random

#  date, customer_name, customer_number, tire_brand, tire_model,
#  tire_size_width, tire_size_profile, tire_size_diameter, car_model, license_plate, check_number, manager
#  https://www.udemy.com/course/pysimplegui/
#  https://pypi.org/project/PySimpleGUI/2.7.0/

base_parameters = list(get_base_parameters.get_base_parameters())
models_dict = {}
diameter_conditions = {}

for brand in range(len(base_parameters[5])):

    brand_choiced = base_parameters[5][brand]
    models_dict[brand_choiced] = base_parameters[6][brand_choiced]

def interface():

    sg.theme('Dark black1')
    layout = [
        [sg.Text('ФИО клиента', size=(12, 1)), sg.InputText(size=(40, 1), key='customer_name', font=('Verdana', 16))],
        [sg.Text('Тел. клиента', size=(12, 1)), sg.InputText(size=(40, 1), key='customer_number', font=('Verdana', 16))],
        [sg.Text('Ширина', size=(12, 1)), sg.Combo(base_parameters[1], size=(5, 10), key='tire_size_width', font=('Verdana', 16)),
        sg.Text('Проф.', size=(4, 1)), sg.Combo(base_parameters[2], size=(5, 10), key='tire_size_profile', font=('Verdana', 16)),
        sg.Text('Диам.', size=(5, 1)), sg.Combo(base_parameters[3], size=(5, 10), key='tire_size_diameter', font=('Verdana', 16)),
        sg.Text('Сезон', size=(5, 1)), sg.Combo(base_parameters[4], size=(6, 10), key='tire_season', font=('Verdana', 16))],
        [sg.Text('Бренд', size=(12, 1)), sg.Combo(base_parameters[5], size=(7, 10), enable_events=True, key='tire_brand', font=('Verdana', 16)),
        sg.Text('Модель', size=(6, 1)), sg.Combo([], size=(25, 10), key='tire_model', font=('Verdana', 16))],
        [sg.Text('Сумма чека', size=(12, 1)), sg.InputText(size=(40, 10), key='check_sum', font=('Verdana', 16))],
        [sg.Text('ФД чека', size=(12, 1)), sg.InputText(size=(40, 10), key='NFD', font=('Verdana', 16))],
        [sg.Text('ФПД чека', size=(12, 1)), sg.InputText(size=(40, 10), key='check_number', font=('Verdana', 16))],
        [sg.Text('Менеджер', size=(12, 1)), sg.Combo(base_parameters[0], size=(39, 12), key='manager', font=('Verdana', 16))],

        [sg.Submit('Зарегистрировать'), sg.Cancel('Отмена')]
    ]
    window = sg.Window('Анкета бесплатного шиномонтажа', layout)


    while True: # The Event Loop

        unfilled_fields = 0
        event, values = window.read()

        if event in (None, 'Exit', 'Отмена'):
            break

        if event == 'tire_brand':
            depended_model = models_dict[values['tire_brand']]
            window['tire_model'].update(values=depended_model)

        if event == 'Зарегистрировать':

            for value in values.values():
                if value == '':
                    unfilled_fields += 1

            if unfilled_fields > 0:
                sg.popup_auto_close('Заполните все поля', auto_close_duration=2)

            else:
                brand_name_cropped = values["tire_brand"][:3].upper()
                rand_first = random.randint(100, 999)
                managers_key = base_parameters[0].index(values['manager']) + 1
                rand_last = random.randint(10, 99)
                values['unique_code'] = f'{brand_name_cropped}{rand_first}{managers_key}{rand_last}'
                sg.popup_scrolled(f'БШМ КОД - {brand_name_cropped}{rand_first}{managers_key}{rand_last}',
                                  title='Скопируй и вставь в комментарий к заказу в 1с',
                                  font=("Verdana Bold", 24), text_color='red', size=(22, 2))
                return values, event

