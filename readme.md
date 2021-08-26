# Altium Usage

Python code to process the license usage CSV file from the Altium Concord Pro Vault. Does not require mucking about with databases and all that.

## Generating the CSV file

1. Using an admin account, sign into the Altium Concord Pro vault via the web interface.
2. Admin > Licenses > Reports tab > Usage History tab
3. Specify time interval, ok to use "custom"
4. Group by YEAR
5. Click Apply, save CSV

The lines in the CSV file should look like this:

> Altium Designer;3RS5-YAW2;Jamieson Olsen;All Users;2021;146 hours;11 hours;2

## Running this program

$ python adusage.py myfile.csv

## Example output

The program output will list license file usage by division and user (hours).

	Division SCD 5182.6 hours (12.2%)
			6.5     John Chramowicz
			13.0    Divya Sirikonda
			160.0   Ken Treptow
			978.0   Andres Quintero Parra
			1133.0  Waqar Ahmed
			1375.0  Greg Deuerling
			1517.0  Neal WIlcer
