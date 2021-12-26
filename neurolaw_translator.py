import re

def temporal_expressions_pt_to_eng(text_in_pt):
    text_in_pt = text_in_pt.lower()
    text_in_en = text_in_pt.replace("ontem", "yesterday")
    text_in_en = text_in_en.replace("fevereiro", "february")
    text_in_en = text_in_en.replace("outubro", "october")
    text_in_en = text_in_en.replace("setembro", "september")
    text_in_en = text_in_en.replace("vigésimo", "twentieth")
    text_in_en = text_in_en.replace("primeiro dia", "1st")
    text_in_en = text_in_en.replace("do mês de ", "")
    text_in_en = text_in_en.replace(" dois ", " two ")
    text_in_en = text_in_en.replace(" dias ", " days ")
    text_in_en = text_in_en.replace(" dia ", " day ")
    text_in_en = text_in_en.replace("depois", "later")
    text_in_en = text_in_en.replace(r'd'+' de', r'd'+'th')
    #text_in_en = text_in_en.replace("tarde", "afternoon")

    result = re.search(r'\d\d de', text_in_en)
    while(result is not None):
        text_in_en_1 = text_in_en[0:result.span()[0]+2]
        text_in_en_2 = "th" + text_in_en[result.span()[1]:len(text_in_en)]
        text_in_en = text_in_en_1 + text_in_en_2
        result = re.search(r'\d\d de', text_in_en)

    result = re.search(r'\d de', text_in_en)
    while(result is not None):
        text_in_en_1 = text_in_en[0:result.span()[0]+1]
        if text_in_en_1[result.span()[0]] in "1":
            text_in_en_2 = "st" + text_in_en[result.span()[1]:len(text_in_en)]
        else:
            if text_in_en_1[result.span()[0]] in "2":
                text_in_en_2 = "nd" + text_in_en[result.span()[1]:len(text_in_en)]
            else:
                text_in_en_2 = "th" + text_in_en[result.span()[1]:len(text_in_en)]
        text_in_en = text_in_en_1 + text_in_en_2
        result = re.search(r'\d de', text_in_en)

    result = re.search(r'de \d\d\d\d', text_in_en)
    while(result is not None):
        text_in_en_1 = text_in_en[0:result.span()[0]]
        text_in_en_2 = text_in_en[result.span()[1]-4:len(text_in_en)]
        text_in_en = text_in_en_1 + text_in_en_2
        result = re.search(r'de \d\d\d\d', text_in_en)

    return text_in_en

#str = "o primeiro dia do mês de fevereiro de 2022"
#print(temporal_expressions_pt_to_eng(str))
