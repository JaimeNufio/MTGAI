import json, re, random
from pprint import pprint

def cleanOracle(oracle,name):
    oracle=oracle.replace(name,"~").replace('\n',' ');
    oracle=re.sub(r'\(.*\)','',oracle);
    return oracle;

def label(color):
    return "__label__"+color+" ";

def concat(colorList):
    temp="";
    temp=temp+temp.join(sorted(colorList));
    return "__label__"+temp+" "
    #Instead of using WUBRG, just sort alphabetically


with open('scryfall-all-cards.json') as j:
    data = json.load(j);

i=1;

#TODO strip out all brackets (Should still read properly as lexical units

f = open("corpusNew.txt","wb");#a for append

for card in data:
    #and len(card['colors'])<2
    if ('colors' in card  and 'oracle_text' in card  and 'type_line' in card and "land" not in card['type_line'].lower()):
    #if ('oracle_text' in card and  'lang' in card and card['lang'] == "en" and 'type_line' in card and "land" not in card['type_line'].lower()):
        temp= concat(card['colors']) if 'colors' in card and len(card['colors']) > 1 else "";
        #temp="item "+str(i)+"|"+card['name']+"|";
        #temp=temp+card['type_line']+"|";
        if ('colors' in card):
            for color in card['colors']:
                temp+=label(color);
            if (len(card['colors'])<1):
                temp+=label("C")
        temp=temp+cleanOracle(card['oracle_text'],card['name'])+"\n";
        temp=temp.lower();
        i=i+1;
        print(temp);
        f.write(temp.encode('utf-8'));
    if ('oracle_text' not in card):
        #total(card['name']+" has no oracle Text");
        pass;

f.close();

#Scramble Lines
#Why? Well, the cards are ordered by rlease date, and therefore biased by order

with open('corpusNew.txt','r') as src:
    data = [(random.random(), line) for line in src]
data.sort()
with open('corpusReady.txt','w') as out:
    for _, line in data:
        out.write(line);
