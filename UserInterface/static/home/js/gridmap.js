var theThing = document.querySelector('#instrearthe');
var container = document.querySelector('#gridmap');
var xPosition = 50+(theThing.clientWidth / 2);
var yPosition = 50+(theThing.clientHeight / 2);
var prexPosition = xPosition;
var preyPosition = yPosition;
var data

container.addEventListener("click",getClickPosition,false);

function getClickPosition(e) {
   
//    data=$.getJSON("/static/home/js/data.json",function(data){
//        if(data["Operation"]["Man"]=="1"){
            
            document.getElementById("curearthe").style.display= "none";
            var parentPosition = getPosition(e.currentTarget);

            xPosition = e.clientX - parentPosition.x - (theThing.clientWidth / 2);
            yPosition = e.clientY - parentPosition.y - (theThing.clientHeight / 2);

            //Constrain the map
            xPosition = xPosition < 0 ? 0 : xPosition;
            yPosition = yPosition < 0 ? 0 : yPosition;
    
            xPosition = xPosition > 590 ? 580 : xPosition;
            yPosition = yPosition > 420 ? 420 : yPosition;

            if (xPosition > 430 && yPosition<230){
                xPosition=430;
                yPosition-230;
            }
            if (xPosition>390 && yPosition<260){
                document.getElementById("tideenv").innerText= "Less than 1 metre";
                document.getElementById("tideToggle").style.animation = "blinker 3s infinite 0s";

            } else{
                document.getElementById("tideenv").innerText= "More than 1 metre";
                document.getElementById("tideToggle").style.animation = "none";

            }
            theThing.style.left = xPosition + "px";
            theThing.style.top = yPosition + "px";

            document.getElementById("curearthe").style.display= "block";
            if (document.getElementById("curearthe").style.left == prexPosition){
                document.getElementById("curearthe").style.left = prexPosition + "px";
                document.getElementById("curearthe").style.top= preyPosition - 50 + "px";
                document.getElementById("curearthe").style.display= "block";
                console.log(prexPosition,preyPosition);
            }

            if( document.getElementById("curearthe").style.display!="none"){
                document.getElementById("locEarthe").innerText="X-axis: " + theThing.style.left + " Y-Axis: " + theThing.style.top;
                document.getElementById("TlocEarthe").innerText="X-axis: " + theThing.style.left + " Y-Axis: " + theThing.style.top;

            }

            var xmlhttp = new XMLHttpRequest();
            xmlhttp.open( 'GET'  , 'http://127.0.0.1:8000/cords/'+ xPosition + '/'+ yPosition + '/'+ parseInt(prexPosition) +'/'+ parseInt(preyPosition), true);
            xmlhttp.send();
            //xmlhttp.abort();
//        }
//    });
}

function moveObject(){
    throttle= (xPosition - prexPosition) > 0 ? xPosition - prexPosition : prexPosition - xPosition;
    throttle= 100 - (throttle/6);
    
    test= parseInt(throttle) +"%";
    prexPosition = prexPosition + (xPosition - prexPosition)/10;
    preyPosition = preyPosition + (yPosition - preyPosition)/10;

    if( document.getElementById("curearthe").style.display!="none"){
        document.getElementById("curearthe").style.left = prexPosition + "px";
        document.getElementById("curearthe").style.top= preyPosition - 50 + "px";
        //Adding Location
        document.getElementById("locEarthe").innerText="X-axis: " + parseInt(prexPosition) + " Y-Axis: " + parseInt(preyPosition);
        document.getElementById("TlocEarthe").innerText="X-axis: " + parseInt(prexPosition) + " Y-Axis: " + parseInt(preyPosition);
    }
    
    document.getElementById("percentageL").style.height= test;
    document.getElementById("percentageR").style.height= test;

}

setInterval(moveObject,200)

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
