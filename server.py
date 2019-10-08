import wikiBot
import pywikiBOT
import json
from flask import Flask, request, Response
from fetchPage import fetchURLLib


wikiEngines = [wikiBot, pywikiBOT]
wikiEngineNames = ["wikipedia", "pywikibot"]


def findEngine(engine):
    global wikiEngines, wikiEngineNames
    count = 0
    for key in wikiEngineNames:
        if engine == key:
            engineModule = wikiEngines[count]
            break
        count = count + 1
    if count == len(wikiEngines):
        raise Exception()
    else:
        return engineModule

server = Flask(__name__)


@server.route('/wikiSearch', methods=['GET'])
def searchHandler():
    queryReq = request.get_json()
    query = queryReq['query']
    '''
    engine = queryReq['engine']
    try:
        engineModule = findEngine(engine)
    except:
        return "Invalid Engine Name"
    '''
    search = wikiBot.searchQuery(query)
    jsonDict = {}
    jsonDict['search'] = search
    return Response(json.dumps(jsonDict), status=200, mimetype='application/json')


@server.route('/wikiSummary', methods=['GET'])
def summaryHandler():
    queryReq = request.get_json()
    query = queryReq['query']
    '''
    engine = queryReq['engine']
    try:
        engineModule = findEngine(engine)
    except:
        return "Invalid Engine Name"
    '''
    summary = wikiBot.summaryQuery(query)
    jsonDict = {}
    jsonDict['summary'] = summary
    return Response(json.dumps(jsonDict), status=200, mimetype='application/json')


@server.route('/wikiPage', methods=['GET'])
def pageHandler():
    queryReq = request.get_json()
    print(queryReq)
    query = queryReq['query']
    '''
    engine = queryReq['engine']
    try:
        engineModule = findEngine(engine)
    except:
        return "Invalid Engine Name"
    '''
    page = wikiBot.pageQuery(query)
    jsonDict = {}
    jsonDict['page'] = page.url
    return Response(json.dumps(jsonDict), status=200, mimetype='application/json')


@server.route('/getMovieDetails', methods=['GET'])
def getPageHTML():
    queryReq = request.get_json()
    fetchURL = fetchURLLib()
    movie = queryReq['pageLink']
    # outfile = queryReq['outfile']
    pageFull = wikiBot.pageQuery(movie)
    pageUrl = pageFull.url
    print("Got URL", pageUrl)
    outfile = "pirates_end" + "_.txt"
    # resultSet = fetchURL.fetchByLink(pageUrl)
    resultSet = fetchURL.fetchPageDetails(pageUrl, outfile)
    # return Response(json.dumps(resultSet), status=200, mimetype='application/json')
    return "Blah"


if __name__ == "__main__":
    hostName = "127.0.0.1"
    portNum = 7010
    server.run(host=hostName, port=portNum, debug=True)     # Doesn't work, use cmdline arguments