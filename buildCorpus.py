import json, re
from pprint import pprint

def cleanOracle(oracle,name):
    oracle=oracle.replace(name,"~").replace('\n',' ');
    oracle=re.sub(r'\(.*\)','',oracle);
    return oracle;

with open('scryfall-all-cards.json') as j:
    data = json.load(j);

i=1;


f = open("fuckme.txt","a");

for card in data:
    if ('oracle_text' in card and  'lang' in card and card['lang'] == "en" and 'type_line' in card and "land" not in card['type_line'].lower()):
        temp="item "+str(i)+"|"+card['name']+"|";
        temp=temp+card['type_line']+"|";
        if ('colors' in card):
            for color in card['colors']:
                temp+=color;
        else:
            temp+="C"
        temp=temp+cleanOracle(card['oracle_text'],card['name'])+"|\n";
        i=i+1;
        f.write(temp.encode('utf-8'));
    if ('oracle_text' not in card):
        #total(card['name']+" has no oracle Text");
        pass;

f.close();
