from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase import pdfmetrics
from reportlab.lib import fonts
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib import colors
import os
import win32api
import win32print
import subprocess
import cups


def create_pdf(file_path, customer_name, tire_size, tire_brand, tire_model, customer_number, fd, fp):

    # Загружаем шрифт
    fonts.addMapping('DejaVu', 0, 0, 'DejaVuSans.ttf')

    # fonts.registerFontFamily(fonts.TTFont('DejaVu', 'DejaVuSans.ttf'))
    pdfmetrics.registerFont(TTFont('DejaVu', 'DejaVuSans.ttf'))

    # Создаем объект canvas
    c = canvas.Canvas(file_path, pagesize=letter)

    c.setFillColor(colors.slategrey)
    c.rect(45, 640, 150, 30, fill=1)
    c.rect(45, 610, 150, 30, fill=1)
    c.rect(45, 580, 150, 30, fill=1)
    c.rect(45, 550, 150, 30, fill=1)
    c.rect(45, 520, 150, 30, fill=1)
    c.rect(45, 490, 150, 30, fill=1)

    c.setFillColor(colors.white)
    c.rect(195, 640, 370, 30)
    c.rect(195, 610, 370, 30)
    c.rect(195, 580, 370, 30)
    c.rect(195, 550, 370, 30)
    c.rect(195, 520, 370, 30)
    c.rect(195, 490, 370, 30)

    c.setFillColor(colors.black)
    c.setFont('DejaVu', 18)
    c.drawString(290, 720, "Купон на бесплатный")
    c.drawString(330, 700, "шиномонтаж")

    c.setFont('DejaVu', 12)
    c.setFillColor(colors.white)
    c.drawString(50, 650, "Ф.И.О. покупателя")
    c.drawString(50, 620, "Модель и размер шин")
    c.drawString(50, 590, "Телефон покупателя")
    c.drawString(50, 560, "Марка и номер авто")
    c.drawString(50, 530, "ФД чека")
    c.drawString(50, 500, "ФП чека")

    c.setFillColor(colors.black)
    c.drawString(220, 650, customer_name)
    c.drawString(220, 620, f"{tire_brand}"+f" {tire_model}"+f" {tire_size}")
    c.drawString(220, 590, customer_number)
    c.drawString(220, 530, fd)
    c.drawString(220, 500, fp)

    c.setFont('DejaVu', 10)
    c.drawString(50, 470, "Акт выполненных работ. Услуги по снятию, демонтажу, монтажу, балансировке и установке")
    c.drawString(50, 455, "выполнены полностью и в срок. Претензий к объему и качеству и сроку не имею")

    c.drawString(375, 430, "Согласен с условиями акции*")
    c.drawString(50, 350, "Подпись дилера и дата")
    c.drawString(375, 350, "Подпись покупателя и дата")

    c.setFillColor(colors.wheat)
    c.rect(365, 390, 200, 30, fill=1)
    c.rect(365, 310, 200, 30, fill=1)
    c.rect(45, 310, 200, 30)

    c.setFillColor(colors.black)
    c.setFont('DejaVu', 8)
    c.drawString(50, 290, "*Условия акции")
    c.drawString(50, 270, f"При покупке четырех летних шин с посадочным диаметром 15+ под торговым знаком {tire_brand} в Автоцентре АВТОГИК")
    c.drawString(50, 260, "в течении всего периода проведения акции, Вы получаете 'Шиномонтаж В ПОДАРОК'. В акции участвуют")
    c.drawString(50, 250, f"все модели летних шин под товарным знаком {tire_brand}. К участию в акции допускаются только")
    c.drawString(50, 240, "физические лица, достигшие 18 лет. Покупатель может пользоваться услугой однократно на 1 комплект")
    c.drawString(50, 230, "шин приобретенных по Акции. Шинный центр, проводящий Акцию, оставляет за собой право на любой момент")
    c.drawString(50, 220, "прекратить проведение акции. Выплата денежного эквивалента, равного стоимости шиномонтажа, не производится.")
    c.drawString(50, 210, "После оказания услуги бесплатного шиномонтажа, потребитель ставит подпись на акте выполненных работ или")
    c.drawString(50, 200, "ином отчетном документе. Количество предоставляемых по Акции услуг ограниченно. Период проведения")
    c.drawString(50, 190, "акции с 01.03.2024 по 30.06.2024. Купоны, по которым не обратились в течении периода проведения Акции,")
    c.drawString(50, 180, "считаются недействительными. Организатор вправе в одностороннем порядке прекратить проведение Акции или")
    c.drawString(50, 170, "вносить изменения в настоящие правила Акции. Участник, принимая участие в Акции, дает свое согласиена")
    c.drawString(50, 160, "получение подарков от Организатора Акции, а также на коммуникацию в отношении  проводимых Организатором")
    c.drawString(50, 150, "рекламных акций, в том числе по телефону, указанному Участником на купоне на бесплатный шиномонтаж.")

    # Добавляем изображение
    c.drawInlineImage(f"base/{tire_brand}.png", 45, 690, width=150, height=40)

    # Закрываем объект canvas, сохраняя изменения в PDF-файл
    c.save()

'''
def print_to_network_printer(file_path, network_printer_name):
    # Получаем информацию о принтере

    # Создаем документ для печати
    hprinter = win32print.OpenPrinter(network_printer_name)
    try:
        win32print.StartDocPrinter(hprinter, 1, ('Test Job', None, 'RAW'))
        try:
            win32print.StartPagePrinter(hprinter)
            # Читаем содержимое файла и печатаем его
            with open(file_path, 'rb') as f:
                win32print.WritePrinter(hprinter, f.read())
            win32print.EndPagePrinter(hprinter)
        finally:
            win32print.EndDocPrinter(hprinter)
    finally:
        win32print.ClosePrinter(hprinter)


if __name__ == "__main__":

    pdf_path = "example_form.pdf"
    
    # Укажите UNC-путь к сетевому принтеру
    network_printer_name = r"\\AUTOGIKVOL-ПК\HP LaserJet MFP M28-M31 PCLmS"

    try:
        print_to_network_printer(pdf_path, network_printer_name)
        print("Печать завершена.")
    except Exception as e:
        print(f"Произошла ошибка при печати: {e}")'''