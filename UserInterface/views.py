from django.shortcuts import render
from functions.data import datasharing
import json

from .forms import AutoManual

def getInfo(data):
    datarecv=datasharing()

    if data=="Stat":
        datasend= datarecv.mic()
    elif data=="Power":
        datasend= datarecv.power()
    elif data=="rub":
        datasend= datarecv.rub()
    elif data=="ops":
        datasend= datarecv.ops()
    elif data=="warn":
        datasend= datarecv.warn()

    return datasend

def home(request):
    StatBoard=getInfo("Stat")
    PowerBoard=getInfo("Power")
    Rubbish=getInfo("rub")
    Operation=getInfo("ops")
    warning=getInfo("warn")

    return  render(
        request,
        'home/home.html',
        {
            # ===TriTrack Mic
                "PiStat": StatBoard["PiStat"],
                "Pi4procTri": StatBoard["Pi4procTi"],
                "BrdStat": StatBoard["BrdStat"],
                "BrdProc":StatBoard["BrdProc"],
            # ===TriTrack PowerBoard
                "Consumption": PowerBoard["Consumption"],
                "CapA": PowerBoard["CapA"],
                "CapB": PowerBoard["CapB"],
            # ===Rubbish Estimation
                "totRub": Rubbish["totRub"],
                "colRub": Rubbish["ColRub"],
                "SortRub": Rubbish["SortRub"],
                "BinA": Rubbish["BinA"],
                "BinB": Rubbish["BinB"],
                "BinC": Rubbish["BinC"],
            # ===Operation
                "autoen" : Operation["Auto"],
                "manen" : Operation["Man"],
            # ===Warning
                "seagull" :warning["seagull"]
        }
    )

def mantoauto(request):

    StatBoard=getInfo("Stat")
    PowerBoard=getInfo("Power")
    Rubbish=getInfo("rub")
    Operation=getInfo("ops")
    warning=getInfo("warn")

    with open("UserInterface/static/home/js/data.json", "r+") as f:
        datafile = json.load(f)
        datafile["Operation"]["Auto"]="1"
        datafile["Operation"]["Man"]="0"
        datafile["v"]=str(float(datafile["v"]) + 0.1)
        f.close
    
    with open("UserInterface/static/home/js/data.json", "w+") as f:
        json.dump(datafile,f)
        f.close

    return  render(
        request,
        'home/home.html',
        {
            # ===TriTrack Mic
                "PiStat": StatBoard["PiStat"],
                "Pi4procTri": StatBoard["Pi4procTi"],
                "BrdStat": StatBoard["BrdStat"],
                "BrdProc":StatBoard["BrdProc"],
            # ===TriTrack PowerBoard
                "Consumption": PowerBoard["Consumption"],
                "CapA": PowerBoard["CapA"],
                "CapB": PowerBoard["CapB"],
            # ===Rubbish Estimation
                "totRub": Rubbish["totRub"],
                "colRub": Rubbish["ColRub"],
                "SortRub": Rubbish["SortRub"],
                "BinA": Rubbish["BinA"],
                "BinB": Rubbish["BinB"],
                "BinC": Rubbish["BinC"],
            # ===Operation
                "autoen" : Operation["Auto"],
                "manen" : Operation["Man"],
            # ===Warning
                "seagull" :warning["seagull"]
        }
    )

def autotoman(request):
        
    StatBoard=getInfo("Stat")
    PowerBoard=getInfo("Power")
    Rubbish=getInfo("rub")
    Operation=getInfo("ops")
    warning=getInfo("warn")
    
    with open("UserInterface/static/home/js/data.json", "r+") as f:
        datafile = json.load(f)
        datafile["Operation"]["Auto"]="0"
        datafile["Operation"]["Man"]="1"
        datafile["v"]=str(float(datafile["v"])+0.1)
        f.close
    
    with open("UserInterface/static/home/js/data.json", "w+") as f:
        json.dump(datafile,f)
        f.close

    return  render(
        request,
        'home/home.html',
        {
            # ===TriTrack Mic
                "PiStat": StatBoard["PiStat"],
                "Pi4procTri": StatBoard["Pi4procTi"],
                "BrdStat": StatBoard["BrdStat"],
                "BrdProc":StatBoard["BrdProc"],
            # ===TriTrack PowerBoard
                "Consumption": PowerBoard["Consumption"],
                "CapA": PowerBoard["CapA"],
                "CapB": PowerBoard["CapB"],
            # ===Rubbish Estimation
                "totRub": Rubbish["totRub"],
                "colRub": Rubbish["ColRub"],
                "SortRub": Rubbish["SortRub"],
                "BinA": Rubbish["BinA"],
                "BinB": Rubbish["BinB"],
                "BinC": Rubbish["BinC"],
            # ===Operation
                "autoen" : Operation["Auto"],
                "manen" : Operation["Man"],
            # ===Warning
                "seagull" :warning["seagull"]
        }
    )