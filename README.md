## Run the Server

- Active the virtual environment
  <code>./env/scripts/activate</code>
  > BE AWARE EXECUTION POLICY MUST BE UNRESTRICTED
    - Open the PowerShell as an Administator and run the following command <code>Set-ExecutionPolciy Unrestricted</code>
    - Press Y after you have activated the env go back and set the Policy again restricted
 - To ensure everything is in place you must run the collect  static 
  <code>python manage.py collectedstatic</code>
 - Now you are ready to run the server
  <code>python manage.py runserver</code>

## To view the User Interface

- Chrome: https://127.0.0.1:8000/
- Edge: https://localhost:8000/
- Firefox & Opera: Not Tested

Noteed that there are some difference between edge and chrome and edge which have not been corrected

## Data oon UI
- TriTrack Microprocessors
   - "PiStat": PiStat
   - "Pi4procTri": 12
   - "BrdStat":"Operational"
   - "BrdProc":30
- TriTrack PowerBoard
   - "Consumption": 1243
   - "CapA":"threequarter"
   - "CapB":"half"
- Rubbish
   - "totRub": dataRub["totRub"]
   - "colRub": dataRub["colRub"]
   - "BinG": dataRub["BinG"]
   - "BinA": dataRub["BinA"]
   - "BinB": dataRub["BinB"]
   - "BinC": dataRub["BinC"]

## Systems Requirements
- Python    3.8.1 (32-bit)
- Django    3.0.2
- pip       20.0.2
- asgiref   3.2.3
- certifi   2019.11.28
- chardet   3.0.4
- idna      2.8
- pymongo   3.10.1
- pytz      2019.3
- requests  2.22.0
- sqlparse  0.3.0
- urllib3   1.25.8
