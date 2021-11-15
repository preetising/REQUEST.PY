book={}
book['tom']={
    "name":"uajal",
    "adder":"dlehi",
    "phone":8745903709
}
book['bob']={
    "name":"bobo",
    
    "adderess":"i like to talk",
    "phone":23456789
}

import json
y=json.dumps(book)
print(y)