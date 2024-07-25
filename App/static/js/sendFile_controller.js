/**
 * SCRIPT ENCARGADO DE MANEJAR EL ENVIO DE DATOS AL SERVIDOR
 * 
 * Este script se ejecuta cuando el documento HTML ha terminado de cargarse.
 * Maneja la interacción del usuario con la interfaz para seleccionar archivos,
 * elegir opciones de prompt y enviar datos al servidor. También muestra un
 * spinner durante el procesamiento y gestiona la descarga de resultados procesados.
 */
document.addEventListener('DOMContentLoaded', () => {
  // Variable para almacenar la opción de prompt seleccionada
  let selectedOption = 'defaultPrompt'; 
  
  // Referencia al elemento del spinner para mostrar la carga
  let spinnerGif = document.getElementById('spinner-Gif');
  spinnerGif.style.display = 'none'; // Ocultar el spinner inicialmente

  // Maneja el evento de cambio en el input de archivo
  document.getElementById('fileInput').addEventListener('change', () => {
    const file = document.getElementById('fileInput').files[0];
    // Mostrar u ocultar el sidebar dependiendo de si se ha seleccionado un archivo
    document.getElementById('sidebar').style.display = file ? 'block' : 'none';
  });

  // Maneja el clic en el botón para seleccionar el prompt por defecto
  document.getElementById('defaultPromptBtn').addEventListener('click', () => {
    selectedOption = 'defaultPrompt'; // Actualiza la opción seleccionada
    document.getElementById('defaultPromptBtn').classList.add('btn-success');
    document.getElementById('customPromptBtn').classList.remove('btn-success');
    document.getElementById('llama3PromptBtn').classList.remove('btn-success');
  });

  // Maneja el clic en el botón para seleccionar el prompt personalizado
  document.getElementById('customPromptBtn').addEventListener('click', () => {
    selectedOption = 'customPrompt'; // Actualiza la opción seleccionada
    document.getElementById('defaultPromptBtn').classList.remove('btn-success');
    document.getElementById('customPromptBtn').classList.add('btn-success');
    document.getElementById('llama3PromptBtn').classList.remove('btn-success');
  });

  // Maneja el clic en el botón para seleccionar el prompt de LLaMA-3
  document.getElementById('llama3PromptBtn').addEventListener('click', () => {
    selectedOption = 'llama3Prompt'; // Actualiza la opción seleccionada
    document.getElementById('defaultPromptBtn').classList.remove('btn-success');
    document.getElementById('customPromptBtn').classList.remove('btn-success');
    document.getElementById('llama3PromptBtn').classList.add('btn-success');
  });

  // Maneja el clic en el botón de envío
  document.getElementById('submitBtn').addEventListener('click', (event) => {
    event.preventDefault(); // Evita el comportamiento por defecto del formulario

    const file_ = document.getElementById('fileInput').files[0];
    const keywords = document.getElementById('keywords').value;

    // Verifica si se ha seleccionado un archivo
    if (!file_) {
      console.log('No se ha seleccionado ningún archivo');
      alert('Seleccione un archivo');
      return;  // Detiene la ejecución si no se selecciona un archivo
    }

    spinnerGif.style.display = 'block'; // Muestra el spinner mientras se procesa

    let filename = file_.name; // Obtiene el nombre del archivo seleccionado

    // Crea un nuevo objeto FormData para enviar los datos al servidor
    const formData = new FormData();
    formData.append('file', file_);  // Añade el archivo al FormData
    formData.append('keywords', keywords);  // Añade las palabras clave
    formData.append('selectedOption', selectedOption);  // Añade la opción seleccionada

    console.log(`Datos de envío a servidor: ${filename}\n${keywords}\n${selectedOption}\n `)
    
    // Envía los datos al servidor mediante una solicitud POST
    fetch('/processing', {
      method: 'POST',
      body: formData
    })
      .then(response => response.json())
      .then(data => {
        if (data.msg === 'File successfully processed') {
          console.log(`Respuesta del servidor: ${data.msg}`);
          console.log(`Resultado: \n ${data.summary}`)

          // Crea un Blob con el resumen procesado para la descarga
          const blob = new Blob([data.summary], { type: 'text/plain' });
          const url = URL.createObjectURL(blob);

          // Crea un enlace de descarga para el archivo de resumen
          const a = document.createElement('a');
          a.href = url;
          a.download = `${filename}_procesado.txt`; // Nombre del archivo descargado
          document.body.appendChild(a);
          a.click(); 
          document.body.removeChild(a);

          // Libera la URL del Blob
          URL.revokeObjectURL(url);
        } else {
          alert('Error en el procesamiento del archivo');
        }
      })
      .catch(err => {
        console.error(`Ha ocurrido un error en la petición: ${err}`);
      })
      .finally(() => {
        spinnerGif.style.display = 'none'; // Oculta el spinner después de la petición
      });
  });
});
