let selectedOption = 'defaultPrompt'; // Valor predeterminado

document.getElementById('fileInput').addEventListener('change', () => {
  const file = document.getElementById('fileInput').files[0];
  if (file) {
    document.getElementById('sidebar').style.display = 'block'; // Mostrar el sidebar
  } else {
    document.getElementById('sidebar').style.display = 'none'; // Ocultar el sidebar si no hay archivo
  }
});

document.getElementById('defaultPromptBtn').addEventListener('click', () => {
  selectedOption = 'defaultPrompt';
  document.getElementById('defaultPromptBtn').classList.add('btn-success');
  document.getElementById('customPromptBtn').classList.remove('btn-success');
  document.getElementById('llama3PromptBtn').classList.remove('btn-success');
});

document.getElementById('customPromptBtn').addEventListener('click', () => {
  selectedOption = 'customPrompt';
  document.getElementById('defaultPromptBtn').classList.remove('btn-success');
  document.getElementById('customPromptBtn').classList.add('btn-success');
  document.getElementById('llama3PromptBtn').classList.remove('btn-success');
});

document.getElementById('llama3PromptBtn').addEventListener('click', () => {
  selectedOption = 'llama3Prompt';
  document.getElementById('defaultPromptBtn').classList.remove('btn-success');
  document.getElementById('customPromptBtn').classList.remove('btn-success');
  document.getElementById('llama3PromptBtn').classList.add('btn-success');
});

document.getElementById('submitBtn').addEventListener('click', (event) => {
  event.preventDefault();

  const file_ = document.getElementById('fileInput').files[0];
  const keywords = document.getElementById('keywords').value;

  if (!file_) {
    console.log('No se ha seleccionado ningún archivo');
    alert('Seleccione un archivo');
    return;  // Detener la ejecución si no se selecciona un archivo
  }

  const formData = new FormData();
  formData.append('file', file_);  // Añadir 'file' como la clave para el archivo
  formData.append('keywords', keywords);  // Añadir las palabras clave
  formData.append('selectedOption', selectedOption);  // Añadir la opción seleccionada

  console.log(`Datos de envio a servidor: ${file_}\n${keywords}\n${selectedOption}\n `)
  fetch('/processing', {
    method: 'POST',
    body: formData
  })
    .then(response => response.json())
    .then(data => {
      console.log(`Respuesta del servidor: ${data.msg}`);
      if (data.msg === 'File successfully processed') {
        alert('Archivo procesado exitosamente');
      } else {
        alert('Error en el procesamiento del archivo');
      }
    })
    .catch(err => {
      console.error(`Ha ocurrido un error en la petición: ${err}`);
      alert('Error en la petición al servidor');
    });
});
