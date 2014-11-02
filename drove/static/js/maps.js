var map;

function initialize() {
  var mapOptions = {
    zoom: 16,
    disableDefaultUI :false,
  };
  map = new google.maps.Map(document.getElementById('map-canvas'),
      mapOptions);

  if(navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(function(position) {
      var pos = new google.maps.LatLng(position.coords.latitude,
                                       position.coords.longitude);

      var infowindow = new google.maps.InfoWindow({
        map: map,
        position: pos,
        content: 'Aqui te encuentras'
      });

      map.setCenter(pos);
    }, function() {
      handleNoGeolocation(true);
    });
    
    
    var lat1 = new google.maps.LatLng(19.339815394277245,-99.19013857841492);
    var marker1 = new google.maps.Marker({
        position: lat1,
        title:""
    });
    marker1.setMap(map);
    
    var lat2 = new google.maps.LatLng(19.342781529114543,-99.18906569480896);
    var marker2 = new google.maps.Marker({
        position: lat2,
        title:""
    });
    marker2.setMap(map);
    
    var lat3 = new google.maps.LatLng(19.34710409326495,-99.18740272521973);
    var marker3 = new google.maps.Marker({
        position: lat3,
        title:""
    });
    marker3.setMap(map);
    
    var lat4 = new google.maps.LatLng(19.349857517054836,-99.18649077415466);
    var marker4 = new google.maps.Marker({
        position: lat4,
        title:""
    });
    marker4.setMap(map);
    
    var lat5 = new google.maps.LatLng(19.355799490191945,-99.18460249900816);
    var marker5 = new google.maps.Marker({
        position: lat5,
        title:""
    });
    marker5.setMap(map);
    
    var lat6 = new google.maps.LatLng(19.35855276721877,-99.18373346328734);
    var marker6 = new google.maps.Marker({
        position: lat6,
        title:""
    });
    marker6.setMap(map);
    
    var lat7 = new google.maps.LatLng(19.361943687911438,-99.18264985084534);
    var marker7 = new google.maps.Marker({
        position: lat7,
        title:""
    });
    marker7.setMap(map);
    
    var lat8 = new google.maps.LatLng(19.36735889262276,-99.18189883232117);
    var marker8 = new google.maps.Marker({
        position: lat8,
        title:""
    });
    marker8.setMap(map);
    
    var lat9 = new google.maps.LatLng(19.372591732606086,-99.17916297912596);
    var marker9 = new google.maps.Marker({
        position: lat9,
        title:""
    });
    marker9.setMap(map);
    
    var lat10 = new google.maps.LatLng(19.376437813458118,-99.177907705307);
    var marker10 = new google.maps.Marker({
        position: lat10,
        title:""
    });
    marker10.setMap(map);
    
    var lat11 = new google.maps.LatLng(19.3800915061677,-99.17666316032408);
    var marker11 = new google.maps.Marker({
        position: lat11,
        title:""
    });
    marker11.setMap(map);

    
    
  } else {
    // Browser doesn't support Geolocation
    handleNoGeolocation(false);
  }
  
  
  
}

function handleNoGeolocation(errorFlag) {
  if (errorFlag) {
    var content = 'Error: el servicio de geolocalizacion fallo.';
  } else {
    var content = 'Error: Tu navegador no soporta el servicio.';
  }

  var options = {
    map: map,
    position: new google.maps.LatLng(60, 105),
    content: content
  };

  var infowindow = new google.maps.InfoWindow(options);
  map.setCenter(options.position);
}



////////////


google.maps.event.addDomListener(window, 'load', initialize);

