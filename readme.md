# Altium Usage

Python code to process the license usage CSV file from the Altium Concord Pro Vault. Does not require mucking about with databases and all that.

## Generating the CSV file

1. Using an admin account, sign into the Altium Concord Pro vault via the web interface.
2. Admin > Licenses > Reports tab > Usage History tab
3. Specify time interval, ok to use "custom"
4. Group by YEAR
5. Click Apply, save CSV

The lines in the CSV file should look like this:

	Altium Designer;3RS5-YAW2;Jamieson Olsen;All Users;2021;146 hours;11 hours;2

## Running this program

$ python adusage.py myfile.csv

## Example output

The program output will list license file usage by division and user (hours).

	Total Altium Designer usage is 42519.5 license-hours

	Division STD 6792.3 license-hours (16.0%)
        5.8     Adam Wixson
        7.0     Paul Dubiel
        13.0    Alex Irigoyen
        44.0    Ugur Alyanak
        220.1   Roman Pilipenko
        435.9   Krzysztof Kompiel
        596.0   Andrzej Makulski
        1006.5  Cristian Arcola
        1999.0  Tom Cummings
        2465.0  Artur Galt

	Division SCD 5182.6 license-hours (12.2%)
        6.5     John Chramowicz
        13.0    Divya Sirikonda
        160.0   Ken Treptow
        978.0   Andres Quintero Parra
        1133.0  Waqar Ahmed
        1375.0  Greg Deuerling
        1517.0  Neal WIlcer

## User-Division list

User names are assigned to Fermilab divisions in a dictionary contained in this python code. Yeah, it's kind of cheesy but it works for now. If the CSV file contains a user name that is not present in this dictionary, the program will throw an exeption and will stop processing the CSV file. Then you'll need to manually add that user name to the dictionary and try again.

