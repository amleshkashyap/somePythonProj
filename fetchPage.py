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
        # print(this_movie_table)
        for movies in this_movie_table:
            print(movies)
            if('pageURL' in movies):
                new_request_link = urllib.request.Request(movies['pageURL'], None, headers)
                new_request_page = str(urllib.request.urlopen(new_request_link).read())
                new_request_page_dict = parseFile.getMovieInfoTable(new_request_page, 'infobox vevent')
                movies['details'] = new_request_page_dict
        with open(outfile, 'w', encoding='utf-8') as csvoutfile:
          spamwriter = csv.writer(csvoutfile)
          spamwriter.writerow(["** Original Page ** ", str(request_page)])
          spamwriter.writerow(["** Page Text ** ", str(this_movie_table)])
          spamwriter.writerow(["** All Translated Text ** "])
          for lines in this_movie_table:
              spamwriter.writerow([str(lines)])
          csvoutfile.close()
        return "Success"