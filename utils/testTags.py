import sys
import re

noisyText = ['\\\\n', '\\t', '\\\\t', "\\xc2\\xa0", '\\xc3\\xac', '\\xc2\\xa8', '\\xc3\\xb9', '\\xc3\\xa0', '\\xc3\\xb2']


if __name__ == "__main__":
    text = str(sys.argv[1])
    #for delim in noisyText:
    #    print(delim)
    #    print(text.replace(delim, ''))
    lineStr = text.lower().replace("a.m.", "am").replace("a.m", "am").replace("p.m.", "pm"). \
        replace("p.m", "pm").replace("–", "-")
    print(lineStr)