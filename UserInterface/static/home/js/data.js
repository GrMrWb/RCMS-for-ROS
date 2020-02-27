var pastversion="1";
var data

function updateData(){
    $.getJSON("/static/home/js/data.json",function(data){
        if (data["v"]!=pastversion){
            //Environmental Data
            document.getElementById("warnenv").innerText= data["Warning"]["seagull"]== "1" ? "SeaGulls in Vicinity" : "NoWarning";
            document.getElementById("titled_warnenv").style.backgroundColor = data["Warning"]["seagull"]== "1" ? "orange" : "green";

            //TriTrack Data
            document.getElementById("PiStat").innerText = data["TriTrackDataMic"]["PiStat"] == "1" ? "Not Available" : "Available Processing";
            document.getElementById("Pi4procTri").innerText = data["TriTrackDataMic"]["Pi4procTri"]+" %";
            document.getElementById("BrdStat").innerText = data["TriTrackDataMic"]["BrdStat"]== "1" ? "Not Available" : "Available Processing";
            document.getElementById("BrdProc").innerText = data["TriTrackDataMic"]["BrdProc"]+" %";

            // PoweBoard
            document.getElementById("Consumption").innerText = data["TriTrackPowerBoard"]["Consumption"] + ' W';
            document.getElementById("Consumptiona").innerText = data["TriTrackPowerBoard"]["Consumption"] + ' W';
            document.getElementById("CapA").innerHTML = '<image style="height:25px;" src=/static/home/src/' + data["TriTrackPowerBoard"]["CapA"]+'.svg />';
            document.getElementById("CapB").innerHTML = '<image style="height:25px;" src=/static/home/src/' + data["TriTrackPowerBoard"]["CapB"]+'.svg />';
            
            //Rubbish
            tot=parseInt(data["Rubbish"]["BinA"])+parseInt(data["Rubbish"]["BinB"])+parseInt(data["Rubbish"]["BinC"])
            document.getElementById("totRub").innerText = data["Rubbish"]["totRub"];
            document.getElementById("colRub").innerText = parseInt(data["Rubbish"]["ColRub"])==tot ? data["Rubbish"]["ColRub"] : "Error";
            document.getElementById("SortRub").innerText = tot;
            document.getElementById("BinA").innerText = data["Rubbish"]["BinA"];
            document.getElementById("BinB").innerText = data["Rubbish"]["BinB"];
            document.getElementById("BinC").innerText = data["Rubbish"]["BinC"];
            pastversion=data["v"];
            delete data
        }
    })  
}
setInterval(updateData,2000);