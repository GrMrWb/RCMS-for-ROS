from django.shortcuts import render
from functions.data import datasharing

# Create your views here.

def home(request):
    datarecv=datasharing()

    StatBoard=datarecv.mic()
    

    PiBoard=3
    if PiBoard==1:
        PiStat="Operational"
    elif PiBoard==2:
        PiStat="Low Capacity"
    elif PiBoard==3:
        PiStat="INOP"

    return  render(
        request,
        'home/home.html',
        {
            # ===TriTrack Mic
                "PiStat": PiStat,
                "Pi4procTri": 12,
                "BrdStat": StatBoard["BrdStat"],
                "BrdProc":30,
            # ===TriTrack PowerBoard
                "Consumption": 1243,
                "CapA":"threequarter",
                "CapB":"half",
        }
    )