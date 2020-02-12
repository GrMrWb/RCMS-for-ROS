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

## To view the UserInterface

- Chrome: https://127.0.0.1:8000/
- Edge: https://localhost:8000/
- Firefox & Opera: Not Tested

Noteed that there are some difference between edge and chrome and edge which have not been corrected
