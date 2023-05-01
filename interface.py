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

for brand in range(len(base_parameters[4])):

    brand_choiced = base_parameters[4][brand]
    models_dict[brand_choiced] = base_parameters[5][brand_choiced]

#diameter_conditions = base_parameters[6]

def interface():

    sg.theme('Dark black1')
    layout = [
        [sg.Text('Дата продажи', size=(12, 1)), sg.InputText(size=(40, 1), key='date')],
        [sg.Text('ФИО клиента', size=(12, 1)), sg.InputText(size=(40, 1), key='customer_name')],
        [sg.Text('Тел. клиента', size=(12, 1)), sg.InputText(size=(40, 1), key='customer_number')],
        [sg.Text('Ширина', size=(12, 1)), sg.Combo(base_parameters[1], size=(5, 10), key='tire_size_width'),
        sg.Text('Проф.', size=(5, 1)), sg.Combo(base_parameters[2], size=(5, 10), key='tire_size_profile'),
        sg.Text('Диам.', size=(5, 1)), sg.Combo(base_parameters[3], size=(5, 10), key='tire_size_diameter')],
        [sg.Text('Бренд', size=(12, 1)), sg.Combo(base_parameters[4], size=(7, 10), enable_events=True, key='tire_brand'),
        sg.Text('Модель', size=(6, 1)), sg.Combo([], size=(19, 10), key='tire_model')],
        [sg.Text('Модель авто', size=(12, 1)), sg.InputText(size=(40, 10), key='car_model')],
        [sg.Text('Номер авто', size=(12, 1)), sg.InputText(size=(40, 10), key='license_plate')],
        [sg.Text('Номер чека', size=(12, 1)), sg.InputText(size=(40, 10), key='check_number')],
        [sg.Text('Менеджер', size=(12, 1)), sg.Combo(base_parameters[0], size=(38, 12), key='manager')],
        #[sg.print("Class",size=(15, 1), font=("Verdana",11),text_color='Red',justification='right', sg.OutPut
        [sg.Submit('Зарегистрировать'), sg.Cancel('Отмена')]
    ]
    window = sg.Window('Анкета бесплатного шиномонтажа', layout)


    while True: # The Event Loop

        unfilled_fields = 0
        event, values = window.read()
        # print(event, values) #debug

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
                sg.popup_scrolled(f'БШМ КОД - {brand_name_cropped}{rand_first}{managers_key}{rand_last}',
                                  title='Скопируй и вставь в комментарий к заказу в 1с',
                                  font=("Verdana Bold", 24), text_color='red', size=(22, 2))
                return values


#print(interface())