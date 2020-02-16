var pastversion="1";
var data
function updateData(){
    $.getJSON("/static/home/js/data.json",function(data){
        if (data["v"]!=pastversion){
            //TriTrack Data
            document.getElementById("PiStat").innerText = data["TriTrackDataMic"]["PiStat"];
            document.getElementById("Pi4procTri").innerText = data["TriTrackDataMic"]["Pi4procTri"];
            document.getElementById("BrdStat").innerText = data["TriTrackDataMic"]["BrdStat"];
            document.getElementById("BrdProc").innerText = data["TriTrackDataMic"]["BrdProc"];

            // PoweBoard
            document.getElementById("Consumption").innerText = data["TriTrackPowerBoard"]["Consumption"];
            document.getElementById("CapA").innerText = data["TriTrackPowerBoard"]["CapA"];
            document.getElementById("CapB").innerText = data["TriTrackPowerBoard"]["CapB"];
            
            //Rubbish
            document.getElementById("totRub").innerText = data["Rubbish"]["totRub"];
            document.getElementById("colRub").innerText = data["Rubbish"]["ColRub"];
            document.getElementById("BinA").innerText = data["Rubbish"]["BinA"]
            document.getElementById("BinB").innerText = data["Rubbish"]["BinB"];
            document.getElementById("BinC").innerText = data["Rubbsih"]["BinC"];
            
            pastversion=data["v"];

            delete data
        }
    })  
}
setInterval(updateData,2000);