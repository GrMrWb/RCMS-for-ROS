from django.shortcuts import render
from functions.data import datasharing

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