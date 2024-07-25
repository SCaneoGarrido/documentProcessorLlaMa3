# ------------------------------- IMPORTACIONES DE LIBRERIAS -------------------------- #
import os
from flask import Flask, render_template, jsonify, request # type: ignore
from werkzeug.utils import secure_filename
from modules.llama3_handler import Llama3Handler
from modules.file_handler import FileHandler

# ------------------------------- CONFIGURACION DE DIRECTORIOS Y VARIABLES -------------- #
app = Flask(__name__, template_folder="templates", static_folder="static")
UPLOADS_FOLDER = 'UPLOADS_FOLDER' # Variable de APP para crear la carpeta de 
ALLOWED_EXTENSIONS = {'txt', 'pdf'} # se pueden agregar más a medida que se requiera
app.config['UPLOADS_FOLDER'] = UPLOADS_FOLDER


# -------------------------------- INICIALIZACION DE CLASES ------------------------------ #
FileManager_instace = FileHandler()
Llama3Controller_instance = Llama3Handler()
# ----------------------------- FUNCION AUXILIAR (COMPROBACION DE UN ARCHIVO CON EXTENSION VALIDO) --------------- #
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


# ----------------------------------- RENDERIZADOR DE HOME -------------------------------------------------------- #
@app.route("/")
def home():
    return render_template("index.html")


# ---------------------------------- RUTA PRINCIPAL DE PROCESAMIENTO --------------------------------------------- #
@app.route('/processing', methods=['POST'])
def processing():
    if request.method == 'POST':
        if 'file' not in request.files:
            return "No file part", 400

        file = request.files['file']
        prompt = request.form.get('prompt', '')
        keywords = request.form.get('keywords')
        if file.filename == '':
            return jsonify({'Error': 'No selected file'}), 400

        try:
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                upload_folder = app.config['UPLOADS_FOLDER']

                if not os.path.exists(upload_folder):
                    os.makedirs(upload_folder)
                
                # Ruta completa del archivo
                ruta_archivo = os.path.join(upload_folder, filename)
                file.save(ruta_archivo)

                
                ruta_txt = FileManager_instace.extract_text_from_pdf(ruta_archivo)
                try:
                    if ruta_txt is not None:
                        result = Llama3Controller_instance.generate_summary_from_text_defaultPrompt(ruta_txt)
                        # manejar las palabras
                        if keywords is not None:
                            result_words = Llama3Controller_instance.search_keywords(ruta_txt, keywords)
                            summary_ = f"{result}\n Seccion Palabras\n {result_words}"

                        summary_ = f"{result}\n"

                        if result:
                            print(result)
                            return jsonify({'msg':'File successfully processed', 'summary':(summary_)}), 200
                        else:
                            return jsonify({'error':'Ocurrio un error'}), 400
                except Exception as e:
                    print(f"Ocurrio un error al procesar el archivo\n Error -> {e}")
                    return jsonify({'error':'Hubo un error al intentar procesar el archivo'}), 500     
            
            else:
                return jsonify({'error': 'Archivo no permitido'}), 400
        except Exception as e:
            print(f"Hubo un error al intentar guardar el archivo en: {UPLOADS_FOLDER}.\nError -> {e}")
            return jsonify({'error': 'No se ha podido procesar su solicitud en este momento'}), 500
    else:
        return "Method not allowed", 405

# ------------------------ EJECUCION DE APP -------------------------------------------- #
if __name__ == "__main__":
    app.run(debug=True)
