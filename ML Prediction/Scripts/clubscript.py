import requests
import sys
import re
import csv


def clubscript() :

    clubparam=['arsenal', 'bournemouth', 'brighton-hove-albion', 'burnley', 'chelsea', 'crystal-palace', 'everton', 'huddersfield-town','leicester-city', 'liverpool', 'manchester-city', 'manchester-united', 'newcastle-united', 'southampton', 'stoke-city', 'swansea-city', 'tottenham-hotspur', 'watford', 'west-bromwich-albion', 'west-ham-united']
    clubs=['Arsenal', 'Bournemouth', 'Brighton', 'Burnley', 'Chelsea', 'Crystal Palace', 'Everton', 'Huddersfield', 'Leicester', 'Liverpool', 'Man City', 'Man United', 'Newcastle', 'Southampton', 'Stoke', 'Swansea', 'Tottenham', 'Watford', 'West Brom', 'West Ham']
    #Clubparam are parameters used by the website below
    url = 'http://www.sportmapworld.com/distance/FIRST/SECOND/'
    #Credits to sportmapworld for providing distances between stadiums
    myFile = open('clubdistance.csv', 'wb')
    with myFile:
        writer = csv.writer(myFile)
        firstrow = ['Home','Away','Distance']
        writer.writerow(firstrow)
        for i in range(len(clubs)):
            for j in range(len(clubs)):
                if (i == j):
                    continue
                new_url = url.replace('FIRST', clubparam[i]).replace('SECOND', clubparam[j])
                #print(new_url)
                req = requests.get(new_url)
                raw = req.content
                reg = r'\((\d+ kilometres)\)'
                #Requesting HTML page and finding regex that returns %%%% kilometres
                distances = re.findall(reg, str(raw))
                #Deleting the last 11 letter from the string (15 kilometres => 15)
                distance = distances[0][:-11]
                data = [clubs[i], clubs[j], distance]
                writer.writerow(data)
                #print int(distance)
    print ("DONE")

clubscript()
