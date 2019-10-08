import utils.parseFile as parseFile
import urllib.request
import csv


# user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.' \
                     '3770.100 Safari/537.36'
headers = {'User-Agent': user_agent, }

class fetchURLLib:
    def fetchPageDetails(self, pageLink, outfile):
        print("Fetching page ", pageLink)
        request_link = urllib.request.Request(pageLink, None, headers)
        request_page = str(urllib.request.urlopen(request_link).read())
        this_movie_table = parseFile.getMovieTable(request_page, 'wikitable plainrowheaders sortable')
        print(this_movie_table)
        for movies in this_movie_table:
            new_request_link = urllib.request.Request(movies.pageURL, None, headers)
            new_request_page = str(urllib.request.urlopen(request_link).read())
            new_request_page_text = parseFile.getMovieInfoTable(request_page, 'infobox vevent')
        # print(request_page_text)
        with open(outfile, 'w', encoding='utf-8') as csvoutfile:
          spamwriter = csv.writer(csvoutfile)
          spamwriter.writerow(["** Original Page ** ", str(request_page)])
          spamwriter.writerow(["** Page Text ** ", str(this_movie_table)])
          spamwriter.writerow(["** All Translated Text ** "])
          for lines in this_movie_table:
              spamwriter.writerow([str(lines)])
          csvoutfile.close()
        return "Success"


    def fetchByLink(self, pageLink):
        print(pageLink)
        request_link = urllib.request.Request(pageLink, None, headers)
        request_page = str(urllib.request.urlopen(request_link).read())
        temp_req_page = request_page
        request_page_text = parseFile.getTextFromPage(request_page)
        '''
        request_page_specific_div = parseFile.getSpecificDivFromPage(request_page, htmlTypes.divTypes[0])
        request_page_all_div = parseFile.getAllDivFromPage(request_page)
        request_page_specific_span = parseFile.getSpecificSpanFromPage(request_page, htmlTypes.spanTypes[0])
        request_page_all_span = parseFile.getAllSpanFromPage(request_page)
        request_page_all_paras = parseFile.getAllParasFromPage(request_page)
        request_page_scripts = parseFile.getScriptsFromPage(request_page)
        request_page_json_scripts = parseFile.getJSONFromPage(request_page)
        '''
        request_page = request_page.split("/>")
        # request_page = urllib.request.urlopen(request_link).read()
        request_page_str = ""
        count = 0
        for line in request_page:
            count = count + 1
        #    if( ("hour" in line) or ("from" in line) or ("open" in line) ):
            request_page_str = request_page_str + "\n" + str(line)
        print("Initial lines "+str(count))
        count = 0
        finalLines = []
        finalLinesRes = []
        # newBody = str(parseFile.getTextFromWikiPage(request_page_str)).split("\n")
        with open("lonelyPlanet_blah1.txt", 'a', encoding='utf-8') as csvoutfile:
          spamwriter = csv.writer(csvoutfile)
          spamwriter.writerow(["** Original Page ** ", str(temp_req_page)])
          for lines in request_page_text:
              spamwriter.writerow(["** All Text Only ** "])
              # spamwriter.writerow([translator.translate(str(line), 'en').text])

          # Other Types of Tags
          '''
          spamwriter.writerow(["** All Div Break Down ** ", str(request_page_all_div)])
          spamwriter.writerow(["** Specific Div Break Down ** ", str(request_page_specific_div)])
          spamwriter.writerow(["** All Span Break Down ** ", str(request_page_all_span)])
          spamwriter.writerow(["** Specific Span Break Down ** ", str(request_page_specific_span)])
          spamwriter.writerow(["** All Paras Break Down ** ", translator.translate(str(request_page_all_paras), 'en')])
          spamwriter.writerow(["** All Scripts Break Down ** ", str(request_page_scripts)])
          spamwriter.writerow(["** JSON Scripts Break Down ** ", str(request_page_json_scripts)])
          '''

          for line in request_page:
            # if('application/json' in line):
                # newLine = json.dumps(line)
                # print(newLine)
                # newLine = str(parseFile.getTextFromWikiPage(line)).split("\n")
            newLine = parseFile.getAllTextFromPage(line)
            # spamwriter.writerow(["Original Line", line])
            # spamwriter.writerow(["Modified Line", newLine])
            # spamwriter.writerow(["****************"])
            # print("Yeah")
            finalLines.append(newLine)
            #for lines in newLine:
            #    finalLines.append(lines.split("\n"))
                # finalLines.append(newLine)
          csvoutfile.close()
        bodyMerge = ""
        for line in finalLines:
            tempLine = []
            # for line in lineArr:
            count = count + 1
            cleanLine = parseFile.cleanExtractedText(str(line))
            # tempLine.append(str(cleanLine))
            #    print(str(line))
            # cleanLine = translator.translate(str(cleanLine),'en')
            # outfile.write(str(cleanLine))
            # bodyMerge = bodyMerge + str(cleanLine)
            finalLinesRes.append(cleanLine)
        # print(str(newBody))
        # outfile.write(str(newBody))
        # bodyEn = translator.translate(bodyMerge, 'en')
        print("Final lines " + str(count))
        resultSet = {}
        resultSet['res1'] = str(request_page_str)
        resultSet['res2'] = finalLines
        resultSet['res3'] = finalLinesRes
        return resultSet