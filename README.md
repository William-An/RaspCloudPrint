# About Raspberry Pi Cloud Printer
Raspberry Pi Cloud Printer is a cloud print platform based on [web.py](http://webpy.org) which runs on [Raspberry Pi](https://www.raspberrypi.org/), a tiny linux computer(based on [CloudPrint](https://github.com/William-An/CloudPrint)). In addition, any device can submit print job to RPCP. 

# Hardware
* A Raspberry Pi 3
* A printer
* A network wire or network card
* Power supply for Pi and printer

# Prerequisites
* Installed CUPS 
* Installed driver for printer
* Installed python3
* Configured network card
* Downloaded this [git repository](https://github.com/William-An/RaspCloudPrint)

## Procedure 
1. Users visit `printerip:8080/upload`
2. After receiving the file, the lcd will display the name of the file and current printjob amount.
3. Raspberry will save the file and use Linux printer command, `lp`, to print the file.
4. Server will automatically delete the uploaded file.
	
		apt-get install cups
		apt-get install hplip (For HP printer)
		git clone https://github.com/William-An/RaspCloudPrint.git
		OR
		wget https://github.com/William-An/RaspCloudPrint/archive/master.zip
		// For HP: some HP printers demand HP-Plugin, you can download from http://hplip.sourceforge.net/plugin.conf
		// For adding printers: you need to modify /etc/cups/cupsd.conf so that you can access the control menu through http


# How to run
    cd <git repo dir> && sudo python3 server.py 80

# Procedure
1. User will visit `printerip/upload` to print file
2. Server will save the file it gets and use `lp` to print this file
3. The file will be delete and user will be redirected to index
4. If error happens, user will be redirected to error page and can access `printerip/log` for view or download print log

# Future
1. Add support for more format; currently(v1.0), RPCP only support pdf
2. Add more options when printing; allow users to configure their printing; currently(v1.0), RPCP can only print by default
3. Add an 1602A LCD screen to show current print job attributes
1. Dokku/Docker installation
1. IOT!
1. CUPS native support (directly connect to printer)

# Error
If there are bugs, please post them on [issues section](https://github.com/William-An/RaspCloudPrint/issues) or contact through my email: [China_Aisa@live.com](mailto:China_Aisa@live.com)

# Acknowledge
[Flaticon](http://www.flaticon.com) -> Tab icon
[web.py](http://webpy.org) -> Server framework 
[html5up](https://html5up.net/) -> HTML Template

# Contact
E-Mail: [China_Aisa@live.com](mailto:China_Aisa@live.com)
Github: [William-An](https://github.com/William-An)
TheXYZLab: [Official Site](http://william-an.xyz) | [Github Organization](https://github.com/TheXYZLAB)

2017/05/30 v1.0


