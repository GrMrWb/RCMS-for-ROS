var pastversion="1";
var data

function updateData(){
    $.getJSON("/static/home/js/warning.json",function(data){
        //Environmental Data
        document.getElementById("warnenv").innerText= data["Warning"]["seagull"]== "True" ? "SeaGulls in Vicinity" : "No Warning";
        document.getElementById("titled_warnenv").style.backgroundColor = data["Warning"]["seagull"]== "True" ? "orange" : "green";

        delete data;
    });
    $.getJSON("/static/home/js/data.json",function(data){
        if (data["v"]!=pastversion){
            
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

            //Manual and Automatic Operation
            
            document.getElementById("titled_autoen").style.backgroundColor = data["Operation"]["Auto"]== "1" ? "green" : "red";
            document.getElementById("autoen").innerText = data["Operation"]["Auto"] == "1" &&  data["Operation"]["Man"] == "0" ? "Enabled" : "Disabled";
            document.getElementById("titled_manen").style.backgroundColor = data["Operation"]["Man"] == "1" ? "green" : "red";
            document.getElementById("manen").innerText = data["Operation"]["Man"] == "1" &&  data["Operation"]["Auto"] == "0" ? "Enabled" : "Disabled";

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

/*function imageExists(){
    image_url= "http://192.168.0.100:8080/stream?topic=/camera/rgb/image_raw"

    var http = new XMLHttpRequest();

    http.open("GET",image_url, false);
    http.send();

    if(http.status!=404){
        document.getElementById("sortrig").innerHTML = '<center><img src="http://192.168.0.100:8080/stream?topic=/camera/rgb/image_raw" style="height:570px;margin:10px"></center>'
    } else {
        document.getElementById("sortrig").innerHTML = '<center><img src="/static/home/src/liveview.jpg" style="height:570px;margin:10px"></center>'
    }

}*/