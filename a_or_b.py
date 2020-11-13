a_or_b = input("a or b:")


def a(a):
    readytext = a.split()
    for i in readytext:
        if len(i) < 3:
            readytext.pop(readytext.index(i))
        i.strip()
        if not i[len(i)-1].isalnum():
            readytext[readytext.index(i)] = i[:len(i)-1]
        print(i)

    readytext.sort(key=str.lower)
    print(readytext)


def b(a):
    readytext = a.casefold()
    
    alpha = {"a": 0, "b": 0, "c": 0, "d": 0, "e": 0, "f": 0, "g": 0, "h": 0, "i": 0, "j": 0, "k": 0, "l": 0, "m": 0,
             "n": 0, "o": 0, "p": 0, "q": 0, "r": 0,
             "s": 0, "t": 0, "u": 0, "v": 0, "w": 0, "x": 0, "y": 0, "z": 0}
    for i in range(len(a)):
        if not readytext[i].isalpha():
            continue
        alpha[readytext[i]] += 1
    for x, y in alpha.items():
        print(x, "=", y)


if a_or_b == "a":
    a(input("Enter text:"))
elif a_or_b == "b":
    b(input("Enter text:"))
else:
    print("ne to vvel")
