document.addEventListener('DOMContentLoaded', function() {
    // Initialize map centered on San Andrés Cholula
    const map = new google.maps.Map(document.getElementById('map'), {
        center: { lat: 19.0514, lng: -98.2839 },
        zoom: 15
    });

    // Handle form submission
    const form = document.getElementById('contactForm');
    form.addEventListener('submit', function(event) {
        event.preventDefault();
        alert('Formulario enviado. Nos pondremos en contacto contigo pronto.');
        form.reset();
    });
});