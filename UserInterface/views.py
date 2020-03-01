from django.shortcuts import render
from functions.data import datasharing

# Create your views here.

def home(request):
    datarecv=datasharing()

    StatBoard=datarecv.mic()
    PowerBoard=datarecv.power()
    Rubbish=datarecv.rub()
    Operation=datarecv.ops()
    warning=datarecv.warn()

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
