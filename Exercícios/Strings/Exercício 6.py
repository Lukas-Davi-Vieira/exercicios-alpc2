letter_to_number = {
    'A': '4',     
    'B': '13',   
    'C': '¢',     
    'D': '7',     
    'E': '3',     
    'F': None,    
    'G': '9',     
    'H': '8',     
    'I': '1',     
    'J': None,    
    'K': None,    
    'L': None,    
    'M': '11',
    'N': None,    
    'O': '0',     
    'P': None,    
    'Q': None,    
    'R': None,    
    'S': '5',     
    'T': None,    
    'U': None,    
    'V': None,    
    'W': None,    
    'X': '8',     
    'Y': None,    
    'Z': '2'
}

letter_to_number = {k: v for k, v in letter_to_number.items() if v is not None}

text = input("Insira qualquer texto para converter para leet speak\n").upper()
leet_text = list()

for i in text:
    if i in letter_to_number:
        leet_text.append(letter_to_number[i])
    else:
        leet_text.append(i)

leet_text = "".join(leet_text)

print(leet_text)
