var xcordsDemo =[50, 75 , 100 , 120, 140, 120, 90 , 80 , 100, 130, 160, 190 , 240 , 280, 315, 335, 350 , 315 , 300, 280, 280, 280, 280, 280, 280, 266, 100, 75, 60 ,50];
var ycordsDemo =[50, 50 , 50, 75, 90, 100, 100 , 125 , 140, 140, 140, 140 , 140 , 140, 140, 155, 175 , 200 , 220, 200, 175, 150, 120, 100, 75, 100, 400, 360, 300, 100];
var theThing = document.querySelector('#instrearthe');
var blueleft = document.getElementById('bluecrab').style.left;
var bluetop = document.getElementById('bluecrab').style.top;
var redleft = document.getElementById('redcrab').style.left;
var redtop = document.getElementById('redcrab').style.top;
var greenleft = document.getElementById('greencrab').style.left;
var greentop = document.getElementById('greencrab').style.top;
var i=0;
var length=ycordsDemo.length*2;

for(var j=0; j < length;j++){
    if ( j >= ycordsDemo.length ){
        x = parseInt(Math.random()*500);
        y = parseInt(Math.random()*400);
        xcordsDemo[j] = x;
        ycordsDemo[j] = y;
    } else{
        xcordsDemo[j] = xcordsDemo[j] + parseInt(Math.random()*100)
    }
}
function moveEarhte(){
    data=$.getJSON("/static/home/js/data.json",function(data){
        if(data["Operation"]["Auto"]=="1"){
            i++;
            theThing.style.left = xcordsDemo[i] + "px";
            theThing.style.top = ycordsDemo[i] + "px";
            
            //console.log(i)
            if( xcordsDemo[i]>300 && ycordsDemo[i] < 250){
                document.getElementById("tideenv").innerText= "Less than 1 metre";
                document.getElementById("tideToggle").style.animation = "blinker 3s infinite 0s";

            } else{
                document.getElementById("tideenv").innerText= "More than 1 metre";
                document.getElementById("tideToggle").style.animation = "none";

            }

            document.getElementById("locEarthe").innerText="X-axis: " + xcordsDemo[i] + " Y-Axis: " + ycordsDemo[i];
            document.getElementById("TlocEarthe").innerText="X-axis: " + xcordsDemo[i] + " Y-Axis: " + ycordsDemo[i];

            i = i==xcordsDemo.length ? -1 : i;
        
        }
        
    })
}

setInterval(moveEarhte,700)

function movecrab(){
    signforLeft = (Math.random()>0.5) ? -1 : 1;
    signforTop = (Math.random()>0.5) ? -1 : 1;
    randomNum = Math.random()*5;
    if (randomNum<1.5){
        document.getElementById('bluecrab').style.left =  blueleft + parseInt(Math.random()*50) + "px";
        document.getElementById('bluecrab').style.top =  bluetop + parseInt(Math.random()*50) + "px" ;
    } else if(randomNum<3.5){
        document.getElementById('redcrab').style.left = redleft + parseInt(Math.random()*50) +"px";
        document.getElementById('redcrab').style.top = redtop + parseInt(Math.random()*50) +"px" ;
    } else {
        document.getElementById('greencrab').style.left = greentop + parseInt(Math.random()*50) +"px";
        document.getElementById('greencrab').style.top = greenleft + parseInt(Math.random()*50) +"px" ;
    }
    console.log('test')
}

setInterval(movecrab,200)
