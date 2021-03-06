from django.shortcuts import render
from functions.data import datasharing
from django.http import HttpResponse
import json,os,random

from .forms import AutoManual

# Receiving data from the JSON File
def getInfo(data):
    datarecv=datasharing()

    if data=="Stat":
        datasend= datarecv.mic()
    elif data=="Power":
        datasend= datarecv.power()
    elif data=="rub":
        datasend= datarecv.rub()
    elif data=="sort":
        datasend= datarecv.sort()
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


# Testing the User Interface and the Main Index
def testUI(request):

    # === Read Data from the JSON file

    StatBoard=getInfo("Stat")
    autocords=getInfo("man")
    SortStat=getInfo("sort")
    Rubbish=getInfo("rub")

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
                # === EarthE Stats
                "PiStat": StatBoard["PiStat"],
                "Pi4procTri": StatBoard["Pi4procTri"],
                "BrdStat": StatBoard["BrdStat"],
                "BrdProc":StatBoard["BrdProc"],
                "RosStat": StatBoard["RosStat"],
                "ROSproc":StatBoard["ROSproc"],
                "aXaxis":autocords["xPos"],
                "aYaxis":autocords["yPos"],
                # === SortRig Stats
                "PiStatSort": SortStat["PiStat"],
                "Pi4procTriSor": SortStat["Pi4procTri"],
                "ArdStat": SortStat["ArdStat"],
                "ArdProc":SortStat["ArdProc"],
                "PrbStat": SortStat["PrbStat"],
                "PrbProc":SortStat["PrbProc"],
                # === Rubbish Stats
                "totRub": Rubbish["totRub"],
                "colRub": Rubbish["ColRub"],
                "SortRub": Rubbish["SortRub"],
                "BinA": Rubbish["BinA"],
                "BinB": Rubbish["BinB"],
                "BinC": Rubbish["BinC"],
            }
        )  
    elif man=="1":
        return render(
            request,
            'home/mrk2Manual.html',
            {
                # === EarthE Stats
                "PiStat": StatBoard["PiStat"],
                "Pi4procTri": StatBoard["Pi4procTri"],
                "BrdStat": StatBoard["BrdStat"],
                "BrdProc":StatBoard["BrdProc"],
                "RosStat": StatBoard["RosStat"],
                "ROSproc":StatBoard["ROSproc"],
                "aXaxis":autocords["xPos"],
                "aYaxis":autocords["yPos"],
                # === SortRig Stats
                "PiStatSort": SortStat["PiStat"],
                "Pi4procTriSor": SortStat["Pi4procTri"],
                "ArdStat": SortStat["ArdStat"],
                "ArdProc":SortStat["ArdProc"],
                "PrbStat": SortStat["PrbStat"],
                "PrbProc":SortStat["PrbProc"],
                # === Rubbish Stats
                "totRub": Rubbish["totRub"],
                "colRub": Rubbish["ColRub"],
                "SortRub": Rubbish["SortRub"],
                "BinA": Rubbish["BinA"],
                "BinB": Rubbish["BinB"],
                "BinC": Rubbish["BinC"],
            }
        )

# Webpage for User Interface Automatic Operation
def testUIauto(request):

    with open("UserInterface/static/home/js/data.json", "r+") as f:
        datafile = json.load(f)
        datafile["Operation"]["Auto"]="1"
        datafile["Operation"]["Man"]="0"
        datafile["v"]=str(float(datafile["v"]) + 0.1)
        f.close
    
    with open("UserInterface/static/home/js/data.json", "w+") as f:
        json.dump(datafile,f)
        f.close

    StatBoard=getInfo("Stat")
    autocords=getInfo("auto")
    SortStat=getInfo("sort")
    Rubbish=getInfo("rub")

    return render(
        request,
        'home/mrk2Auto.html',
        {
            # === EarthE Stats
            "PiStat": StatBoard["PiStat"],
            "Pi4procTri": StatBoard["Pi4procTri"],
            "BrdStat": StatBoard["BrdStat"],
            "BrdProc":StatBoard["BrdProc"],
            "RosStat": StatBoard["RosStat"],
            "ROSproc":StatBoard["ROSproc"],
            "aXaxis":autocords["xPos"],
            "aYaxis":autocords["yPos"],
            # === SortRig Stats
            "PiStatSort": SortStat["PiStat"],
            "Pi4procTriSor": SortStat["Pi4procTri"],
            "ArdStat": SortStat["ArdStat"],
            "ArdProc":SortStat["ArdProc"],
            "PrbStat": SortStat["PrbStat"],
            "PrbProc":SortStat["PrbProc"],
            # === Rubbish Stats
            "totRub": Rubbish["totRub"],
            "colRub": Rubbish["ColRub"],
            "SortRub": Rubbish["SortRub"],
            "BinA": Rubbish["BinA"],
            "BinB": Rubbish["BinB"],
            "BinC": Rubbish["BinC"],
            "BinD": Rubbish["BinD"],
            "BinAtfr": Rubbish["BinD"],
            "BinBtfr": Rubbish["BinD"],
            "BinCtfr": Rubbish["BinD"],
            "BinDtfr": Rubbish["BinD"],
        }
    )

# Webpage for User Interface Manual Operation
def testUIman(request):

    with open("UserInterface/static/home/js/data.json", "r+") as f:
        datafile = json.load(f)
        datafile["Operation"]["Auto"]="0"
        datafile["Operation"]["Man"]="1"
        datafile["v"]=str(float(datafile["v"])+0.1)
        f.close
    
    with open("UserInterface/static/home/js/data.json", "w+") as f:
        json.dump(datafile,f)
        f.close

    StatBoard=getInfo("Stat")
    autocords=getInfo("auto")
    SortStat=getInfo("sort")
    Rubbish=getInfo("rub")

    return render(
        request,
        'home/mrk2Manual.html',
        {
            # === EarthE Stats
            "PiStat": StatBoard["PiStat"],
            "Pi4procTri": StatBoard["Pi4procTri"],
            "BrdStat": StatBoard["BrdStat"],
            "BrdProc":StatBoard["BrdProc"],
            "RosStat": StatBoard["RosStat"],
            "ROSproc":StatBoard["ROSproc"],
            "aXaxis":autocords["xPos"],
            "aYaxis":autocords["yPos"],
            # === SortRig Stats
            "PiStatSort": SortStat["PiStat"],
            "Pi4procTriSor": SortStat["Pi4procTri"],
            "ArdStat": SortStat["ArdStat"],
            "ArdProc":SortStat["ArdProc"],
            "PrbStat": SortStat["PrbStat"],
            "PrbProc":SortStat["PrbProc"],
            # === Rubbish Stats
            "totRub": Rubbish["totRub"],
            "colRub": Rubbish["ColRub"],
            "SortRub": Rubbish["SortRub"],
            "BinA": Rubbish["BinA"],
            "BinB": Rubbish["BinB"],
            "BinC": Rubbish["BinC"],
        }
    )

# Webpage for User Interface Main Operation
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
                "Pi4procTri": StatBoard["Pi4procTri"],
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

# Webpage for User Interface Manual to Automatic Operation
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
                "Pi4procTri": StatBoard["Pi4procTri"],
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
# Webpage for User Interface Aitomatic to manual Operation
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
                "Pi4procTri": StatBoard["Pi4procTr  i"],
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

# Passing Data thorugh the URL
# These are the coordinates of Instructed and Current Coordinates
# ixaxis = Instracted X - Axis
# iyaxis = Current y - Axis
# cxaxis = Instracted X - Axis
# cyaxis = Current y - Axis
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

# Passing Data thorugh the URL
# These are the coordinates of the current position of earthe
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
# Webpage for User Interface Manual to Automatic Operation
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
# Webpage for User Interface Manual to Automatic Operation
def automation(request):
    with open("UserInterface/static/home/js/data.json", "r") as f:
        datafile = json.load(f)
        f.close

    if datafile["Operation"]["Man"]=="1":
        textResponse="True"
    else:
        textResponse="False"
    return HttpResponse(textResponse)

# Passing Data thorugh the URL
# These are the coordinates of the current position of earthe
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
