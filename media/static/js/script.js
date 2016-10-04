var map;
var directionService = new google.maps.DirectionsService();
var directionDisplay;
var geocoder;

//direction will be draggable
var directionOptions = {
  draggable: true
};

function initializeMap(){
  directionDisplay = new google.maps.DirectionsRenderer(directionOptions);
  var latlng = new google.maps.LatLng(39.57, 32.51);
  var mapOptions = {
    zoom: 4,
    center: latlng,
    mapTypeId: google.maps.MapTypeId.ROADMAP
  };
  map = new google.maps.Map(document.getElementById("map"), mapOptions);
  google.maps.event.addListener(directionDisplay, "directions_changed", function(){
     saveResultAsStr(directionDisplay.directions);
  });

  directionDisplay.setMap(map);
  geocoder = new google.maps.Geocoder();
}

function saveResultAsStr(result){
    var legs = result.routes[0].legs[0];
    var route = [];

    for(var i = 0; i < legs.steps.length; i++){
        route.push(legs.steps[i].start_point.lat() + "," + legs.steps[i].start_point.lng());
    }

    $('#id_route').val(route.join("\n"));
}

function findPosition(address, callback){
    geocoder.geocode({'address': address}, function(results, status){
        if(status = google.maps.GeocoderStatus.OK){
            var position = results[0].geometry.location;
            callback(position);
        }
    });
}



function searchRoute(){
    var start = $("#id_where").val();
    var to = $("#id_to").val();
    alert(start+"      "+to);

    geocoder.geocode({'address': start}, function(results, status){
        if(status = google.maps.GeocoderStatus.OK){
            var start_position = results[0].geometry.location;
            geocoder.geocode({'address': to}, function(results, status){
                if(status = google.maps.GeocoderStatus.OK){
                    var end_position = results[0].geometry.location;

                    $('#id_start').val(start_position.lat()+","+start_position.lng());
                    $('#id_end').val(end_position.lat()+","+end_position.lng());
                    $('#searchRouteForm').submit();
                }});
        }});

}

function showRouteOnMap(){
  var start = $("#where").val();
  var end = $("#to").val();
  var request = {
    origin: start,
    destination: end,
    travelMode: google.maps.TravelMode.DRIVING
  };

  directionService.route(request, function(result, status){
      if (status == google.maps.DirectionsStatus.OK){
        $("#createRouteSubmit").attr('disabled', false);
        directionDisplay.setDirections(result);
      }
  });

}
$(document).ready(function (){
    $("#createRouteSubmit").attr('disabled', true);
    $("#show").click(showRouteOnMap);
    $("#sroute").click(searchRoute);
});





















