(function(){
  const links = document.querySelectorAll('a[href^="#"]');
  links.forEach(link => link.addEventListener('click', e => {
    const id = link.getAttribute('href');
    if (id && id.length > 1) {
      const el = document.querySelector(id);
      if (el) {
        e.preventDefault();
        el.scrollIntoView({ behavior: 'smooth', block: 'start' });
      }
    }
  }));
  const y = document.getElementById('year');
  if (y) y.textContent = new Date().getFullYear();

  // Fallback for profile image
  const profileImg = document.querySelector('.profile-photo');
  if (profileImg) {
    profileImg.addEventListener('error', () => {
      const fallback = profileImg.getAttribute('data-fallback') || 'assets/img/profile-fallback.svg';
      if (profileImg.src.indexOf(fallback) === -1) profileImg.src = fallback;
    }, { once: true });
  }
})();
