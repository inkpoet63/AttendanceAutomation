import pandas as pd
import os
from datetime import date

def getSchoolName(schoolCode):
    Musslemen = "MUHS"
    Washington = "WAHS"
    Jefferson = "JEHS"
    Martinsburg = "MAHS"
    Springmills = "SMHS"
    BerkeleySprings = "BSHS"
    PawPaw = "PPHS"

    if schoolCode == Musslemen:
        return "Musslemen"
    elif schoolCode == Washington:
        return "Washington"
    elif schoolCode == Jefferson:
        return "Jefferson"
    elif schoolCode == Martinsburg:
        return "Martinsburg"
    elif schoolCode == Springmills:
        return "Springmills"
    elif schoolCode == BerkeleySprings:
        return "Berkeley Springs"
    elif schoolCode == PawPaw:
        return "Paw Paw"
    else:
        return "Faculty"




daywanted = 20210823

data = pd.read_csv(r'data\AttendanceData.csv') # Reads file Mr.Ball sent me

today = date.today()

Absent = ['Absent']

currentdate = today.strftime("%Y%m%d")  # creates todays date

moredata = data.loc[(data['Date'] == daywanted) & data['Attendance'].isin(Absent)]      # Gets rows if columns have specific data

for index, row in moredata.iterrows():
    userId = row["Unique User ID"]
    firstName = row["First Name"]
    lastName = row["Last Name"]
    courseName = row["Course Name"]
    sectionName = row["Section Name"]
    attendance = row["Attendance"]
    schoolCode = userId[:4]
    schoolName = getSchoolName(schoolCode)
    if schoolName != "Faculty":
        print(f"{userId} : {schoolName} : {firstName} {lastName} : {courseName} : {sectionName} : {attendance}")
    #print(index,row["Unique User ID"],row["First Name"], row["Last Name"], row["Course Name"], row["Section Name"],  row["Attendance"])





