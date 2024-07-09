import os

from flask import Flask, render_template, jsonify, request 
from werkzeug.utils import secure_filename
from modules.llama3_controler import Llama3Controler

app = Flask(__name__, template_folder="templates", static_folder="static")

UPLOADS_FOLDER = 'UPLOADS_FOLDER'
ALLOWED_EXTENSIONS = {'txt', 'pdf'} # se pueden agregar más a medida que se requiera

app.config['UPLOADS_FOLDER'] = UPLOADS_FOLDER

# FUNCION AUXILIAR (COMPROBACION DE UN ARCHIVO CON EXTENSION VALIDO)
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# renderizador
@app.route("/")
def home():
    return render_template("index.html")

@app.route('/processing', methods=['POST'])
def processing():
    if request.method == 'POST':
        if 'file' not in request.files:
            return "No file part", 400

        file = request.files['file']

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

                # AQUI TIENES QUE SEGUIR CON LA LOGICA PARA PROCESADO
                Llama3Controler_instance = Llama3Controler(upload_folder) # Esta es la instancia de clase de LLama3Controler
                
                
                return jsonify({'msg': f'Se ha guardado su archivo en la ruta {ruta_archivo} del servidor'}), 200
            else:
                return jsonify({'error': 'Archivo no permitido'}), 400
        except Exception as e:
            print(f"Hubo un error al intentar guardar el archivo en: {UPLOADS_FOLDER}.\nError -> {e}")
            return jsonify({'error': 'No se ha podido procesar su solicitud en este momento'}), 500
    else:
        return "Method not allowed", 405

if __name__ == "__main__":
    app.run(debug=True)
