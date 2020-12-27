# json = java script object notation 
import json
p = '{"employee":{"name":"priya ranjan","salary":56000,"married":false} }'
print(type(p))
#  loads

# Convert Json into dictionary

p_dict = json.loads(p)  
print(p_dict)
print(type(p_dict))

'''
    Python                  JSON

    ------------------------------
    dict                    object
    list,tuple              array   
    str                     string
    int,float,int           number
    True                    true    
    False                   false
    None                    null

'''



print('-'*25)

# --------------------------------------------------------
# With the help of load we can work with files.

with open(r"json.txt") as f:
    data = json.load(f)
print(data)
print(type(data))

print('-'*25)


'''
    loads() -> json string ko dictionary me convert karta h.
    load() -> json file ko dictionary me convert karta h.

    dumps() -> python dictionary ko json object  me convert karta h.
    dump() ->  python dictionary ko json object me convert karta h or file me save kar deta h.
'''


p = {'employee': {'name': 'priya ranjan', 'salary': 56000, 'married': False}}
s = json.dumps(p,indent=4,sort_keys=True)
print(s,type(s))


print('-'*25)

p = {'employee': {'name': 'priya ranjan', 'salary': 56000, 'married': False}}
with open("saurabh.txt",'w') as f:
    json.dump(p,f,indent=4,sort_keys=True)



print(dir(json))   