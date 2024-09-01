var prevScrollpos = window.pageYOffset;
window.onscroll = function() {
var currentScrollPos = window.pageYOffset;
  if (prevScrollpos > currentScrollPos) {
    document.getElementById("navbar").style.top = "0";
  } else {
    document.getElementById("navbar").style.top = "-100px";
  }
  prevScrollpos = currentScrollPos;
}

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

document.addEventListener('DOMContentLoaded', function() {
  const zoomToggle = document.querySelector('.zoom-toggle');
  const zoomOptions = document.querySelector('.zoom-options');
  const zoomInButton = document.querySelector('.zoom-in');
  const zoomOutButton = document.querySelector('.zoom-out');

  zoomToggle.addEventListener('click', function() {
      zoomOptions.style.display = zoomOptions.style.display === 'block' ? 'none' : 'block';
  });

  function setZoom(scale) {
      document.body.style.transform = `scale(${scale})`;
      document.body.style.transformOrigin = '0 0'; // Define a origem de escala
      document.body.style.width = `${100 / scale}%`; // Ajusta a largura para evitar barra de rolagem horizontal
  }

  let currentZoom = 1; 

  zoomInButton.addEventListener('click', function() {
      if (currentZoom < 2) { // Limite superior do zoom (200%)
          currentZoom += 0.1;
          setZoom(currentZoom);
      }
  });

  zoomOutButton.addEventListener('click', function() {
      if (currentZoom > 0.5) { // Limite inferior do zoom (50%)
          currentZoom -= 0.1;
          setZoom(currentZoom);
      }
  });
});
