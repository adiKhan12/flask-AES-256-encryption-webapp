// Add active class to current navigation link

var currentUrl = window.location.href;
var navLinks = document.querySelectorAll('nav a');

for (var i = 0; i < navLinks.length; i++) {
  if (navLinks[i].href === currentUrl) {
    navLinks[i].classList.add('active');
  }
}
