//FUNÇÃO PARA HEADER SUBIR E DESCER
document.addEventListener("DOMContentLoaded", function() {
  var prevScrollpos = window.pageYOffset;
  var navbar = document.getElementById("navbar");

  window.onscroll = function() {
      var currentScrollPos = window.pageYOffset;
      if (prevScrollpos > currentScrollPos) {
          navbar.style.top = "0";
      } else {
          navbar.style.top = "-100px"; // Ajuste se necessário
      }
      prevScrollpos = currentScrollPos;
  }
});

// FUNÇÃO DAS PAGINAS
document.addEventListener('DOMContentLoaded', function() {
  const navLinks = document.querySelectorAll('.nav-links a');

  navLinks.forEach(link => {
    link.addEventListener('click', function(e) {
      const href = this.getAttribute('href');
      if (href !== '#') {
        e.preventDefault();
        window.location.href = href;
      }
    });
  });
})

//FUNÇÃO WIDGET ZOOM
document.addEventListener('DOMContentLoaded', function() {
  const zoomToggle = document.querySelector('.zoom-toggle');
  const zoomOptions = document.querySelector('.zoom-options');
  const zoomInButton = document.querySelector('.zoom-in');
  const zoomOutButton = document.querySelector('.zoom-out');
  const mainContent = document.querySelector('.main-content'); // Seleciona o conteúdo principal

  // Alterna a visibilidade das opções de zoom
  zoomToggle.addEventListener('click', function() {
      zoomOptions.style.display = zoomOptions.style.display === 'block' ? 'none' : 'block';
  });

  // Função para ajustar o zoom do conteúdo principal usando a propriedade `zoom`
  function setZoom(scale) {
      mainContent.style.zoom = scale; // Usa a propriedade `zoom` para ajustar o nível de zoom
  }

  let currentZoom = 1; // Zoom padrão (100%)

  // Evento de clique para aumentar o zoom
  zoomInButton.addEventListener('click', function() {
      if (currentZoom < 2) { // Limite superior do zoom (200%)
          currentZoom += 0.1;
          setZoom(currentZoom);
      }
  });

  // Evento de clique para diminuir o zoom
  zoomOutButton.addEventListener('click', function() {
      if (currentZoom > 0.5) { // Limite inferior do zoom (50%)
          currentZoom -= 0.1;
          setZoom(currentZoom);
      }
  });
});

//FUNÇÃO SIDEBAR
document.getElementById('menu-button').addEventListener('click', function() {
  document.getElementById('sidebar').classList.toggle('active');
  document.querySelector('.nav-links').classList.toggle('hidden');
});