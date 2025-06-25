function initMap() {
    var sanAndresCholula = {lat: 19.0515, lng: -98.2833};
    var map = new google.maps.Map(document.getElementById('map-canvas'), {
        zoom: 14,
        center: sanAndresCholula
    });

    var marker = new google.maps.Marker({
        position: sanAndresCholula,
        map: map,
        draggable: true
    });

    google.maps.event.addListener(marker, 'dragend', function(event) {
        document.querySelector('input[name="location"]').value = event.latLng.lat() + ', ' + event.latLng.lng();
    });
}