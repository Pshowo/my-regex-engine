def my_regex(word):
    # 1.
    if word.strip() == "|":
        return True
    
    # 2.
    elif "|" in word:
        reg, word = word.split("|")

        if (len(reg) == 0 and len(word) != 0) or (len(reg) == 0 and len(word) == 0):
            return True

        elif len(reg) > 0 and len(word) == 0:
            return False
        
        elif len(reg) > 0 and len(word) > 0:
            if reg == word:
                return True
            elif reg == ".":
                return True
            else:
                return False
    # 3.
    else:
        return False

