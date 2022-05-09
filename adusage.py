# Python code to process the license usage CSV file from the
# Altium Concord Pro Vault
# Jamieson Olsen <jamieson@fnal.gov>

import csv
import sys

# This dictionary shows which users belong to which division
# names must be exact match to the names used on the vault accounts

# if the CSV file contains a name that does not exist in this dictionary
# the program will throw an exception

UserDivDB = {
"Chris Edwards":"DIR",

"Mark Zientarski":"ESH",

"Adam Olson":"ND",
"Linda Bagby":"ND",
"Javier Fernando Castano":"ND",
"Matt Micheli":"ND",
"Trevor Nichols":"ND",

"Andrew Feld":"AD",
"Alyssa Miller":"AD",
"Andrea Saewert":"AD",
"Alexei Semenov":"AD",
"Brian Vaughn":"AD",
"Aisha Ibrahim":"AD",
"Craig Drennan":"AD",
"Pete Dimovski":"AD",
"Rick Divelbiss":"AD",
"Ed Cullerton":"AD",
"Eric Claypool":"AD",
"Evan Milton":"AD",
"Brian Fellenz":"AD",
"Jim Galloway":"AD",
"Glenn Johnson":"AD",
"Michael Henry":"AD",
"Harsh Maniar":"AD",
"Jeremy Arnold":"AD",
"Jose Berlioz":"AD",
"John Dusatko":"AD",
"Josh Einstein-Curtis":"AD",
"Ken Koch":"AD",
"Dan Klepec":"AD",
"Matt Davidson":"AD",
"Mark Austin":"AD",
"Dan Mcarthur":"AD",
"James McTeague":"AD",
"Dan Munger":"AD",
"Nick Gurley":"AD",
"Joe Pastika":"AD",
"Dave Peterson":"AD",
"Rich Prokop":"AD",
"Brian Schupbach":"AD",
"Siddharth Poopathi":"AD",
"Ahmed Syed":"AD",
"Tom Boes":"AD",
"Trevor Butler":"AD",
"Ty Omark":"AD",
"Troy Petersen":"AD",
"John Van Bogaert":"AD",
"Yesenia Govea-Vargas":"AD",
"Joseph Flores":"AD",
"Steven Hays":"AD",
"Adam Koscielak":"AD",
"Susanna Eschbach":"AD",
"Jeff Simmons":"AD",
"Steve Rocos":"AD",

"Adam Anderson":"PPD",
"Albert Dyer":"PPD",
"Arnab Ghosh":"PPD",
"Brian Hess":"PPD",
"Steve Chappa":"PPD",
"Lou Dalmonte":"PPD",
"Gary Drake":"PPD",
"Farah Fahim":"PPD",
"Cristian Gingu":"PPD",
"Tyler Griffin":"PPD",
"Sten Hansen":"PPD",
"Scott Holm":"PPD",
"Dave Huffman":"PPD",
"Jamieson Olsen":"PPD",
"Johnny Green":"PPD",
"Jamieson Olsen":"PPD",
"Jamieson Olsen (Vault Admin)":"PPD",
"Juan Vega":"PPD",
"Jin-Yuan Wu":"PPD",
"Terry Kiper":"PPD",
"Kevin Kuk":"PPD",
"Sergey Los":"PPD",
"Lee Scott":"PPD",
"Maral Alyari":"PPD",
"Miguelangel Marchan":"PPD",
"Nina Moibenko":"PPD",
"Paul Rubinov":"PPD",
"Terri Shaw":"PPD",
"Mike Utes":"PPD",
"Vadim Rusu":"PPD",
"Vadim Rusu":"PPD",
"Walt Jaskerney":"PPD",
"Tom Deline":"PPD",
"Ashif Reza":"PPD",
"Waqar Ahmed":"PPD",

"Alan Prosser":"SCD",
"Andres Quintero Parra":"SCD",
"John Chramowicz":"SCD",
"Greg Deuerling":"SCD",
"Jason Greskoviak":"SCD",
"Rick Kwarciany":"SCD",
"Ryan Rivera":"SCD",
"Ken Treptow":"SCD",
"Neal WIlcer":"SCD",
"Ted Zmuda":"SCD",
"Divya Sirikonda":"SCD",

"Artur Galt":"APS-TD-TI",
"Adam Wixson":"APS-TD-TI",
"Cristian Arcola":"APS-TD-TI",
"Andrzej Makulski":"APS-TD-TI",
"Krzysztof Kompiel":"APS-TD-TI",
"Tom Cummings":"APS-TD-TI",
"Darryl Orris":"APS-TD-TI",
"Daniel Eddy":"APS-TD-TI",

"Alex Irigoyen":"APS-TD-SRF",
"Mohamed Hassan":"APS-TD-SRF",
"Paul Dubiel":"APS-TD-SRF",
"Roman Pilipenko":"APS-TD-SRF",

"Omar Al Atassi":"APS-TD-CRYO",

"Tom Thode":"APS-TD-MAG",

"Ugur Alyanak":"APS-TD-SRF",
"Warren Schappert":"APS-TD-SRF",
"Mike Quinlan":"APS-TD-SRF",

"Daniil Frolov":"NQI"
} 

UserHoursDB = {} # number of hours each user used a license
DivHoursDB = {}  # number of hours used by each division
TotalHours = 0

if ( len(sys.argv) != 2 ):
    print("usage: adusage.py input.csv")
    quit()

with open(sys.argv[1], 'r') as csv_file:
    reader = csv.reader(csv_file, delimiter=';')

    for row in reader:
        if "Designer" in row[0]: # only consider AD and AD-SE license usage, ignore vault usage
            t = row[5].split()
            user = row[2]
            divname = UserDivDB[user]

            if "min" in t[1]: # convert minutes to hours
                newtime = int(t[0])/60.0
            else: # newtime in hours
                newtime = int(t[0])
            
            TotalHours = TotalHours + newtime
            
            if user in UserHoursDB: # update
                UserHoursDB[user] = UserHoursDB[user] + newtime
            else: # insert
                UserHoursDB[user] = newtime

            if divname in DivHoursDB: # update
                DivHoursDB[divname] = DivHoursDB[divname] + newtime
            else: # insert
                DivHoursDB[divname] = newtime
   
    UHlist=sorted((value, key) for (key,value) in UserHoursDB.items())
    SortedUserHoursDB=dict([(k,v) for v,k in UHlist])

    print("\nTotal Altium Designer usage is %.1f license-hours" % TotalHours)

    for div,hours in DivHoursDB.items():
        print("\nDivision-Dept %s %.1f license-hours (%3.1f%%)" % (div,hours,(hours/TotalHours)*100))
        for user,hours in SortedUserHoursDB.items():
            if UserDivDB[user]==div:
                print("\t%.1f\t%s" % (hours, user))









