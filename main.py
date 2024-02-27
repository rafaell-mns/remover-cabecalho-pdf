import PyPDF3

def remove_header_by_position(input_pdf_path, output_pdf_path, header_height_threshold):
    with open(input_pdf_path, 'rb') as input_file:
        reader = PyPDF3.PdfFileReader(input_file)
        writer = PyPDF3.PdfFileWriter()

        for page_num in range(reader.numPages):
            page = reader.getPage(page_num)
            media_box = page.mediaBox
            
            # Se o cabeçalho estiver acima da altura especificada, consideramos removê-lo
            if media_box.upperRight[1] > header_height_threshold:
                media_box.upperRight = (media_box.upperRight[0], header_height_threshold)
            
            writer.addPage(page)

        with open(output_pdf_path, 'wb') as output_file:
            writer.write(output_file)

input_pdf_path = 'input.pdf'  # Caminho do PDF de entrada
output_pdf_path = 'output.pdf'  # Caminho do PDF de saída após a remoção do cabeçalho
header_height_threshold = 540  # Altura máxima do cabeçalho na página (ajuste conforme necessário)

print("A função vai ser executada...")
remove_header_by_position(input_pdf_path, output_pdf_path, header_height_threshold)
print("Função executada com sucesso!")
