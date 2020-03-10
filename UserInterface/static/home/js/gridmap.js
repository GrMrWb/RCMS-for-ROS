var theThing = document.querySelector('#instrearthe');
var container = document.querySelector('#gridmap');
var xPosition=50+(theThing.clientWidth / 2);
var yPosition=50+(theThing.clientHeight / 2);

container.addEventListener("click",getClickPosition,false);
 
function getClickPosition(e) {
    
    prexPosition=xPosition;
    preyPosition=yPosition;

    var parentPosition = getPosition(e.currentTarget);
    xPosition = e.clientX - parentPosition.x - (theThing.clientWidth / 2);
    yPosition = e.clientY - parentPosition.y - (theThing.clientHeight / 2);

    //Constrain the map
    xPosition = xPosition < 0 ? 0 : xPosition;
    yPosition = yPosition < 0 ? 0 : yPosition;

    xPosition = xPosition > 940 ? 940 : xPosition;
    yPosition = yPosition > 500 ? 500 : yPosition;

    var xmlhttp1 = new XMLHttpRequest();
    xmlhttp1.open("GET", 'http://localhost:8000/instruction/'+ xPosition+'/'+ yPosition, true);
    xmlhttp1.send();

    theThing.style.left = xPosition + "px";
    theThing.style.top = yPosition + "px";

    document.getElementById("curearthe").style.left = prexPosition+ 100 + "px";
    document.getElementById("curearthe").style.top= preyPosition + 50 + "px";
    document.getElementById("curearthe").style.display= "block";
    setTimeout(donothing(), 100);
    var xmlhttp = new XMLHttpRequest();
    xmlhttp.open("GET", 'http://localhost:8000/current/'+ prexPosition+'/'+ preyPosition, true);
    xmlhttp.send();
}



function donothing() {
    //
}
 
// Helper function to get an element's exact position
function getPosition(el) {
    var xPos = 0;
    var yPos = 0;
    
    while (el) {
        if (el.tagName == "BODY") {
            // deal with browser quirks with body/window/document and page scroll
            var xScroll = el.scrollLeft || document.documentElement.scrollLeft;
            var yScroll = el.scrollTop || document.documentElement.scrollTop;
        
            xPos += (el.offsetLeft - xScroll + el.clientLeft);
            yPos += (el.offsetTop - yScroll + el.clientTop);
        } else {
            // for all other non-BODY elements
            xPos += (el.offsetLeft - el.scrollLeft + el.clientLeft);
            yPos += (el.offsetTop - el.scrollTop + el.clientTop);
        }
    
        el = el.offsetParent;
    }
    return {
        x: xPos,
        y: yPos
    };
}