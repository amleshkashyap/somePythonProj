'''
request_link = urllib.request.Request(pageLink, None, headers)
        request_page = str(urllib.request.urlopen(request_link).read())
        # request_page_text = parseFile.getTextFromPage(request_page)
        request_page_text = parseFile.getTextFromEnglishPage(request_page)

https://en.wikipedia.org/wiki/Pirates_of_the_Caribbean:_At_World%27s_End
'''

