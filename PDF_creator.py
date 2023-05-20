from reportlab.pdfgen import canvas

# Создание нового PDF-документа
c = canvas.Canvas("output.pdf", pagesize=(500, 800))

# Добавление текста на страницу
c.drawString(200, 200, "storage")

# Сохранение и закрытие документа
c.save()