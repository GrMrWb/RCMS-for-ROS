from django.shortcuts import render
from functions.data import datasharing
from django.http import HttpResponse
import json,os,random

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
    elif data=="auto":
        datasend= datarecv.auto()
    elif data=="man":
        datasend= datarecv.auto()
    else:
        datasend={'No data'}

    return datasend

def testLayout(request):

    StatBoard=getInfo("Stat")
    autocords=getInfo("auto")

    return render(
        request,
        'home/mrk2Layout.html',
        {
            "PiStat": StatBoard["PiStat"],
            "Pi4procTri": StatBoard["Pi4procTi"],
            "BrdStat": StatBoard["BrdStat"],
            "BrdProc":StatBoard["BrdProc"],
            "aXaxis":autocords["xPos"],
            "aYaxis":autocords["yPos"]
        }
    )

def testUI(request):

    StatBoard=getInfo("Stat")
    autocords=getInfo("man")

    with open("UserInterface/static/home/js/data.json", "r") as f:
        datafile = json.load(f)
        auto=datafile["Operation"]["Auto"]
        man=datafile["Operation"]["Man"]
        f.close()

    if auto=="1":
        return render(
            request,
            'home/mrk2Auto.html',    
            {
                "PiStat": StatBoard["PiStat"],
                "Pi4procTri": StatBoard["Pi4procTi"],
                "BrdStat": StatBoard["BrdStat"],
                "BrdProc":StatBoard["BrdProc"],
                "aXaxis":autocords["xPos"],
                "aYaxis":autocords["yPos"]
            }
        )  
    elif man=="1":
        return render(
            request,
            'home/mrk2Manual.html',
            {
                "PiStat": StatBoard["PiStat"],
                "Pi4procTri": StatBoard["Pi4procTi"],
                "BrdStat": StatBoard["BrdStat"],
                "BrdProc":StatBoard["BrdProc"],
                "aXaxis":autocords["xPos"],
                "aYaxis":autocords["yPos"]
            }
        )

def testUIauto(request):
    
    StatBoard=getInfo("Stat")
    autocords=getInfo("auto")
    return render(
        request,
        'home/mrk2Auto.html',
        {
            "PiStat": StatBoard["PiStat"],
            "Pi4procTri": StatBoard["Pi4procTi"],
            "BrdStat": StatBoard["BrdStat"],
            "BrdProc":StatBoard["BrdProc"],
            "aXaxis":autocords["xPos"],
            "aYaxis":autocords["yPos"]
        }
    )

def testUIman(request):
    
    StatBoard=getInfo("Stat")
    autocords=getInfo("auto")
    return render(
        request,
        'home/mrk2Manual.html',
        {
            "PiStat": StatBoard["PiStat"],
            "Pi4procTri": StatBoard["Pi4procTi"],
            "BrdStat": StatBoard["BrdStat"],
            "BrdProc":StatBoard["BrdProc"],
            "aXaxis":autocords["xPos"],
            "aYaxis":autocords["yPos"]
        }
    )

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

def cordOnJSON(request,ixaxis,iyaxis,cxaxis,cyaxis):
    with open("UserInterface/static/home/js/manualoperation.json", "r") as f:
        try:
            datafile = json.load(f)  
        except:
            f.close
            with open("UserInterface/static/home/js/manualoperation.json", "a+") as f:
                f.seek(0,2)
                f.truncate()
                f.seek(0, 0)
                f.close
            with open("UserInterface/static/home/js/manualoperation.json", "r") as f:
                datafile =json.load(f)    

        datafile["Manual"]["ix-axis"]=ixaxis
        datafile["Manual"]["iy-axis"]=iyaxis
        datafile["Manual"]["cx-axis"]=cxaxis
        datafile["Manual"]["cy-axis"]=cyaxis
        version=random.randint(1,101)
        datafile["v"]=str(version)
        f.close
    
    with open("UserInterface/static/home/js/manualoperation.json", "w+") as f:
        json.dump(datafile,f)
        f.close

    return HttpResponse('<p>Thanks Earth-E</p>')

def infoOnJSON(request,processedData):
    data=processedData.split(":")
    with open("UserInterface/static/home/js/data.json", "r") as f:
        try:
            datafile = json.load(f)  
        except:
            f.close
            with open("UserInterface/static/home/js/data.json", "a+") as f:
                f.seek(0,2)
                f.truncate()
                f.seek(0, 0)
                f.close
            with open("UserInterface/static/home/js/data.json", "r") as f:
                datafile =json.load(f)    

        datafile["TriTrackDataMic"]["PiStat"]=data[0]
        datafile["TriTrackDataMic"]["Pi4procTri"]=data[1]
        datafile["TriTrackDataMic"]["BrdStat"]=data[2]
        datafile["TriTrackDataMic"]["BrdProc"]=data[3]
        version=random.randint(1,101)
        datafile["v"]=str(version)
        f.close
    
    with open("UserInterface/static/home/js/data.json", "w+") as f:
        json.dump(datafile,f)
        f.close

    return HttpResponse('<p>Thanks Earth-E</p>')

def warning(request,seagull,tide):
    with open("UserInterface/static/home/js/warning.json", "r") as f:
        datafile = json.load(f)
        datafile["Warning"]["seagull"]=seagull
        datafile["Warning"]["tide"]=tide
        f.close
    
    with open("UserInterface/static/home/js/warning.json", "w+") as f:
        json.dump(datafile,f)
        f.close

    return HttpResponse('<p>Thanks Earth-E</p>')

def automation(request):
    with open("UserInterface/static/home/js/data.json", "r") as f:
        datafile = json.load(f)
        f.close

    if datafile["Operation"]["Man"]=="1":
        textResponse="True"
    else:
        textResponse="False"
    return HttpResponse(textResponse)

def cordsFromRos(request,currentPosition):
    newStr=currentPosition.split(":")
    
    with open("UserInterface/static/home/js/manualoperation.json", "r") as f:
        try:
            datafile = json.load(f)  
        except:
            f.close
            with open("UserInterface/static/home/js/manualoperation.json", "a+") as f:
                f.seek(0,2)
                f.truncate()
                f.seek(0, 0)
                f.close
            with open("UserInterface/static/home/js/manualoperation.json", "r") as f:
                datafile =json.load(f)    

        datafile["Manual"]["cx-axis"]=newStr[0]
        datafile["Manual"]["cy-axis"]=newStr[1]
        version=random.randint(1,101)
        datafile["v"]=str(version)
        f.close
    
    with open("UserInterface/static/home/js/manualoperation.json", "w+") as f:
        json.dump(datafile,f)
        f.close

    return HttpResponse('<p>Thanks Earth-E</p>')