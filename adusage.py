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
"Chris Edwards":"INFERASTRUCTURE SERVICES",

"Mark Zientarski":"ESH",
"Adam Olson":"ESH",
"Tom Houlahan":"ESH",
"Jeff Putney":"ESH",

"Andrew Feld":"ACCELERATORS",
"Alyssa Miller":"ACCELERATORS",
"Andrea Saewert":"ACCELERATORS",
"Alexei Semenov":"ACCELERATORS",
"Brian Vaughn":"ACCELERATORS",
"Aisha Ibrahim":"ACCELERATORS",
"Craig Drennan":"ACCELERATORS",
"Pete Dimovski":"ACCELERATORS",
"Rick Divelbiss":"ACCELERATORS",
"Ed Cullerton":"ACCELERATORS",
"Eric Claypool":"ACCELERATORS",
"Evan Milton":"ACCELERATORS",
"Brian Fellenz":"ACCELERATORS",
"Jim Galloway":"ACCELERATORS",
"Glenn Johnson":"ACCELERATORS",
"Michael Henry":"ACCELERATORS",
"Harsh Maniar":"ACCELERATORS",
"Jeremy Arnold":"ACCELERATORS",
"Jose Berlioz":"ACCELERATORS",
"John Dusatko":"ACCELERATORS",
"Josh Einstein-Curtis":"ACCELERATORS",
"Ken Koch":"ACCELERATORS",
"Dan Klepec":"ACCELERATORS",
"Matt Davidson":"ACCELERATORS",
"Mark Austin":"ACCELERATORS",
"Dan Mcarthur":"ACCELERATORS",
"James McTeague":"ACCELERATORS",
"Dan Munger":"ACCELERATORS",
"Nick Gurley":"ACCELERATORS",
"Joe Pastika":"ACCELERATORS",
"Dave Peterson":"ACCELERATORS",
"Rich Prokop":"ACCELERATORS",
"Brian Schupbach":"ACCELERATORS",
"Siddharth Poopathi":"ACCELERATORS",
"Ahmed Syed":"ACCELERATORS",
"Tom Boes":"ACCELERATORS",
"Trevor Butler":"ACCELERATORS",
"Ty Omark":"ACCELERATORS",
"Troy Petersen":"ACCELERATORS",
"John Van Bogaert":"ACCELERATORS",
"Yesenia Govea-Vargas":"ACCELERATORS",
"Joseph Flores":"ACCELERATORS",
"Steven Hays":"ACCELERATORS",
"Adam Koscielak":"ACCELERATORS",
"Susanna Eschbach":"ACCELERATORS",
"Jeff Simmons":"ACCELERATORS",
"Steve Rocos":"ACCELERATORS",
"Yuriy Koval":"ACCELERATORS",
"Finley Novak":"ACCELERATORS",
"Matt Kufer":"ACCELERATORS",
"Brad Claypool":"ACCELERATORS",
"Mallory Sutter":"ACCELERATORS",
"Chris Izzo":"ACCELERATORS",
"Dustin Pieper":"ACCELERATORS",
"Matthew Domeier":"ACCELERATORS",
"Matt Saewert":"ACCELERATORS",
"Alexander Quilty":"ACCELERATORS",
"Gilberto Perez":"ACCELERATORS",
"Andrew Whitbeck":"ACCELERATORS",
"Sabri Shawar":"ACCELERATORS",
"David Capetillo":"ACCELERATORS",
"Jonathan Eisch":"ACCELERATORS",
"Mike Coleman":"ACCELERATORS",
"Shengli Liu":"ACCELERATORS",
"Spencer Garcia-Schiefelbein":"ACCELERATORS",
"Chris Olsen":"ACCELERATORS",


"Adam Anderson":"PARTICLE PHYSICS",
"Albert Dyer":"PARTICLE PHYSICS",
"Arnab Ghosh":"PARTICLE PHYSICS",
"Brian Hess":"PARTICLE PHYSICS",
"Steve Chappa":"PARTICLE PHYSICS",
"Lou Dalmonte":"PARTICLE PHYSICS",
"Gary Drake":"PARTICLE PHYSICS",
"Farah Fahim":"PARTICLE PHYSICS",
"Cristian Gingu":"PARTICLE PHYSICS",
"Tyler Griffin":"PARTICLE PHYSICS",
"Sten Hansen":"PARTICLE PHYSICS",
"Scott Holm":"PARTICLE PHYSICS",
"Dave Huffman":"PARTICLE PHYSICS",
"Jamieson Olsen":"PARTICLE PHYSICS",
"Johnny Green":"PARTICLE PHYSICS",
"Jamieson Olsen":"PARTICLE PHYSICS",
"Jamieson Olsen (Vault Admin)":"PARTICLE PHYSICS",
"Juan Vega":"PARTICLE PHYSICS",
"Jin-Yuan Wu":"PARTICLE PHYSICS",
"Terry Kiper":"PARTICLE PHYSICS",
"Kevin Kuk":"PARTICLE PHYSICS",
"Sergey Los":"PARTICLE PHYSICS",
"Lee Scott":"PARTICLE PHYSICS",
"Maral Alyari":"PARTICLE PHYSICS",
"Miguelangel Marchan":"PARTICLE PHYSICS",
"Nina Moibenko":"PARTICLE PHYSICS",
"Paul Rubinov":"PARTICLE PHYSICS",
"Terri Shaw":"PARTICLE PHYSICS",
"Mike Utes":"PARTICLE PHYSICS",
"Vadim Rusu":"PARTICLE PHYSICS",
"Vadim Rusu":"PARTICLE PHYSICS",
"Walt Jaskerney":"PARTICLE PHYSICS",
"Tom Deline":"PARTICLE PHYSICS",
"Ashif Reza":"PARTICLE PHYSICS",
"Waqar Ahmed":"PARTICLE PHYSICS",
"Jacques Ntahoturi":"PARTICLE PHYSICS",
"Yash Saxena":"PARTICLE PHYSICS",
"Manuel Arroyave":"PARTICLE PHYSICS",

# Neutrino Division folks now under PPD 

"Linda Bagby":"PARTICLE PHYSICS",
"Javier Fernando Castano":"PARTICLE PHYSICS",
"Matt Micheli":"PARTICLE PHYSICS",
"Trevor Nichols":"PARTICLE PHYSICS",

"Alan Prosser":"COMPUTATIONAL SCIENCE",
"Andres Quintero Parra":"COMPUTATIONAL SCIENCE",
"John Chramowicz":"COMPUTATIONAL SCIENCE",
"Greg Deuerling":"COMPUTATIONAL SCIENCE",
"Jason Greskoviak":"COMPUTATIONAL SCIENCE",
"Rick Kwarciany":"COMPUTATIONAL SCIENCE",
"Ryan Rivera":"COMPUTATIONAL SCIENCE",
"Ken Treptow":"COMPUTATIONAL SCIENCE",
"Neal Wilcer":"COMPUTATIONAL SCIENCE",
"Ted Zmuda":"COMPUTATIONAL SCIENCE",
"Divya Sirikonda":"COMPUTATIONAL SCIENCE",
"Joe Kaminski":"COMPUTATIONAL SCIENCE",

# Combining various APSTD departments now under single directorate

"Artur Galt":"APSTD",
"Adam Wixson":"APSTD",
"Cristian Arcola":"APSTD",
"Andrzej Makulski":"APSTD",
"Krzysztof Kompiel":"APSTD",
"Tom Cummings":"APSTD",
"Darryl Orris":"APSTD",
"Daniel Eddy":"APSTD",
"Alex Irigoyen":"APSTD",
"Mohamed Hassan":"APSTD",
"Paul Dubiel":"APSTD",
"Roman Pilipenko":"APSTD",
"Omar Al Atassi":"APSTD",
"Tom Thode":"APSTD",
"Ugur Alyanak":"APSTD",
"Warren Schappert":"APSTD",
"Mike Quinlan":"APSTD",
"Alexander Hogberg":"APSTD",

"Sanskriti Joshi":"VISITOR",
"Parker Adamski":"VISITOR",
"Elena Pedreschi":"VISITOR",
"Elena Pedreschi":"VISITOR",

"David Van Zanten":"EMERGING TECHNOLOGIES",
"Yulia Krasnikova":"EMERGING TECHNOLOGIES",
"Geev Nahal":"EMERGING TECHNOLOGIES",
"Daniil Frolov":"EMERGING TECHNOLOGIES",
"Silvia Zorzetti":"EMERGING TECHNOLOGIES"
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
        print("\nDirectorate %s %.1f license-hours (%3.1f%%)" % (div,hours,(hours/TotalHours)*100))
        for user,hours in SortedUserHoursDB.items():
            if UserDivDB[user]==div:
                print("\t%8.1f\t%s" % (hours, user))









