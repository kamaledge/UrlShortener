1. Copy the entire repository to any file location in server with FTP Software.
   eg. server1/home/URLShortener/

2. Install all the python library dependencies.

   make install


3. To start the connector run the below command:

abc> make start

4. Check the status of the connector by running the below command

abc> make status

5. To stop the connector run the below command:

abc> make stop


6. Installation steps on windows:

On windows the UrlShortener is supported only in DEVELOPMENT Mode.

Below are the alternatives for steps 2, 3 and 5 mentioned above to run the service.

    2-ALT: pip install -r requirements.txt
    7-ALT: python app.py (This starts the service on port 5000)
    9-ALT: Ctrl + C to stop the process. 