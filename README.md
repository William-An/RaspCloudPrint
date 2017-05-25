# RaspCloudPrint
A simple python server run on Raspberry Pi 3 to handle print job submitted by web.

## Hardware
1. A Raspberry Pi 3
2. A 1602A LCD

## Procedure 
1. Users visit `printerip:8080/upload`
2. After receiving the file, the lcd will display the name of the file and current printjob amount.
3. Raspberry will save the file and use Linux printer command, `lp`, to print the file.
4. Server will automatically delete the uploaded file.

## How to run
1. Download this repository to your Raspberry Pi
2. Use `cloudprint/Scripts/python server.py` to run server, you can assign port by add the port number after this command.
3. Now you should see an output like this `http://127.0.0.1:portnum` which means the server is running