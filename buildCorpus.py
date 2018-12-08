import json, re, random, string
from pprint import pprint

trans = str.maketrans('','',"#$%&(),.;<=>?@[\]^_`|")
def cleanOracle(oracle,name):
    oracle=oracle.replace(name,"~").replace('\n',' ');
    oracle=re.sub(r'\(.*\)','',oracle);
    oracle=oracle.lower();
    oracle=oracle.translate(trans);
    return oracle;

def handleColors(colors):
    temp = "";
    temp1 = "";
    for color in colors:
        temp1 = temp1+color;
        temp = temp+"__label__"+color+" ";

    if len(colors) > 1:
        temp = temp+" __label__"+temp1+" ";
    return temp;

with open('data.json') as j:
    data = json.load(j);

f = open("temp.txt","w"); #a
post = "";

for card in data:
    post=""
    if ('oracle_text' in card  and "land" not in card['type_line'].lower()):

        #post=post+(card['name']);
        if ('colors' in card and len(card['colors']) > 0):
            post=post+handleColors(card['colors']);
        else:
            post=post+"__label__C ";    
        post=post+cleanOracle(card['oracle_text'],card['name'])

        if (card['oracle_text']==""):
            continue;

        f.write(post+"\n")

f.close();

with open('temp.txt','r') as source:
    data = [ (random.random(), line) for line in source ]
data.sort()

with open('corpus.txt','w') as target:
    for _, line in data:
        target.write( line )
print("Done.");
