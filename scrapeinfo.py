import json, re


Creature = "(Legendary )?(Enchantment )?(Artifact )?Creature — .*"
with open('scryfall-all-cards.json') as file:
    data = json.load(file);

    print(len(data));
    for obj in data:
        if (re.match(Creature,obj['type_line'])):
            cType = obj['type_line'].split(" — ",1)[1];
            #print(cType.split(" "));
            if ('Aura' in cType):
                pass#print(obj);
            if (obj['object'] != 'card'):
                print(obj);
            if (obj['name'] == "Child of Night"):
                print('got')
