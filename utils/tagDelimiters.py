noisyText = ['\\\\n', '\\t',   '\\\\t', '\\n',   '\\r',   '""',
             '\\xa0', '\\xa6', '\\xa7', '\\xa8', '\\xa9', '\\xaa', '\\xac',
             '\\xb0', '\\xb1', '\\xb2', '\\xb8', '\\xb9', '\\xba',
             '\\xc0', '\\xc1', '\\xc2', '\\xc3', '\\xc4',
             '\\xd0', '\\xd1',
             '\\xe2', '\\xea', '\\xed',
             '\\x80', '\\x81', '\\x82', '\\x83', '\\x88', '\\x89', '\\x8b', '\\x8c',
             '\\x90', '\\x98', '\\x93', '\\x94', '\\x95', '\\x99', '\\x9c',
             'x2 x80 x93']
noisyTextNew = ['\\\\n', '\\t',   '\\\\t', '\\n',   '\\r',   '""']

linkStart = "<a href.*>"
supStart = "<sup id=.*"
imgStart = "<img .*>"
divTypes = ['styles__infoItem___72gXC', 'article']
spanTypes = ['styles__infoItemLabel___2siRm']
headerTypes = ['']
scriptTypes = ['']
tagCloseSplitter = "/>"
newlineSplitter = "\n"
tabSplitter = "\t"
paraSplitter = "</p>,"
delimiters = ['<br>', '</br>', '     ', '<em>', '</em>', '<br/>', '<p>', '</p>', '<b>', "</b>", "<i>", "</i>",
              "<li>", "</li>", "<u>", "</u>", "</a>", "</sup>", linkStart, supStart, imgStart]

