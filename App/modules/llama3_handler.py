# ------------------------ IMPORTACION DE LIBRERIAS ------------------------ #
import subprocess

# ------------------------ CLASE MANEJO DE LLAMA ------------------------ #
class Llama3Handler:
    # ------------------------ CONSTRUCTOR ------------------------ #
    def __init__(self) -> None:
        self.command = 'ollama run llama3'
    # ------------------------ CHAT CON LLAMA 3 ------------------------ #
    def just_chat_with_llama(self, msg):
        prompt = f"""
            Porfavor responde al usuario el mensaje que ha enviado '{msg}'.
            Recuerda siempre consultar si necesita ayuda en alguna tareas
            (responde el idioma en el que este el mensaje)
        """
        try:
            result = subprocess.run(self.command, input=prompt, text=True, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding='utf-8')
            output = result.stdout.strip()
            return output
        except subprocess.CalledProcessError as e:
            print(f"Error al ejecutar el comando: {e}")
            print(f"Salida de error: {e.stderr}")
            return ""
        

    # ------------------------ CHAT EN BASE A UN ARCHIVO ------------------------ #
    def chat_with_file(self, msg, docx_text):
        with open(docx_text, 'r', encoding='utf-8') as file:
            text_docx = file.read()
        
        prompt = f"""
            Contesta el mensaje del usuario '{msg}' en base al archivo que ha proporcionado: '{text_docx}'
        """

        try:
            result = subprocess.run(self.command, input=prompt, text=True, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding='utf-8')
            output = result.stdout.strip()
            return output
        except subprocess.CalledProcessError as e:
            print(f"Error al ejecutar el comando: {e}")
            print(f"Salida de error: {e.stderr}")
            return ""

    # ------------------------ GENERA UN RESUMEN CON UN PROMPT PREDETERMINADO ------------------------ #
    def generate_summary_from_text_defaultPrompt(self, txt_path):
        with open(txt_path, 'r', encoding='utf-8') as file:
            text = file.read()
        
        new_prompt = f"""
            Genera un resumen extenso y detallado del siguiente texto: '{text}'. 
            El resumen debe ser en español y debe abarcar los aspectos más importantes y relevantes del contenido. Asegúrate de incluir:
            - **Resumen Extenso:**: Proporciona un resumen que abarque toda la informacion sobre el texto, no debes saltar detalles.
            - **Contexto General**: Proporciona una visión general del tema principal del documento, destacando los puntos más significativos.
            - **Puntos Clave**: Identifica y resume los puntos clave, ideas principales y cualquier información crucial que se discuta en el texto.
            - **Conceptos y Términos Importantes**: Explica los conceptos, términos técnicos o palabras clave mencionadas, proporcionando una breve definición o descripción cuando sea necesario.
            - **Estructura y Argumentos**: Describe cómo está estructurado el documento y los principales argumentos o secciones presentadas.
            - **Conclusiones y Recomendaciones**: Resume cualquier conclusión importante o recomendaciones ofrecidas en el documento.

            Evita incluir detalles redundantes o información irrelevante. No uses tablas, gráficos ni caracteres especiales como barras o líneas de separación. El resumen debe ser claro, comprensible y completo, proporcionando una visión integral del documento.
        """

        try:
            result = subprocess.run(self.command, input=new_prompt, text=True, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding='utf-8')
            output = result.stdout.strip()
            return output

        except subprocess.CalledProcessError as e:
            print(f"Error al ejecutar el comando: {e}")
            print(f"Salida de error: {e.stderr}")
            return ""
    
    # ------------------------ BUSCA PALABRAS CLAVE ------------------------ #
    def search_keywords(self, txt_path, key_words):
        with open(txt_path, 'r', encoding='utf-8') as file:
            text = file.read()
            
        if key_words == '':
            print("No se han ingresado palabras clave")
            result_noWords = "No se ingresaron palabras clave"
            return result_noWords
        
        prompt_keyWords = f"""
            Basado en el siguiente texto: '{text}', proporciona una explicación breve y clara en español sobre el contexto en el que se mencionan las siguientes palabras clave: {key_words}.
            Evita incluir tablas, gráficos o caracteres especiales como barras o líneas de separación. No intentes dibujar o crear tablas.
        """
        
        try:
            result = subprocess.run(self.command, input=prompt_keyWords, text=True, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding='utf-8')
            output = result.stdout.strip()
            return output

        except subprocess.CalledProcessError as e:
            print(f"Error al ejecutar el comando: {e}")
            print(f"Salida de error: {e.stderr}")
            return ""