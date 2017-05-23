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
