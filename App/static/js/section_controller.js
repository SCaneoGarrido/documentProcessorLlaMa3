// seccion de control de secciones, con sus wenos comentarios

// Este script corre cuando el DOM es cargado
document.addEventListener('DOMContentLoaded', function() {
  // Get the home, ML, and app links
  const linkHome = document.getElementById('linkHome');
  const linkML = document.getElementById('linkML');
  const linkApp = document.getElementById('linkApp');

  // Get the home, ML, and app sections
  const homeSection = document.getElementById('homeSection');
  const mlSection = document.getElementById('mlSection');


  // Add a click event listener to the home link
  linkHome.addEventListener('click', function() {
    // Show the home section, hide the ML and app sections
    homeSection.style.display = 'block'; // Display the home section
    mlSection.style.display = 'none'; // Hide the ML section
    appSection.style.display = 'none'; // Hide the app section
  
  });

  // Add a click event listener to the ML link
  linkML.addEventListener('click', function() {
    // Hide the home section, show the ML section, hide the app section
    homeSection.style.display = 'none'; // Hide the home section
    mlSection.style.display = 'block'; // Display the ML section
    appSection.style.display = 'none'; // Hide the app section
  
  });

  // Add a click event listener to the app link
  linkApp.addEventListener('click', function() {
    // Hide the home and ML sections, show the app section
    homeSection.style.display = 'none'; // Hide the home section
    mlSection.style.display = 'none'; // Hide the ML section
    appSection.style.display = 'block'; // Display the app section
  });

});

// seccion de control de secciones