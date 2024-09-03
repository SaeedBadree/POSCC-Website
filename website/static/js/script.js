
document.addEventListener('scroll', function() {
  const aboutSection = document.querySelector('.about-section');
  const linkItems = document.querySelectorAll('.link-item');

  const triggerPoint = window.innerHeight * 0.7; // Adjust as necessary

  // Check About Section
  if (aboutSection.getBoundingClientRect().top < triggerPoint) {
      aboutSection.classList.add('scrolled');
  }

  // Check Link Items
  linkItems.forEach(item => {
      if (item.getBoundingClientRect().top < triggerPoint) {
          item.classList.add('scrolled');
      }
  });
});



