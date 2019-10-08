import wikipedia
import pywikibot
import sys
import traceback

def checkPageExistence(query):
    print(query)
    site = pywikibot.Site()
    page = pywikibot.Page(site, query)
    print(query)
    if (page.exists()):
        return True
    else:
        return False

def searchQuery(query):
    print(query)
    pageCheck = checkPageExistence(query)
    if(pageCheck):
        try:
            search = wikipedia.search(query, results=1)
            return search
        except:
            exc_type, exc_value, exc_traceback = sys.exc_info()
            print(exc_value)
            if("Disambiguation" in exc_value):
                print("Disambiguation Error")
            exit()
    else:
        return "No Wikipedia Page Exists"


def summaryQuery(query):
    pageCheck = checkPageExistence(query)
    if (pageCheck):
        try:
            search = wikipedia.summary(query)
            return search
        except:
            print("No wikipedia page")
            exit()
    else:
        return "No Wikipedia Page Exists"


def pageQuery(query):
    pageCheck = checkPageExistence(query)
    if (pageCheck):
        try:
            search = wikipedia.page(query)
            return search
        except:
            print("No wikipedia page")
            exit()
    else:
        return "No Wikipedia Page Exists"


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Need the type of search as argument 1 and query as the rest")
        exit()
    else:
        arg = ""
        argTemp = sys.argv[2:]
        for key in argTemp:
            arg = arg + " " + key
        if sys.argv[1].lower() == "search":
            print(searchQuery(arg))
        elif sys.argv[1].lower() == "summary":
            print(summaryQuery(arg))
        elif sys.argv[1].lower() == "page":
            wikipage = pageQuery(arg)
            print(wikipage)
            print(wikipage.url)
        else:
            print("Invalid type, enter search, summary or page")