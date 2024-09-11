def check_a_letter(text):
    text_lower = text.lower()
    
    count_a = text_lower.count('a')
    
    if count_a == 0:
        return f"The provided text doesn't have any letter a on it"
    
    return f"The provided text has {count_a} letter a on it"

text = input("Type a text: ")

print(check_a_letter(text))
