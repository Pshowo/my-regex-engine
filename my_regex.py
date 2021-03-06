import sys
sys.setrecursionlimit(10000)

def compare_char(reg, word, **kwargs):
    if not kwargs:
        a = True if not reg or (word and not reg) or (not word and not reg) else reg in (".", word)
    else:
        a = True if not reg or (word and not reg) or (not word and not reg) else reg in (word)
    return a


def compare_word(word, **kwargs):    
    reg, word = word.split("|")
    meta_ch = None
    if not reg or (word and not reg) or (not word and not reg):
        return True
    elif reg[0] == "$" and not word:
        return True
    elif reg and not word and reg != "$":
        return False
    else:

        if reg.startswith("^") and compare_char(reg[1], word[0]):
            return compare_word(reg[2:]+"|"+word[1:], meta="^")
        if reg.endswith("$") and len(word) > len(reg) and not kwargs:
            if "\\" in reg:
                count = reg.count("\\")
                return compare_word(reg+"|"+word[-(len(reg)-1-count):], meta="$")
            else:
                return compare_word(reg+"|"+word[-(len(reg)-1):], meta="$")

        elif reg.startswith("^") and not compare_char(reg[1], word[0]):
            return False

        elif len(reg) > 1 and reg[0] == "\\":
            if compare_char(reg[1], word[0], meta_ch=True):
                return compare_word(reg[2:]+"|"+word[1:])
            else:
                if len(word) >= len(reg):
                    return compare_word(reg+"|"+word[1:])
                else:
                    return False

        elif len(reg) > 1 and reg[1] == "?":
            if not compare_char(reg[0], word[0]):
                return compare_word(reg[2:]+"|"+word)
            elif compare_char(reg[0], word[0]) and len(word) == 1:
                return True
            elif compare_char(reg[0], word[0]) and not compare_char(reg[0], word[1]):
                return compare_word(reg[2:]+"|"+word[1:])
            elif reg[0] == "." and compare_char(reg[0], word[1]):
                return compare_word(reg+"|"+word[1:])
            elif compare_char(reg[0], word[1]):
                return False

        elif len(reg) > 1 and reg[1] == "*":
            if reg[0] == "." and len(reg) > 2:
                if len(word) > 1 and compare_char(reg[2], word[1]):
                    return compare_word(reg[2:]+"|"+word[1:])
                elif compare_char(reg[2], word[0]):
                    return True

            if not compare_char(reg[0], word[0]):
                return compare_word(reg[2]+"|"+word)
            if compare_char(reg[0], word[0]) and len(word) == 1:
                return True
            elif compare_char(reg[0], word[0]) and compare_char(reg[0], word[1]):
                return compare_word(reg+"|"+word[1:])
            else:
                return compare_word(reg[2]+"|"+word[1:])

        elif len(reg) > 1 and reg[1] == "+":
            if kwargs:
                meta_ch = kwargs['meta']

            if not compare_char(reg[0], word[0]):
                return False
            if compare_char(reg[0], word[0]) and len(word) == 1:
                if reg.endswith("$") and not compare_char(reg[-2], word[0]):
                    return False
                else:
                    return True
            elif compare_char(reg[0], word[0]) and compare_char(reg[0], word[1]):
                return compare_word(reg+"|"+word[1:], meta=meta_ch)
            elif len(reg) <= 2:
                if meta_ch == "^":
                    return True
                else:
                    return False
            else:
                return compare_word(reg[2]+"|"+word[1:])

        
 
        elif compare_char(reg[0], word[0]):
            if kwargs:
                meta_ch = kwargs['meta']
            else: 
                meta_ch=None
            return compare_word(reg[1:]+"|"+word[1:], meta=meta_ch)
        else:
            return False if kwargs else compare_word(reg+"|"+word[1:]) 


print(compare_word('\.$|end.'))  # True



