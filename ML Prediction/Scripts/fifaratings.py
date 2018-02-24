import requests
import sys
import re
import csv


def fifaratings() :

    yearparam=['06_2', '07_3', '08_4', '09_5', '10_6', '11_7', '12_9','13_10', '14_13', '15_14', '16_73', '17_173']

    #yearparam are parameters used by the website below
    url = 'https://www.fifaindex.com/teams/FIRST?league=13'
    #Credits to FifaIndex for providing FIFA ratings of EPL teams from 2005-present
    myFile = open('fifaratings.csv', 'wb')
    year = 2005
    with myFile:
        writer = csv.writer(myFile)
        firstrow = ['Team','Season','ATT', 'MID', 'DEF', 'OVR']
        writer.writerow(firstrow)
        for i in range(len(yearparam)):
            new_url = url.replace('FIRST', 'fifa'+ yearparam[i] + '/')
            req = requests.get(new_url)
            raw = req.content
            reg = r'alt="([\s\w]+)"'
            clubNames = re.findall(reg, str(raw))
            #print(clubNames)
            #returns all club names

            reg = r'<td data-title="ATT"><span class="label rating r[1|2|3|4]">(\d+)'
            offenseScores = re.findall(reg, str(raw))
            #print(offenseScores)
            #returns all offenseScores

            reg = r'<td data-title="MID"><span class="label rating r[1|2|3|4]">(\d+)'
            midfieldScores = re.findall(reg, str(raw))
            #print(midfieldScores)
            #returns all midfieldScores

            reg = r'<td data-title="DEF"><span class="label rating r[1|2|3|4]">(\d+)'
            defenseScores = re.findall(reg, str(raw))
            #print(defenseScores)
            #returns all defenseScores

            reg = r'<td data-title="OVR"><span class="label rating r[1|2|3|4]">(\d+)'
            overallScores = re.findall(reg, str(raw))
            #print(overallScores)
            #returns all overallScores
            if(yearparam[i] == '12_9'):#Arsenal scores from 2012 was classified under Pro League
                clubNames.append('Arsenal')
                offenseScores.append('84')
                midfieldScores.append('80')
                defenseScores.append('81')
                overallScores.append('81')
                #print(offenseScores)
            if(yearparam[i] == '13_10'): #Southampton scores for 2012-2013 for some reason was classified under MLS(Major League Soccer)
                clubNames.append('Southampton')
                offenseScores.append('73')
                midfieldScores.append('74')
                defenseScores.append('71')
                overallScores.append('73')
            for j in range(len(clubNames)):
                data = [clubNames[j], str(year) + '/' + str(year+1), int(offenseScores[j]), int(midfieldScores[j]), int(defenseScores[j]), int(overallScores[j])]
                # converts the data to numeric form
                writer.writerow(data)
                #writes the rows in the csv file
            year = year + 1
        #for fifa 18
        new_url = url.replace('FIRST', '')
        req = requests.get(new_url)
        raw = req.content
        reg = r'alt="([\s\w]+)"'
        clubNames = re.findall(reg, str(raw))
        #print(clubNames)
        #returns all club names

        reg = r'<td data-title="ATT"><span class="label rating r[1|2|3|4]">(\d+)'
        offenseScores = re.findall(reg, str(raw))
        #print(offenseScores)

        reg = r'<td data-title="MID"><span class="label rating r[1|2|3|4]">(\d+)'
        midfieldScores = re.findall(reg, str(raw))
        #print(midfieldScores)

        reg = r'<td data-title="DEF"><span class="label rating r[1|2|3|4]">(\d+)'
        defenseScores = re.findall(reg, str(raw))
        #print(defenseScores)

        reg = r'<td data-title="OVR"><span class="label rating r[1|2|3|4]">(\d+)'
        overallScores = re.findall(reg, str(raw))
        #print(overallScores)

        for j in range(len(clubNames)):
            data = [clubNames[j], str(year) + '/' + str(year+1), int(offenseScores[j]), int(midfieldScores[j]), int(defenseScores[j]), int(overallScores[j])]
            writer.writerow(data)
        ##print(raw)
    print ("DONE")

fifaratings()
