import sys
import re
import utils.tagDelimiters as tagDelimiters
from bs4 import BeautifulSoup
import html2text
import time
from googletrans import Translator
from ast import literal_eval


translator = Translator(service_urls=[
      'translate.google.com',
      'translate.google.co.kr',
      'translate.google.it'
    ], user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.' \
                    '3770.100 Safari/537.36')

def myTranslate(string, src, dest='en'):
    strTranslate = translator.translate(string, src=src, dest=dest).text


def getMovieTable(body, tableclass):
    soupObj = BeautifulSoup(body, 'html.parser')
    bodyNew2 = soupObj.find_all('table', attrs={'class': tableclass})
    movieList = list()
    for rows in bodyNew2:
        table = rows.find_all('tr')
        findHead = 0
        for cols in table:
            movieInformation = {"title": None, "year": None, "pageURL": None}
            if(findHead == 0):
                findHead = 1
                continue
            low_table = cols.find_all(['th', 'td'])
            # print(low_table)
            for i in range(len(low_table)):
                if(i > 1):
                    break
                element = low_table[i]
                if(i == 0):
                    headDetails = element('a')
                    for keys in headDetails:
                        if(keys):
                            this_element = keys.get('title')
                            this_element = this_element.replace("\xe2\x80\x93", "-").replace("x2 x80 x93", "-"). \
                                replace("\xa0", " ").replace("\\", "")
                            movieInformation.update({"title": this_element})
                            this_element = keys.get('href')
                            this_element = "https://en.wikipedia.org" + this_element
                            movieInformation.update({"pageURL": this_element})
                            break
                    continue
                elif(i == 1):
                    if (element.string != None):
                        this_element = element.string
                        movieInformation.update({"year": this_element})
                        movieList.append(movieInformation)
                        break
        break
    return movieList


def getMovieInfoTable(body, tableclass):
    soupObj = BeautifulSoup(body, 'html.parser')
    bodyNew2 = soupObj.find_all('table', attrs={'class': tableclass})
    movieInformation = {"title": None, "budget": 0, "collection": 0, "duration": 0, "released": None}
    foundTitle = 0
    for rows in bodyNew2:
        table = rows.find_all('tr')
        for cols in table:
            # print(cols)
            low_table = cols.find_all(['th', 'td'])
            # print(low_table)
            for i in range(len(low_table)):
                element = low_table[i]
                if (foundTitle == 0):
                    this_element = element.text.replace("\xe2\x80\x93", "-").replace("x2 x80 x93", "-"). \
                        replace("\xa0", " ").replace("\\", "")
                    movieInformation.update({"title": this_element})
                    foundTitle = 1
                    continue
                foundText = 0
                if(element.string != None):
                    if(element.string.lower() == "budget"):
                        for keys in low_table[i+1]:
                            this_element = keys.replace("\xe2\x80\x93", "-").replace("x2 x80 x93", "-").\
                                replace("\xa0", " ")
                            movieInformation.update({"budget": this_element})
                            break
                    if (element.string.lower() == "box office"):
                        for keys in low_table[i+1]:
                            this_element = keys.replace("\xe2\x80\x93", "-").replace("x2 x80 x93", "-").\
                                replace("\xa0", " ")
                            movieInformation.update({"collection": this_element})
                            break
                    if (element.string.lower() == "running time"):
                        for keys in low_table[i + 1]:
                            this_element = keys.replace("\xe2\x80\x93", "-").replace("x2 x80 x93", "-").\
                                replace("\xa0", " ")
                            movieInformation.update({"duration": this_element})
                            break
                    if (element.string.lower() == "release date"):
                        dates = low_table[i + 1]
                        if(dates.string != None):
                            this_date = dates.string
                            movieInformation.update({"released": this_date})
                            continue
                        else:
                            try:
                                this_date = dates.text.split("\\n")[1]
                                this_date = this_date.replace("\xe2\x80\x93", "-").replace("x2 x80 x93", "-").\
                                    replace("\xa0", " ")
                                movieInformation.update({"released": this_date})
                                continue
                            except:
                                continue
                        # this_element = element.string.replace("\\xe2\\x80\\x93", "-").replace("x2 x80 x93", "-")
                        # print(this_element)
                else:
                    continue
                    aElement = element.find_all('a')
                    for keys in aElement:
                        if(keys):
                            this_element = keys.get('title')
                            if(this_element != None):
                                foundText = 1
                                this_element = this_element.replace("\\xe2\\x80\\x93", "-").replace("x2 x80 x93", "-")
                                # print(this_element)
                    if(foundText == 0):
                        for keys in element:
                            # print(keys)
                            break
        break
    print(movieInformation)
    bodyNew = [bodyNew2]
    return bodyNew


def getTextFromEnglishPage(body):
    bodyNew = html2text.html2text(body)
    print("Got html2text")
    bodyNew = bodyNew.replace("\\xe2\\x80\\x93", "-").replace("x2 x80 x93", "-")
    for delim in tagDelimiters.noisyText:
        bodyNew = bodyNew.replace(delim, '')
    bodyNew1 = bodyNew.splitlines()
    bodyNew2 = []
    for line in bodyNew1:
        tempStr = line.strip(' ')
        if(tempStr == ''):
            continue
        elif( (line == '') or (line == ' ') or ("www." in line) or ("http" in line) ):
            continue
        else:
            bodyNew2.append(line)
            '''
            flagFound = 0
            for delim in tagDelimiters.noisyText:
                if(delim in line):
                    try:
                        print(line)
                        newVal = literal_eval("b'{}'".format(line)).decode('utf-8')
                        print("Decoded and Pushing ", newVal)
                        bodyNew2.append(newVal)
                        flagFound = 1
                    except:
                        pass
                    break
            if(flagFound == 0):
                bodyNew2.append(line)
            '''
    return bodyNew2

def getTextFromPage(body):
    bodyNew = html2text.html2text(body)
    #for line in bodyNew.splitlines():
    #    print(myTranslate(line, 'auto', 'en')
    try:
        bodyNew1 = myTranslate(str(bodyNew), 'it', 'en')
    except:
        print("Unable to translate")
        time.sleep(5)
        try:
            bodyNew1 = myTranslate(str(bodyNew), 'it', 'en')
        except:
            print("Second Attempt Failed")
            bodyNew1 = bodyNew
    for delim in tagDelimiters.noisyText:
        bodyNew1 = bodyNew1.replace(delim, '')
    bodyNew1 = bodyNew1.splitlines()
    bodyNew2 = []
    for line in bodyNew1:
        tempStr = line.strip(' ')
        if(tempStr == ''):
            continue
        elif( (line == '') or (line == ' ') or ("www." in line) or ("http" in line) ):
            continue
        else:
            # lineTrans = myTranslate(str(line), 'auto', 'en')
            bodyNew2.append(line)
    return bodyNew2


def cleanExtractedText(string):
    for delim in tagDelimiters.delimiters:
        string = re.sub(delim, '', string)
    return string


## Other Functions


def getTextFromWikiFile(filename):
    with open(filename, "r", encoding="utf-8") as infile:
        readText = infile.readlines()
        for line in readText:
            temp = line
            print(temp)
            for delim in tagDelimiters.delimiters:
                temp = re.sub(delim, '', temp)
            print(temp)
            break
    return

def getSoupTextFromPage(body):
    soupObj = BeautifulSoup(body, 'html.parser')
    bodyNew2 = soupObj.get_text()
    bodyNew2 = str(bodyNew2).split('*')
    return bodyNew2

def getAllParasFromPage(body):
    soupObj = BeautifulSoup(body, 'html.parser')
    bodyNew2 = soupObj.find_all("p")
    bodyNew = [bodyNew2]
    return bodyNew


def getAllTextFromPage(body):
    soupObj = BeautifulSoup(body, 'html.parser')
    bodyNew2 = soupObj.find_all('div')
    bodyNew = [bodyNew2]
    return bodyNew


def getSpecificDivFromPage(body, divclass):
    soupObj = BeautifulSoup(body, 'html.parser')
    bodyNew2 = soupObj.find_all('div', attrs={'class': divclass})
    bodyNew = [bodyNew2]
    return bodyNew

def getAllDivFromPage(body):
    soupObj = BeautifulSoup(body, 'html.parser')
    bodyNew2 = soupObj.find_all('div')
    bodyNew = [bodyNew2]
    return bodyNew


def getSpecificSpanFromPage(body, spanclass):
    soupObj = BeautifulSoup(body, 'html.parser')
    bodyNew2 = soupObj.find_all('span', attrs={'class': spanclass})
    bodyNew = [bodyNew2]
    return bodyNew


def getAllSpanFromPage(body):
    soupObj = BeautifulSoup(body, 'html.parser')
    bodyNew2 = soupObj.find_all('span')
    bodyNew = [bodyNew2]
    return bodyNew


def getScriptsFromPage(body):
    soupObj = BeautifulSoup(body, 'html.parser')
    bodyNew2 = soupObj.find_all('script')
    bodyNew = [bodyNew2]
    return bodyNew


def getJSONFromPage(body):
    soupObj = BeautifulSoup(body, 'html.parser')
    bodyNew2 = soupObj.find_all('script', type='application/json')
    bodyNew = [bodyNew2]
    return bodyNew


if __name__ == "__main__":
    arg = sys.argv[1]
    getTextFromWikiFile(arg)