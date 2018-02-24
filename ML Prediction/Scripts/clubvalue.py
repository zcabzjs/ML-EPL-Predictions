import requests
import sys
import re
import csv
import time

def clubValue() :
    #various parameters and ids that were used by transfermarkt for each club
    clubId = ['11', '989', '1237', '1132', '631', '873', '29', '1110', '1003', '31', '281', '985', '762', '180', '512', '2288', '148', '1010', '984', '379']
    clubparam=['arsenal-fc', 'afc-bournemouth', 'brighton-amp-hove-albion', 'burnley-fc', 'chelsea-fc', 'crystal-palace', 'everton-fc', 'huddersfield-town','leicester-city', 'liverpool-fc', 'manchester-city', 'manchester-united', 'newcastle-united', 'southampton-fc', 'stoke-city', 'swansea-city', 'tottenham-hotspur', 'watford-fc', 'west-bromwich-albion', 'west-ham-united']
    clubs=['Arsenal', 'Bournemouth', 'Brighton', 'Burnley', 'Chelsea', 'Crystal Palace', 'Everton', 'Huddersfield', 'Leicester', 'Liverpool', 'Man City', 'Man United', 'Newcastle', 'Southampton', 'Stoke', 'Swansea', 'Tottenham', 'Watford', 'West Brom', 'West Ham']

    url = 'https://www.transfermarkt.co.uk/CLUBPARAM/kader/verein/CLUBID/plus/0/galerie/0?saison_id=YEAR'
    #Credits to transfermarkt for providing detailed information of teams for each season
    myFile = open('clubValues.csv', 'wb')
    startingYear = 2005
    currentYear = 2018
    #Transermarkt did not allow python 'user-agent', thus had to use a 'Google Chrome' user-agent for headers
    headers={
        'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/525.13 (KHTML, like Gecko) Chrome/0.2.149.27 Safari/525.13',
    }
    with myFile:
        writer = csv.writer(myFile)
        firstrow = ['Team','Season','Market Value']
        writer.writerow(firstrow)
        for year in range(startingYear, currentYear):
            for j in range(len(clubparam)):
                new_url = url.replace('CLUBPARAM', clubparam[j]).replace('CLUBID', clubId[j]).replace('YEAR', str(year))
                #print(new_url)
                req = requests.get(new_url, headers = headers)
                #print(req)
                raw = req.content
                # Finding market value that is in the form £88.8m
                reg ='\xa3(\d+\.\d+)m</td>\s+<td class="rechts">'
                results = re.findall(reg, str(raw), re.UNICODE)
                if(len(results) > 0):
                    marketValue = results[-1]
                    data = [clubs[j], str(year) + '/' + str(year+1), float(marketValue)*1000000]
                    writer.writerow(data)
                else:
                    # Finding market value that is in the form £88.8k
                    reg ='\xa3(\d+)k</td>\s+<td class="rechts">'
                    results = re.findall(reg, str(raw), re.UNICODE)
                    marketValue = results[-1]
                    data = [clubs[j], str(year) + '/' + str(year+1), float(marketValue)*1000]
                    writer.writerow(data)

                time.sleep(0.001)
    print ("DONE")

clubValue()
