poll_talen = ["Lucas", "Maud", "Jan", "Dillan", 
              "Piet", "Joris"]

favorite_languages = {    
    "Jan": "python",    
    "Piet": "c",    
    "Joris": "ruby"}

dict = {

}
for naam in poll_talen:
    if naam in favorite_languages:
        print(f'{naam} bedankt voor deelname')
    else:
        print(f'{naam} moeten nog deelnemen')
        x = input()
        if x != "":
            favorite_languages[naam] = x
print(favorite_languages)

# for namen in poll_talen:
#     print(namen)
#     x = input()
#     namen.append(x)
#     print(namen)