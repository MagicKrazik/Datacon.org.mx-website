document.addEventListener('DOMContentLoaded', function() {
    const menu = document.querySelector('.navbar-menu');
    const menuToggle = document.querySelector('.navbar-toggle');
    const navLinks = document.querySelectorAll('.navbar-link');
    const dropdowns = document.querySelectorAll('.navbar-dropdown');

    menuToggle.addEventListener('click', mobileMenu);
    navLinks.forEach(n => n.addEventListener('click', closeMenu));

    function mobileMenu() {
        menuToggle.classList.toggle('active');
        menu.classList.toggle('active');
    }

    function closeMenu() {
        menuToggle.classList.remove('active');
        menu.classList.remove('active');
    }

    dropdowns.forEach(dropdown => {
        dropdown.addEventListener('click', function(e) {
            if (window.innerWidth < 960) {
                e.preventDefault();
                this.classList.toggle('active');
            }
        });
    });
});