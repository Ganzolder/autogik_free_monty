import PySimpleGUI as sg

# Определяем список вариантов для первого выпадающего списка
list1 = ['Option 1', 'Option 2', 'Option 3']

# Определяем зависящие списки со списками вариантов для каждого элемента первого списка
list2_options = {
    'Option 1': ['Choice 1', 'Choice 2', 'Choice 3'],
    'Option 2': ['Choice 4', 'Choice 5', 'Choice 6'],
    'Option 3': ['Choice 7', 'Choice 8', 'Choice 9']
}

# Определяем GUI элементы
layout = [
    [sg.Text('Select an option from List 1'), sg.Combo(list1, key='-LIST1-', enable_events=True)],
    [sg.Text('Select an option from List 2'), sg.Combo([], size=(10, 1), key='-LIST2-')]
]

# Создаем окно
window = sg.Window('Dependent Dropdown Lists Example', layout)

# Цикл обработки событий
while True:
    event, values = window.read()
    print(values)
    if event == sg.WINDOW_CLOSED:
        break
    elif event == '-LIST1-':
        # Обновляем список вариантов для второго выпадающего списка в зависимости от выбранного элемента первого списка
        list2 = list2_options[values['-LIST1-']]
        window['-LIST2-'].update(values=list2)

# Закрываем окно
window.close()
