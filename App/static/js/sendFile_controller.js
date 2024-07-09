document.getElementById('file_input').addEventListener('submit', (event) => {
  event.preventDefault();

  const file_ = document.getElementById('fileInput').files[0];

  if (!file_) {
    console.log('No se ha seleccionado ningún archivo');
    alert('Seleccione un archivo');
    return;  // Detener la ejecución si no se selecciona un archivo
  }

  const formData = new FormData();
  formData.append('file', file_);  // Añadir 'file' como la clave para el archivo

  fetch('/processing', {
    method: 'POST',
    body: formData
  })
    .then(response => response.json())
    .then(data => {
      console.log(`Respuesta del servidor: ${data.msg}`);
    })
    .catch(err => {
      console.error(`Ha ocurrido un error en la petición: ${err}`);
    });
});
