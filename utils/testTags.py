import sys
import re
#import scrapy_proj.scrapy_proj.util.timeTypes as timeTypes
#import scrapy_proj.scrapy_proj.util.regexGroups as regexGroups
import timeTypes
import regexGroups

noisyText = ['\\\\n', '\\t', '\\\\t', "\\xc2\\xa0", '\\xc3\\xac', '\\xc2\\xa8', '\\xc3\\xb9', '\\xc3\\xa0', '\\xc3\\xb2']


if __name__ == "__main__":
    text = str(sys.argv[1])
    #for delim in noisyText:
    #    print(delim)
    #    print(text.replace(delim, ''))
    lineStr = text.lower().replace("a.m.", "am").replace("a.m", "am").replace("p.m.", "pm"). \
        replace("p.m", "pm").replace("–", "-")
    print(lineStr)

    for type in timeTypes.timeIdentifiers:
        if (type in lineStr):
            # print("Found " + lineStr)
            # tempStr1 = group_time_num_hyph.findall(lineStr)
            # tempStr2 = group_time_letter_hyph.findall(lineStr)
            # tempStr1 = regexGroups.group_time_all_hyph.findall(lineStr)
            # tempStr2 = regexGroups.group_time_all_to.findall(lineStr)
            tempStr1 = regexGroups.groupAllTime.finditer(lineStr)
            tempStr2 = regexGroups.groupAllDays.findall(lineStr)
            tempStr3 = regexGroups.groupAllMonths.findall(lineStr)
            tempStr4 = regexGroups.groupAllTime.findall(lineStr)
            for blah in tempStr1:
                print(blah)
            # print(tempStr1.groups())
            print(tempStr2)
            print(tempStr3)
            print(tempStr4)
            break