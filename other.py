# ex 1

def compare_start(regex, text):
#    print("comparing_start:", regex, text)
    # regexp empty or EOL reached
    if not regex or (regex == "$" and not text):
        return True

    if regex[0] == "\\":
        regex = regex[1:]
        escape = True
    else:
        escape = False

    if text:
        # symbol matched and no wildcard following
        if (regex[:1] == text[:1] or not escape and regex[:1] == '.') and (not regex[1:2] or regex[1:2] not in '?*+'):
            return compare_start(regex[1:], text[1:])

        # symbol matched and *+ wildcards following
        if regex[:1] == text[:1] and regex[1:2] in '*+':
            # shifting text until no match
            while text and regex[0] == text[:1]:
                text = text[1:]
            return compare_start(regex[2:], text)
        #  . wildcard with *+ wildcards following
        if not escape and regex[:1] == '.' and regex[1:2] in '*+' and regex[2:3] != text[:1]:
            while text and regex[2:3] != text[1:2]:
                text = text[1:]
            return compare_start(regex[2:], text[1:])

        # symbol matched and ? wildcard following
        if (regex[:1] == text[:1] or not escape and regex[:1] == '.') and regex[1:2] in '?':
            return compare_start(regex[2:], text[1:])

        # symbol not matched and ?* wildcards following
        if regex[1:2] in ['?', '*']:
            return compare_start(regex[2:], text)

    return False


def compare(regex, text):
    # ^ case
    if regex[:1] == "^":
        return compare_start(regex[1:], text)
    # general case
    while text or not regex:
#        print("comparing:", regex, text)
        if compare_start(regex, text):
            return True
        else:
            text = text[1:]
    return False


print(compare(*input().split('|')))


# ex 2

def match(regexp, input_):
    if not len(regexp):
        return True
    if not len(input_) and not len(regexp):
        return False
    if not len(input_) and regexp[-1] == '$':
        return True
    if len(regexp) > 1 and regexp[0] == f'\\':
        return match(regexp[1:], input_)
    if len(regexp) > 1 and regexp[1] in ['?', '+', '*']:
        if regexp[1] in ['*', '+'] and not len(input_):
            return True
        if regexp[1] in ['?', '*'] and not regexp[0] == input_[0]:
            return match(regexp[2:], input_)
        elif regexp[1] in ['?', '+'] and regexp[0] == input_[0] and regexp[0] != input_[1]:
            return match(regexp[2:], input_[1:])
        elif regexp[1] in ['*', '+'] and regexp[0] in [input_[0], '.']:
            if len(regexp) > 2 and regexp[0] == '.' and regexp[2] == input_[0]:
                return match(regexp[2:], input_)
            return match(regexp, input_[1:])
    if regexp[0] in [input_[0], '.']:
        return match(regexp[1:], input_[1:])
    return False


def define_input(regexp, input_):
    if len(input_) >= len(regexp.lstrip('^').rstrip('$')) or len(input_) > 0:
        if y := match(regexp.lstrip('^'), input_):
            return y
        elif not (regexp.endswith('$') and regexp.startswith('^')) and not regexp.startswith('^'):
            return define_input(regexp, input_[1:])
        return y
    return False


regex, chars = input().split('|')
print(define_input(regex, chars))
