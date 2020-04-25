var xcordsDemo =[50, 75 , 100 , 120, 140, 120, 90 , 80 , 100, 130, 160, 190 , 240 , 280, 315, 335, 350 , 315 , 300, 280, 280, 280, 280, 280, 280, 266, 100, 75, 60 ,50];
var ycordsDemo =[50, 50 , 50, 75, 90, 100, 100 , 125 , 140, 140, 140, 140 , 140 , 140, 140, 155, 175 , 200 , 220, 200, 175, 150, 120, 100, 75, 100, 400, 360, 300, 100];
var theThing = document.querySelector('#instrearthe');
var bluegrab = document.getElementById('bluecrab');
var redcrab = document.getElementById('redcrab');
var greencrab = document.getElementById('greencrab');
var RprevpositionL = 112; RprevpositionT = 20;
var GprevpositionL = 382; GprevpositionT = 340;
var BprevpositionL = 486; BprevpositionT= 340;
var currentXPosition=50; currentYPosition=50; counter=0;
var i=0;
var Xdiff = xcordsDemo[i+1] - xcordsDemo[i];
var Ydiff = ycordsDemo[i+1] - ycordsDemo[i] ;
var numberSteps = parseInt(Math.abs(xcordsDemo[i+1] - xcordsDemo[i])/25);
var length=ycordsDemo.length*2;

for(var j=1; j < length;j++){
    if ( j >= ycordsDemo.length ){
        x = parseInt(Math.random()*500);
        y = parseInt(Math.random()*400);
        xcordsDemo[j] = x;
        ycordsDemo[j] = y;
    } else{
        xcordsDemo[j] = xcordsDemo[j] + parseInt(Math.random()*100)
    }
}

// Moving the Earthe for automatic operation
function moveEarhte(){
    data=$.getJSON("/static/home/js/data.json",function(data){
        if(data["Operation"]["Auto"]=="1"){
            /*
            counter = counter+1;

            var signL = Xdiff>0 ? +1 : -1;
            var signT = Ydiff>0 ? +1 : -1;

            xPos=currentXPosition+25*signL;
            yPos=currentXPosition+25*signT;

            console.log(xPos,yPos);
            var MoveApart=findNearCrab(xPos,yPos)
            xPos = (Xdiff>0) ? xPos+MoveApart : xPos-MoveApart;
            yPos = (Ydiff>0) ? yPos+MoveApart : yPos-MoveApart;
            
            if(Math.abs(xPos - xcordsDemo[i]) > 25){
                numberSteps++;
                console.log(numberSteps);
            }

            if (numberSteps==counter){
                i++;
                Xdiff = xcordsDemo[i+1] - xcordsDemo[i];
                Ydiff = ycordsDemo[i+1] - ycordsDemo[i];
                numberSteps = parseInt(Math.abs(xcordsDemo[i+1] - xcordsDemo[i])/25);
                counter=0;
                console.log("Success");
            }
            theThing.style.left = xPos + "px";
            theThing.style.top = yPos + "px";
            
            */
            i++;
            var MoveApart=findNearCrab(xcordsDemo[i],ycordsDemo[i])
            Xdiff = xcordsDemo[i+1] - xcordsDemo[i];
            Ydiff = ycordsDemo[i+1] - ycordsDemo[i] ;
            xcordsDemo[i] = (Xdiff>0) ? xcordsDemo[i] + MoveApart : xcordsDemo[i] - MoveApart;
            ycordsDemo[i] = (Ydiff>0) ? ycordsDemo[i] + MoveApart : ycordsDemo[i] - MoveApart;

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

            document.getElementById("locEarthe").innerText="X-axis: " + parseInt(xcordsDemo[i]) + " Y-Axis: " + parseInt(xcordsDemo[i]);
            document.getElementById("TlocEarthe").innerText="X-axis: " + parseInt(xcordsDemo[i]) + " Y-Axis: " + parseInt(xcordsDemo[i]);

            i = i==xcordsDemo.length ? -1 : i;
        
        }
        
    })
}

setInterval(moveEarhte,2500)

function movecrab(){
    signforLeft = (Math.random()>0.5) ? -1 : 1;
    signforTop = (Math.random()>0.5) ? -1 : 1;
    randomNum = Math.random()*5;
    if (randomNum<1.5){
        BprevpositionL =  BprevpositionL + signforLeft*parseInt(Math.random()*20);
        BprevpositionT =  BprevpositionT + signforTop*parseInt(Math.random()*20);
        bluegrab.style.left = (BprevpositionL > 0 && BprevpositionL < 500) ? BprevpositionL + "px" : bluegrab.style.left;
        bluegrab.style.top = (BprevpositionT > 0 && BprevpositionT < 440) ? BprevpositionT + "px" : bluegrab.style.top;
    } else if(randomNum<3.5){
        RprevpositionL =  RprevpositionL + signforLeft*parseInt(Math.random()*20);
        RprevpositionT =  RprevpositionT + signforTop*parseInt(Math.random()*20);
        redcrab.style.left = (RprevpositionL > 0 && RprevpositionL < 500) ? RprevpositionL + "px" : redcrab.style.left;
        redcrab.style.top = (RprevpositionT > 0 && RprevpositionT < 440) ? RprevpositionT + "px" : redcrab.style.top;
    } else {
        GprevpositionL =  GprevpositionL + signforLeft*parseInt(Math.random()*20);
        GprevpositionT =  GprevpositionT + signforTop*parseInt(Math.random()*20);
        greencrab.style.left = (GprevpositionL > 0 && GprevpositionL < 500) ? GprevpositionL + "px" : greencrab.style.left;
        greencrab.style.top = (GprevpositionT > 0 && GprevpositionT < 440) ? GprevpositionT + "px" : greencrab.style.top;
    }
}

setInterval(movecrab,1000   )

function findNearCrab(xPos,yPos){
    var difference;
    if(Math.abs(BprevpositionL-xPos) < 45 || Math.abs(BprevpositionT-yPos) < 45){
        difference=Math.sqrt(Math.abs(BprevpositionL-xPos)^2 + Math.abs(BprevpositionT-yPos)^2);
    } else if(Math.abs(RprevpositionL-xPos) < 45 || Math.abs(RprevpositionT-yPos)<45){
        difference=Math.sqrt(Math.abs(RprevpositionL-xPos)^2 + Math.abs(RprevpositionT-yPos)^2);
    } else if (Math.abs(GprevpositionL-xPos) < 45 || Math.abs(GprevpositionT-yPos)<45){
        difference=Math.sqrt(Math.abs(GprevpositionL-xPos)^2 + Math.abs(GprevpositionT-yPos)^2);
    } else {
        difference=0
    }

    return difference
}