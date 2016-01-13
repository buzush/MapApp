$(function () {
    "use strict";

    var map = L.map('map');
    map.locate({setView: true, maxZoom: 16});
    var mapLink = '<a href="http://openstreetmap.org">OpenStreetMap</a>';
    L.tileLayer(
        'http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
            attribution: '&copy; ' + mapLink + ' Contributors',
            maxZoom: 18,
        }).addTo(map);


    function onLocationFound(e) {
        var radius = e.accuracy / 2;
        //L.marker(e.latlng).addTo(map)
        //    .bindPopup("You are within " + radius + " meters from this point").openPopup();
        L.circle(e.latlng, radius).addTo(map);
    }

    function onLocationError(e) {
        alert(e.message);
    }


    map.on('locationfound', onLocationFound);
    map.on('locationerror', onLocationError);

    //var marker = L.marker([31.774626752743806, 35.200505772395005]).addTo(map);

    $.get($("#map").data('url'))
        .success(function(data) {
            console.log(data);
            $.each(data.points, function(i, point) {
                var marker = L.marker([point.lng, point.lat]).addTo(map).on("click",function(e){
                    console.log(e);
                    console.log(e.layer);
                    $("#siteModal").modal();
                });
            });
        })
        .error(function(x) {
            console.error(x);
        })
});
