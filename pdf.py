from reportlab.lib.units import mm
from reportlab.pdfgen import canvas
from email import send_email

# Função para gerar o PDF
def generate_pdf():
    # Nome do arquivo PDF
    pdf_file = "sophia_ll.pdf"

    # Cria o canvas para o arquivo PDF com o tamanho de página A4
    c = canvas.Canvas(pdf_file, pagesize=(210 * mm, 297 * mm))

    # Texto a ser repetido
    text = "Sophia D L Lisboa"

    # Largura do texto
    text_width = c.stringWidth(text, "Helvetica", 12)

    # Tamanho da fonte
    font_size = 30

    # Enquanto houverem páginas para serem geradas (neste exemplo, apenas uma página)
    while c.getPageNumber() <= 1:
        # Posição Y inicial da página
        y = 297 * mm - (3 * mm)

        # Enquanto a posição Y ainda estiver dentro da página
        while y >= 0:
            # Posição X inicial da linha
            x = 0

            # Enquanto a posição X ainda estiver dentro da largura da página
            while x < 210 * mm:
                # Desenha o texto na posição X e Y
                c.drawString(x, y, text)

                # Atualiza a posição X para a próxima coluna
                x += text_width +12

            # Atualiza a posição Y para a próxima linha
            y -= font_size

        # Adiciona uma página ao PDF
        c.showPage()

    # Salva o arquivo PDF
    c.save()
  
    send_email('dalpizzol.eder@gmail.com', 'PDF', pdf_file )
# Executa a função se este arquivo for executado diretamente
if __name__ == "__main__":
    generate_pdf()
