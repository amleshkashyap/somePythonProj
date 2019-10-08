import pywikibot
import sys

def pageQuery(query):
    site = pywikibot.Site()
    pageTemp = pywikibot.Page(site, query)
    if pageTemp.exists():
        if pageTemp.isRedirectPage():
            page = pageTemp.getRedirectTarget()
        else:
            page = pageTemp.get()
        return page
    else:
        raise Exception("Page Doesn't Exist")


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Need the type of search as argument 1 and query as the rest")
        exit()
    else:
        arg = ""
        argTemp = sys.argv[2:]
        for key in argTemp:
            arg = arg + " " + key
        ''' 
        if sys.argv[1].lower() == "search":
            print(searchQuery(arg))
        elif sys.argv[1].lower() == "summary":
            print(summaryQuery(arg))
        '''
        if sys.argv[1].lower() == "page":
            page = pageQuery(arg)
            #print(page.text)
            try:
                fullPage = page.get(get_redirect=True)
                with open('blackmirror.txt', 'w', encoding='utf-8') as f:
                    for key in fullPage:
                        f.writelines(key)
                f.close()

            except Exception as err:
                print(err)
                exit()
        else:
            print("Invalid type, enter search, summary or page")