# User Interface

[![User Interface](https://img.youtube.com/vi/Veu4dWLZzMg/0.jpg)](https://youtu.be/Veu4dWLZzMg)

- Currently capable to acquire data from ROS and illustrate it every 0.5s
- Send data to ROS if the User wants to control the Earth-E manual
- Can stream live video from the Earth-E, Eye-in-the-Sky and Sorting Rig
- Control Sorting Rig and the user is able to see what type of rubbish is the one that the Sorting Rig picks
- Amount of Rubbish inside each Bins
- Perforfmance Indices for each sub-System

## Run the Server

- Make sure you have Pytho 3.8 installed on the 
- Active the virtual environment (for windows only)
  <code>./env/scripts/activate</code>
  > BE AWARE EXECUTION POLICY MUST BE UNRESTRICTED
    - Open the PowerShell as an Administator and run the following command <code>Set-ExecutionPolciy Unrestricted</code>
    - Press Y after you have activated the env go back and set the Policy again restricted
    - This is only for running the server on localhost
- To ensure everything is in place you must run the collect  static 
<code>python manage.py collectedstatic</code>
- Now you are ready to run the server
<code>python manage.py runserver</code>

## To view the User Interface

- Chrome: https://127.0.0.1:8000/
- Edge: https://localhost:8000/
- Firefox & Opera: https://127.0.0.1:8000/

In order to run the User Interface on a specific _IP_ and _Port_ and connect to it remotely from another pc on the network you can run the following:

<code>python manage.py runserver _IP_:_PORT_</code>

Noteed that there are some difference between edge and chrome and edge which have not been corrected

## Data on UI

- TriTrack Mic
  - "PiStat": StatBoard["PiStat"],
  - "Pi4procTri": StatBoard["Pi4procTi"],
  - "BrdStat": StatBoard["BrdStat"],
  - "BrdProc":StatBoard["BrdProc"],
  - "RosStat": StatBoard["RosStat"],
  - "ROSproc":StatBoard["ROSproc"],
  - "aXaxis":autocords["xPos"],
  - "aYaxis":autocords["yPos"],
  > StatBoard is a dictionary which is called by <code>datasharing.mic()</code> which is located at <code>functions/data.py</code>
  
- TriTrack PowerBoard
  - "Consumption": PowerBoard["Consumption"],
  - "CapA": PowerBoard["CapA"], 
  - "CapB": PowerBoard["CapB"],
  > PowerBoard is a dictionary which is called by <code>datasharing.prb()</code> which is located at <code>functions/data.py</code>
  
- Sorting Data
  - "PiStatSort": SortStat["PiStat"],
  - "Pi4procTriSor": SortStat["Pi4procTri"],
  - "ArdStat": SortStat["ArdStat"],
  - "ArdProc":SortStat["ArdProc"],
  - "PrbStat": SortStat["PrbStat"],
  - "PrbProc":SortStat["PrbProc"],
  > Sorting Data is a dictionary which is called by <code>datasharing.prb()</code> which is located at <code>functions/data.py</code>
  
- Rubbish Estimation
  - "totRub": Rubbish["totRub"],
  - "colRub": Rubbish["ColRub"],
  - "BinA": Rubbish["BinA"],
  - "BinB": Rubbish["BinB"],
  - "BinC": Rubbish["BinC"],
  > Rubbish is a dictionary which is called by <code>datasharing.rub()</code> which is located at <code>functions/data.py</code>
  
- Operation
  - "autoen" : Operation ["Auto"]
  - "manen" : Operation ["Manual"]
  > report to the ROS that the user is using either the Automatic or Manual Operation

- Warnings
  - "seagull" : warning["seagull"]
  - "tide" : warning["tide"]

## Requirements.txt
- Python    3.8.1 (32-bit)
- Django    3.0.3
- pip       20.0.2
- asgiref   3.2.3
- astroid   2.3.3
- certifi   2019.11.28
- chardet   3.0.4
- colorama  0.4.3
- idna      2.8
- pytz      2019.3
- requests  2.22.0
- sqlparse  0.3.0
- urllib3   1.25.8
