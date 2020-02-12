## Run the Server

- Make sure you have the install Python 3.8.1
- Make sure you have active the virtual environment
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
   - "Pi4procTri": 12,
   - "BrdStat":"Operational",
   - "BrdProc":30,
- TriTrack PowerBoard
   - "Consumption": 1243,
   - "CapA":"threequarter",
   - "CapB":"half",

- Rubbish
   - "totRub": dataRub["totRub"],
   - "colRub": dataRub["colRub"],
   - "BinG": dataRub["BinG"],
   - "BinA": dataRub["BinA"],
   - "BinB": dataRub["BinB"],
   - "BinC": dataRub["BinC"],
