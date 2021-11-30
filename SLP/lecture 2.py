language_name = "Python"
print(language_name)

language_name = "jypton"
print(language_name)
print(language_name.upper())
print(language_name.capitalize())

digit_input = input("write digit: ")

if digit_input.isdigit() and len(digit_input) == 1:
    print("digit")
    digit = int(digit_input)
    print("ready to convert: ", digit)
else:
    print("No digit")

sentence = "Half of climate finance should go to adaptation - UN deputy leader"
sentence = sentence.lower()
sentence = sentence.replace(".", "")
print(sentence.split(" "))
