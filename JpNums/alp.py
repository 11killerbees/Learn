import random
"""
あいうえお
かきくけこ
さしすせそ
"""
def letter():
    allJp =["あ","い","う","え","お","か","き","く","け","こ","さ","し","す","せ","そ"]
    allEn =["a","i","u","e","o","ka","ki","ku","ke","ko","sa","si","su","se","so",]

    aEn = ["a","i","u","e","o"]
    aJp = ["あ","い","う","え","お"]
    kEn = ["ka","ki","ku","ke","ko"]
    kJp = ["か","き","く","け","こ"]
    sEn = ["sa","si","su","se","so",]
    sJp = ["さ","し","す","せ","そ"]
            # english
    lang1 = allEn
            # japanise
    lang2 = allJp

    num = random.randint(0,len(lang1)-1)
    jp = lang2[num]
    print(jp)
    print("input: ")
    check = input()
    check = lang1.index(check)

    if lang2[check] == jp:
        print("right")
    else:
        print("wrong")
        print("answer is ",lang1[num])

for i in range(50):
    letter()