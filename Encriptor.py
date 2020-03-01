SYMBOLS = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя'
Max_Key_Size = len(SYMBOLS)


def getMode():
    while True:
        print("Шифровать или дешифровать текст?")
        mode = input().lower()
        if mode in ["шифровать", "ш", "дешифровать", "д"]:
            return mode
        else:
            print('Введите "шифровать" или "ш" для зашифровки или "дешифровать" или "д" для дешифровки ')


def getMessage():
    print("Введите исходный текст:")
    return input()


def getKey():
    key = 0
    while True:
        print("Введите ключ 1-%s" % Max_Key_Size)
        key = int(input())
        if key >= 1 and key <= Max_Key_Size:
            return key


def getTranslatedMessage(mode, message, key):
    if mode[0] == "д":
        key = -key
    translated = ''

    for symbol in message:
        symbolIndex = SYMBOLS.find(symbol)
        if symbolIndex == -1:
            translated += symbol
        else:
            symbolIndex += key

            if symbolIndex >= len(SYMBOLS):
                symbolIndex -= len(SYMBOLS)
            elif symbolIndex < 0:
                symbolIndex += len(SYMBOLS)

            translated += SYMBOLS[symbolIndex]

    return translated


mode = getMode()
message = getMessage()
key = getKey()
print("Измененный текст:")
print(getTranslatedMessage(mode, message, key))
