from flask import Flask, render_template, jsonify, request #type: ignore

app = Flask(__name__, template_folder="templates", static_folder="static")


# renderizador
@app.route("/")
def home():
  return render_template("index.html")



@app.route('/processing', methods=['POST'])
def processing():
  if request.method == 'POST':
    if request.method == 'POST':
      
      if 'file' not in request.files:
        return "No file part", 400
      
      file = request.files['file']
      if file.filename == '':
        return jsonify({'Error': 'No selected file'}), 400
      
      return jsonify({'success':f"Archivo recibido {file.filename}"}), 200

    else:
      return "Method not allowed", 405              
if __name__ == "__main__":
  app.run(debug=True)