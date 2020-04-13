var xcordsDemo =[50, 75 , 100 , 120, 140, 120, 90 , 80 , 100, 130, 160, 190 , 240 , 280, 315, 335, 350 , 315 , 300, 280, 280, 280, 280, 280, 280, 266, 100, 75, 60 ,50];
var ycordsDemo =[50, 50 , 50, 75, 90, 100, 100 , 125 , 140, 140, 140, 140 , 140 , 140, 140, 155, 175 , 200 , 220, 200, 175, 150, 120, 100, 75, 100, 400, 360, 300, 100];
var theThing = document.querySelector('#instrearthe');
var i=0;

function moveEarhte(){
    data=$.getJSON("/static/home/js/data.json",function(data){
        if(data["Operation"]["Auto"]=="1"){
            i++;
            theThing.style.left = xcordsDemo[i] + "px";
            theThing.style.top = ycordsDemo[i] + "px";
            i = i==xcordsDemo.length ? -1 : i;
            
            console.log(i)

            document.getElementById("test").innerText="X-axis: " + xcordsDemo[i] + " Y-Axis: " + xcordsDemo[i];
        
        }
        
    })
}

setInterval(moveEarhte,700)

for(var j=0; j < ycordsDemo.length;j++){
    signRand=Math.random()*4;
    if (signRand > 3){
        xcordsDemo[j] = xcordsDemo[j] + parseInt(Math.random()*20);
        ycordsDemo[j] = ycordsDemo[j] - parseInt(Math.random()*20);
    } else if(signRand > 2) {
        xcordsDemo[j] = xcordsDemo[j] - parseInt(Math.random()*20);
        ycordsDemo[j] = ycordsDemo[j] + parseInt(Math.random()*20);
    } else if(signRand > 1) {
        xcordsDemo[j] = xcordsDemo[j] - parseInt(Math.random()*20);
        ycordsDemo[j] = ycordsDemo[j] - parseInt(Math.random()*20);
    } else {
        xcordsDemo[j] = xcordsDemo[j] - parseInt(Math.random()*20);
        ycordsDemo[j] = ycordsDemo[j] - parseInt(Math.random()*20);
    }
}

// 