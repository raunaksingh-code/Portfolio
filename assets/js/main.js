document.addEventListener('DOMContentLoaded', function () {

  /* ---------- Navbar scroll state ---------- */
  var navbar = document.getElementById('navbar');
  if (navbar) {
    function onScroll() {
      if (window.scrollY > 12) {
        navbar.classList.add('is-scrolled');
      } else {
        navbar.classList.remove('is-scrolled');
      }
    }
    document.addEventListener('scroll', onScroll, { passive: true });
    onScroll();
  }

  /* ---------- Mobile nav toggle ---------- */
  var navToggle = document.getElementById('navToggle');
  var navLinks = document.getElementById('navLinks');
  if (navToggle && navLinks) {
    navToggle.addEventListener('click', function () {
      navToggle.classList.toggle('is-open');
      navLinks.classList.toggle('is-open');
    });
    navLinks.querySelectorAll('a').forEach(function (link) {
      link.addEventListener('click', function () {
        navToggle.classList.remove('is-open');
        navLinks.classList.remove('is-open');
      });
    });

    /* ---------- Scrollspy active nav link ---------- */
    var sections = Array.prototype.slice.call(document.querySelectorAll('section[id]'));
    var navAnchors = Array.prototype.slice.call(navLinks.querySelectorAll('a'));

    function updateActiveLink() {
      var scrollPos = window.scrollY + 120;
      var current = sections[0];
      sections.forEach(function (sec) {
        if (sec.offsetTop <= scrollPos) current = sec;
      });
      navAnchors.forEach(function (a) {
        var isActive = a.getAttribute('href') === '#' + current.id;
        a.classList.toggle('is-active', isActive);
      });
    }
    document.addEventListener('scroll', updateActiveLink, { passive: true });
    updateActiveLink();
  }

  /* ---------- Reveal on scroll ---------- */
  var revealEls = document.querySelectorAll('.reveal');
  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add('is-visible');
          io.unobserve(entry.target);
        }
      });
    }, { threshold: 0.12 });
    revealEls.forEach(function (el) { io.observe(el); });
  } else {
    revealEls.forEach(function (el) { el.classList.add('is-visible'); });
  }

});
