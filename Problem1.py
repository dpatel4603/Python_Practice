# wrw blf hvv ozhg mrtsg'h vkrhlwv?
# Yvzs! I xzm'g yvorvev Lzmxv olhg srh qly zg gsv xlolmb!!


def isLower(c):
    if 'a' <= c <= 'z':
        return True
    return False


def decoder(word):
    decoded_message = ''
    for i in range(len(word)):
        if isLower(word[i]):
            c = chr(ord('z') -
                    ord(word[i]) + ord('a'))
            decoded_message += c
        else:
            decoded_message += word[i]
    return decoded_message


code = input("code: ")
print("The decoded message is: " + decoder(code))
