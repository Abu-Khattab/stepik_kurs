# ''' шифр Цезаря '''
#
# def caesar_cipher(text, shift):
#     result = ""
#     alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
#
#     for char in text:
#         if char in alphabet:
#             index = (alphabet.index(char) + shift) % len(alphabet)
#             result += alphabet[index]
#         else:
#             result += char
#
#     return result
#
#
# text = "Блажен, кто верует, тепло ему на свете!"
# shift = 10
# encrypted_text = caesar_cipher(text.lower(), shift)
# print(encrypted_text)



# ''' шифр Цезаря '''
#
#
# text = input()
# n = int(input())
#
# code_text = ''
# for char in text:
#     if char.isalpha():
#         code_text += chr(ord(char) + n)
#     else:
#         code_text += char
#
#
# print(code_text)



''' шифр Цезаря '''


eng_lower_alphabet = 'abcdefghijklmnopqrstuvwxyz'
eng_upper_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
rus_lower_alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
rus_upper_alphabet = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
symbol = [" ", ",", ".", "!", "?"]

print("Выберите язык: aнгл=e, рус=r")
lan = input()
print("Выберите шифрование: шифрование - ch, дешифрование - def")
chif = input()
print("Введите ключ шифрования")
n = int(input())
print("Введите фразу")
f = input()

def chru(chifr, n, l, fraza):
    if l == 'r':
        moch = 32
    if l == 'e':
        moch = 26
    if chifr== 'def':
        n = -n
    for i in range(len(fraza)):
        if fraza[i].isalpha():
            if fraza[i] == fraza[i].upper():
                for j in range (moch):
                    if moch == 32:
                        if fraza[i] == rus_upper_alphabet[j]:
                            print(rus_upper_alphabet[(j+n)%moch], end = '')
                            break
                    if moch == 26:
                        if fraza[i] == eng_upper_alphabet[j]:
                            print(eng_upper_alphabet[(j+n)%moch], end = '')
                            break
            elif fraza[i] ==fraza[i].lower():
                for j in range (moch):
                    if moch == 32:
                        if fraza[i] == rus_lower_alphabet[j]:
                           print(rus_lower_alphabet[(j+n)%moch], end='')
                           break
                    if moch == 26:
                        if fraza[i] == eng_lower_alphabet[j]:
                           print(eng_lower_alphabet[(j+n)%moch], end = '')
                           break
        else:
            print(fraza[i], end='')

chru(chif, n, lan, f)