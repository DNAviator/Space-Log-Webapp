# Space Log Webapp

## Description
 A basic webpage that can be used to record Captain's logs and view previously created logs

## Functionality
 Uses Django with sqlite to store text with a creation date. In the html you are able to input your text log and by clicking the submit button add your log to the database. All the previously created logs will be visible in a scrollable sidebar sorted by the date they were created.

 ## How to use
 In order to use this webapp follow these instructions:
 1. Clone the repository
 2. Verify you have python installed \\
    Python can be downloaded at https://www.python.org/downloads/ (The code is run on 3.12.2 but should run on any python 3)
 3. Verify your python has django installed as a package (I personally use a venv) \\
    To install django in your console run: pip install django
 4. After you have your environment setup navigate in the consol to the CrudApp directory with cd .\CrudApp\ (assuming you are already in the project directory)
 5. Once in the directory run the code: python manage.py runserver (optionally port number can be added here)
 6. The terminal should provide a link to the running webserver or it should be able to be found at localhost:8000 (or the specified port)

 ## How to modify database entries
 As a captains log the primary functionality is for storage but if you want to modify or delete entries follow these steps:
 1. Make sure the webserver is not running
 2. In the CrudApp directory run python manage.py createsuperuser and follow the instructions provided in the terminal
 3. Run the server and navigate to /admin (potential full url of localhost:8000/admin)
 4. Enter the admin credentials and click the change button for Captain's Logs