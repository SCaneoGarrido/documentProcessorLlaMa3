import subprocess
import tempfile

class Llama3Controller:
    def __init__(self, model_name="llama3"):
        self.model_name = model_name

    def query(self, prompt):
        """Realiza una consulta al modelo Llama3 con un prompt dado."""
        # Crea un archivo temporal para almacenar la salida
        with tempfile.NamedTemporaryFile(delete=True, mode='w+', encoding='utf-8') as temp_file:
            result = subprocess.run(
                ["ollama", "run", self.model_name, prompt],
                stdout=temp_file,
                stderr=subprocess.PIPE,
                text=True
            )
            temp_file.seek(0)  # Regresa al inicio del archivo
            output = temp_file.read()
            return output.strip()

    def analyze_file(self, file_path, prompt):
        """Analiza el contenido de un archivo usando el modelo Llama3 con un prompt definido."""
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
            file_content = file.read()
        
        # Construye el prompt incluyendo el contenido del archivo
        full_prompt = f"{prompt}\n\nContenido del archivo:\n{file_content}"
        
        # Ejecuta la consulta al modelo
        return self.query(full_prompt)
