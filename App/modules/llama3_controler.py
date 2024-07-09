# Este modulo es para crear la logica de los controles para llama3
import os

class Llama3Controler:
  def __init__(self, uploads_folder):
    self.uploads_folder = uploads_folder

  
  def clear_uploads(self):
    # Esta funcion se encargara de limpiar todo el contenido de la carpeta
    # UPLOADS_FOLDER luego de que se termine el procesamiento
    print(f"Carpeta a limpiar {self.uploads_folder}")
    try:
      for f in os.listdir(self.uploads_folder):
        os.remove(os.path.join(dir, f))

      print("Directorio limpiado correctamente")
      return True
    except Exception as e:
      print(f"Hubo un error al limpiar el directorio {e}")
      return False