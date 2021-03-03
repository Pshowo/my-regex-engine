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

def compare_word(word):
    
    reg, word = word.split("|")
    mem = None
    
    if len(reg) == 0 and len(word) == 0:
        return True
    elif len(reg) == 0 and len(word) > 1:
        return True
    elif len(reg) > 1 and len(word) == 0:
        return False
    elif len(reg) <= 1 and len(word) <= 1:
        return my_regex(reg+"|"+word)

    elif reg.startswith("^"):
        return compare_word(reg[1:]+"|"+word[:len(reg[1:])])

    elif len(reg) > 1 and reg[1].startswith("?"):
        n=0
        if reg[0] == word[0] or "." == word[0]:
            for _ in word[0:]:
                if reg[0] == _ or "." ==_:
                    n+=1
            if n>1:
                return False
            else:
                return compare_word(reg[2:]+"|"+word[1:])   
        else:
            return compare_word(reg[2:]+"|"+word)

    elif len(reg) > 1 and reg[1].startswith("*"):
        n=0
        if reg[0] == word[0]:
            for _ in word[0:]:
                if reg[0] == _:
                    n+=1
            else:
                return compare_word(reg[2:]+"|"+word[n:])   
        else:
            return compare_word(reg[2:]+"|"+word)

            
        # return compare_word(reg[1:]+"|"+word)
    
    elif len(reg) > 1 and reg[1].startswith("+"):
        n=0
        if reg[0] == word[0] or reg[0] == ".":
            for _ in word[0:]:
                if reg[0] == _ or reg[0] == ".":
                    n+=1
            else:
                return compare_word(reg[2:]+"|"+word[n:])   
        else:
            return False
    
    elif not my_regex(reg[0]+"|"+word[0]):

        return compare_word(reg+"|"+word[1:])
    elif reg.endswith("$"):
        return compare_word(reg[:-1]+"|"+word[-len(reg[1:]):])
    else:
        return compare_word(reg[1:]+"|"+word[1:])        


print(compare_word('^no+pe$|noooooooope'))


