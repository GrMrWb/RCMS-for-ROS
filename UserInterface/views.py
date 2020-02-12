from django.shortcuts import render

# Create your views here.

def home(request):
    StatBoard=1
    if StatBoard==1:
        BrdStat="Operational"
    elif StatBoard==2:
        BrdStat="Low Capacity"
    elif StatBoard==3:
        BrdStat="INOP"

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
                "BrdStat":"Operational",
                "BrdProc":30,
            # ===TriTrack PowerBoard
                "Consumption": 1243,
                "CapA":"threequarter",
                "CapB":"half",
        }
    )