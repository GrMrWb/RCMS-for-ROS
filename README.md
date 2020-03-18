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

In order to run the User Interface on a specific IP and Port and connect to it remotely from another pc on the network you can run the following   

- Chrome: https://127.0.0.1:8000/
- Edge: https://localhost:8000/
- Firefox & Opera: https://127.0.0.1:8000/

Noteed that there are some difference between edge and chrome and edge which have not been corrected

## Data on UI
- TriTrack Mic
  - "PiStat": StatBoard["PiStat"],
  - "Pi4procTri": StatBoard["Pi4procTi"],
  - "BrdStat": StatBoard["BrdStat"],
  - "BrdProc":StatBoard["BrdProc"],
  > StatBoard is a dictionary which is called by <code>datasharing.mic()</code> which is located at <code>functions/data.py</code>
  
- TriTrack PowerBoard
  - "Consumption": PowerBoard["Consumption"],
  - "CapA": PowerBoard["CapA"], 
  - "CapB": PowerBoard["CapB"],
  > PowerBoard is a dictionary which is called by <code>datasharing.prb()</code> which is located at <code>functions/data.py</code>
  
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
  
## Things to be followed
- Sorting Rig interface

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
- pymongo   3.10.1
- pytz      2019.3
- requests  2.22.0
- sqlparse  0.3.0
- urllib3   1.25.8
