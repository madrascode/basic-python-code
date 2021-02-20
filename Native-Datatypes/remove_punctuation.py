punctuation = ''' !()-[]{},:;'"<>./!@#$%^&*_-=|'''

my_string = "HEllo !@ , he said -----_________-------- and went|.............._____-----__-_-____-----__"


no_puntuation= ""
for char in my_string:
    if char not in punctuation:
        no_puntuation += char

print(no_puntuation.casefold()) 