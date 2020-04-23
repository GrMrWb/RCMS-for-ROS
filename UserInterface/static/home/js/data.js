var pastversion="1";
var data

function updateData(){
    $.getJSON("/static/home/js/warning.json",function(data){
        //Environmental Data
        document.getElementById("warnenv").innerText= data["Warning"]["seagull"]== "True" ? "SeaGulls in Vicinity" : "No Env Warning";
        document.getElementById("warnToggle").style.animation = data["Warning"]["seagull"]== "True" ? "blinker 3s infinite 0s" : "none";
        delete data;
    });

    $.getJSON("/static/home/js/data.json",function(data){
        if (data["v"]!=pastversion){
            if (data["Operation"]["Auto"]=="1"){
                $.getJSON("/static/home/js/warning.json",function(data){
                    //Environmental Data
                    document.getElementById("warnenv").innerText= data["Warning"]["seagull"]== "True" ? "SeaGulls in Vicinity" : "No Env Warning";
                    document.getElementById("warnToggle").style.animation = data["Warning"]["seagull"]== "True" ? "blinker 3s infinite 0s" : "none";
                    document.getElementById("tideenv").innerText= data["Warning"]["tide"]== "True" ? "Tide Less than 1 metre" : "Tide More than 1 metre";
                    document.getElementById("tideToggle").style.animation = data["Warning"]["tide"]== "True" ? "blinker 3s infinite 0s" : "none";           
                    delete data;
                });
            }
            //EarthE Data
            document.getElementById("PiStat").innerText = data["TriTrackDataMic"]["PiStat"] == "1" ? "Not Available" : "Available Processing";
            document.getElementById("Pi4procTri").innerText = data["TriTrackDataMic"]["Pi4procTri"]+" %";
            document.getElementById("BrdStat").innerText = data["TriTrackDataMic"]["BrdStat"]== "1" ? "Not Available" : "Available Processing";
            document.getElementById("BrdProc").innerText = data["TriTrackDataMic"]["BrdProc"]+" %";
            document.getElementById("RosStat").innerText = data["TriTrackDataMic"]["RosStat"]== "1" ? "Not Available" : "Available Processing";
            document.getElementById("ROSproc").innerText = data["TriTrackDataMic"]["ROSproc"]+" %";
            document.getElementById("Operation").innerText = data["Operation"]["Auto"]== "1" ? "Automatic" : "Manual";

            // PoweBoard
            document.getElementById("Consumption").innerText = data["TriTrackPowerBoard"]["Consumption"] + ' W';
            document.getElementById("Consumptiona").innerText = data["TriTrackPowerBoard"]["Consumption"] + ' W';
            document.getElementById("CapA").innerHTML = '<image style="height:25px;" src=/static/home/src/' + data["TriTrackPowerBoard"]["CapA"]+'.svg />';
            document.getElementById("CapB").innerHTML = '<image style="height:25px;" src=/static/home/src/' + data["TriTrackPowerBoard"]["CapB"]+'.svg />';
            document.getElementById("TCapA").innerHTML = '<image style="height:25px;" src=/static/home/src/' + data["TriTrackPowerBoard"]["CapA"]+'.svg />';
            document.getElementById("TCapB").innerHTML = '<image style="height:25px;" src=/static/home/src/' + data["TriTrackPowerBoard"]["CapB"]+'.svg />';
            
            //Sorting Rig Data
            document.getElementById("PiStatSort").innerText = data["SortRigPerform"]["PiStat"] == "1" ? "Not Available" : "Available Processing";
            document.getElementById("Pi4procTriSor").innerText = data["SortRigPerform"]["Pi4procTri"]+" %";
            document.getElementById("ArdStat").innerText = data["SortRigPerform"]["ArdStat"]== "1" ? "Not Available" : "Available Processing";
            document.getElementById("ArdProc").innerText = data["SortRigPerform"]["ArdProc"]+" %";
            document.getElementById("PrdStat").innerText = data["SortRigPerform"]["PrdStat"]== "1" ? "Not Available" : "Available Processing";
            document.getElementById("PrbProc").innerText = data["SortRigPerform"]["PrbProc"]+" %";

            //Rubbish
            tot=parseInt(data["Rubbish"]["BinA"])+parseInt(data["Rubbish"]["BinB"])+parseInt(data["Rubbish"]["BinC"])+parseInt(data["Rubbish"]["BinD"])
            document.getElementById("totRub").innerText = data["Rubbish"]["totRub"];
            document.getElementById("colRub").innerText = data["Rubbish"]["ColRub"];
            document.getElementById("SortRub").innerText = tot;
            document.getElementById("BinA").innerText = data["Rubbish"]["BinA"];
            document.getElementById("BinB").innerText = data["Rubbish"]["BinB"];
            document.getElementById("BinC").innerText = data["Rubbish"]["BinC"];
            document.getElementById("BinD").innerText = data["Rubbish"]["BinD"];
            
            //Toast Rubbish
            document.getElementById("TcolRub").innerText = data["Rubbish"]["ColRub"];
            document.getElementById("TSortRub").innerText = tot;
            document.getElementById("TBinA").innerText = data["Rubbish"]["BinA"];
            document.getElementById("TBinB").innerText = data["Rubbish"]["BinB"];
            document.getElementById("TBinC").innerText = data["Rubbish"]["BinC"];
            document.getElementById("TBinD").innerText = data["Rubbish"]["BinD"];

            if (data["Operation"]["Man"]==data["Operation"]["Auto"]){
                document.getElementById("errorProc").innerHTML='<p>ERROR IN THE PROCESS</p><p>Giving the following priority</p><ul><li>Controller</li><li>Autonomous</li><li>GridMap</li></ul>';
            }
            //imageExists();
            pastversion=data["v"];
            delete data
        }
    })  
}
setInterval(updateData,2000);

function throttleAuto(){
    test= parseInt(Math.random()*100) +"%";
    document.getElementById("percentageL").style.height= test;
    document.getElementById("percentageR").style.height= test;
}

//setInterval(throttleAuto,500);

function trashAuto(){
    randItem=Math.random()*5

    if (randItem<1){
        document.getElementById("percentagePlastic").style.width= "0%";
        document.getElementById("percentageMetal").style.width= "100%";
        document.getElementById("percentagePaper").style.width= "100%";
        document.getElementById("percentageUnable").style.width= "100%";
        document.getElementById("trashident").innerHTML = '<center><image style="height:200px;" src="/static/home/src/Plastic-Bottle.PNG" />';
        
    } else if (randItem<2){
        document.getElementById("percentagePlastic").style.width= "100%";
        document.getElementById("percentageMetal").style.width= "0%";
        document.getElementById("percentagePaper").style.width= "100%";
        document.getElementById("percentageUnable").style.width= "100%";
        document.getElementById("trashident").innerHTML = '<center><image style="height:200px;" src="/static/home/src/Can.PNG" />';
    } else if (randItem<3){
        document.getElementById("percentagePlastic").style.width= "100%";
        document.getElementById("percentageMetal").style.width= "100%";
        document.getElementById("percentagePaper").style.width= "100%";
        document.getElementById("percentageUnable").style.width= "0%";
        document.getElementById("trashident").innerHTML = '<center><image style="height:200px;" src="/static/home/src/.PNG" />';
    } else {
        document.getElementById("percentagePlastic").style.width= "100%";
        document.getElementById("percentageMetal").style.width= "100%";
        document.getElementById("percentagePaper").style.width= "0%";
        document.getElementById("percentageUnable").style.width= "100%";
        document.getElementById("trashident").innerHTML = '<center><image style="height:200px;" src="/static/home/src/silver-ring-pull-end.PNG" />';
    }
}

setInterval(trashAuto,2500);
