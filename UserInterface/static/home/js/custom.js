//clock
var monthNames = [ "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December" ]; 
var dayNames= ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]


var newDate = new Date();
newDate.setDate(newDate.getUTCDate()); 
$('#date').html(monthNames[newDate.getUTCMonth()]);
$("#day").html(newDate.getUTCDate);

setInterval( function() {
    var seconds = new Date().getUTCSeconds();
    $("#sec").html(( seconds < 10 ? "0" : "" ) + seconds);
},1000);

setInterval( function() {
    var minutes = new Date().getUTCMinutes();
    var hours = new Date().getUTCHours();
    $("#hours").html(( hours < 10 ? "0" : "" ) + hours + ':' + minutes);
    $("#timeOclock").html("ZULU");
}, 1000);

$("#dateOclock").click(function(){
    hours = new Date().getHours();
    $("#hours").html(( hours < 10 ? "0" : "" ) + hours);
    $("#timeOclock").html("LOCAL");
});