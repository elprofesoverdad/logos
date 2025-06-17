function updateLandingPageClass() {
  const body = document.body;
  const marker = document.querySelector('[data-landing-page]');
  const isLanding = body.classList.contains('landing-page');
  // Sincroniza la clase landing-page
  if (marker && !isLanding) {
    body.classList.add('landing-page');
    console.log('[LandingPage] Clase landing-page AGREGADA al body');
  } else if (!marker && isLanding) {
    body.classList.remove('landing-page');
    console.log('[LandingPage] Clase landing-page REMOVIDA del body');
  }
}

// Ejecuta al cargar y en cada navegación interna
if (typeof window !== 'undefined') {
  document.addEventListener('DOMContentLoaded', updateLandingPageClass);
  document.addEventListener('pjax:success', updateLandingPageClass);
}