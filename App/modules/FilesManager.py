# --------------------- IMPORTACIONES ------------------------------- #
import os
from PyPDF2 import PdfReader

# ----------------- INSTANCIAMIENTO DE CLASE ----------------------- #

class FileManager:
    def __init__(self):
        self.files_folder = 'FILES_FOLDER'
        # Verificamos si la carpeta existe; si no, la creamos
        if not os.path.exists(self.files_folder):
            os.makedirs(self.files_folder)
    
    def process_pdf(self, file_path):
        try:
            # ------------------- OBTENEMOS LA CANTIDAD DE PAGINAS -------------------------------------  #
            reader = PdfReader(file_path)
            pages = len(reader.pages)
            
            # ------------------- DEFINIMOS LA RUTA DEL ARCHIVO DE SALIDA -------------------------------------  #
            output_file_path = os.path.join(self.files_folder, 'output.txt')
            
            # ------------------- ABRIMOS EL ARCHIVO TXT EN MODO ESCRITURA -------------------------------------  #
            with open(output_file_path, 'w', encoding='utf-8') as file_output:
                # ------------------- CICLO PARA EXTRAER EL TEXTO DE CADA PÁGINA ----------------------------- #
                for index in range(pages):
                    page = reader.pages[index]  # Obtenemos la página según el índice 
                    page_text = page.extract_text()  # Extraemos el texto de la página
                    
                    # ------------------- ESCRIBIMOS EL TEXTO EN EL ARCHIVO ------------------------------------- #
                    if page_text:  # Verificamos si se extrajo texto
                        print(f"Texto extraido: {page_text}")
                        file_output.write(page_text + '\n')  # Escribimos el texto con un salto de línea 
            return output_file_path
        
        except Exception as e:
            print(f"Hubo un error al procesar el archivo PDF\n Error -> {e}")
            return None

    