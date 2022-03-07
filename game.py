text = "The sunset sets at twelve o' clock."
def alphabet_position(text):
    string =""
    
    for char in text.lower():
        if char.isalpha():
            string += str(ord(char)-96)+' '
            
        elif char == " ":
            continue
        else:
            pass
    if string[-1]==' ':
        string = string.rstrip(string[-1])
    return string

print(alphabet_position(text))