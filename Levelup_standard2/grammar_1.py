import spacy
import re


def grammar(sentence):
    sentence = sentence.replace("'re", " are")
    sentence = sentence.replace("n't", " not")
    sentence = sentence.replace("'s", " is")
    grammar_dictionary = {}
    en_nlp = spacy.load("en_core_web_sm")
    repeat = []
    result = []
    detect_object = []
    result_detect = []
    concatPos = ''
    doc = en_nlp(sentence)

    # POS
    for word in doc:
        concatPos += word.tag_ + " "

    doc = concatPos

    # parse sentence structure
    expression_list = [r"IN NN"]
    for i in expression_list:
        expression = i
        for match in re.finditer(expression, doc):
            start, end = match.span()
            repeat.append(match.span())

    for j in repeat:
        repeat_index = [i for i in range(len(concatPos[:j[0]].split()) \
                                         , len(concatPos[:j[0]].split()) + len(concatPos[j[0]:j[1]].split()))]
        result.append(repeat_index)

    # Add space in original sentence since
    # index in POS and setence.split() is different
    punctuation = "!@#$%^&*()_+<>?:.,;"
    parse_sentence = sentence
    for a in parse_sentence:
        if a in punctuation:
            parse_sentence = parse_sentence.replace(a, ' ' + a)

    # show detected part
    try:
        for list_1 in result:
            for index in list_1:
                detect_object.append(parse_sentence.split()[index])
            result_detect.append(' '.join(detect_object))
            detect_object = []

    except:
        result_detect = ["None"]

    try:
        detect_target_word = [l for l in result_detect if l.split()[0] == 'In']

    except:
        detect_target_word = ["None"]

    if len(detect_target_word) > 0:
        result = [j for j in detect_target_word]
        grammar_dictionary['C2_43'] = result
    else:
        result = None

    # A1_1
    repeat = []
    result = []
    detect_object = []
    result_detect = []

    # parse sentence structure
    expression_list = [r"JJ CC JJ"]
    for i in expression_list:
        expression = i
        for match in re.finditer(expression, doc):
            start, end = match.span()
            repeat.append(match.span())

    for j in repeat:
        repeat_index = [i for i in range(len(concatPos[:j[0]].split()) \
                                         , len(concatPos[:j[0]].split()) + len(concatPos[j[0]:j[1]].split()))]
        result.append(repeat_index)

    # Add space in original sentence since
    # index in POS and setence.split() is different
    punctuation = "!@#$%^&*()_+<>?:.,;"
    parse_sentence = sentence
    for a in parse_sentence:
        if a in punctuation:
            parse_sentence = parse_sentence.replace(a, ' ' + a)

    # show detected part
    try:
        for list_1 in result:
            for index in list_1:
                detect_object.append(parse_sentence.split()[index])
            result_detect.append(' '.join(detect_object))
            detect_object = []

    except:
        result_detect = ["None"]

    try:
        detect_target_word = [l for l in result_detect if l.split()[1] == 'and']

    except:
        detect_target_word = ["None"]

    if len(detect_target_word) > 0:
        result = [j for j in detect_target_word]
        grammar_dictionary['A1_1'] = result
    else:
        result = None

    # A2_2
    repeat = []
    result = []
    detect_object = []
    result_detect = []

    # parse sentence structure
    expression_list = [r"JJ CC JJ"]
    for i in expression_list:
        expression = i
        for match in re.finditer(expression, doc):
            start, end = match.span()
            repeat.append(match.span())

    for j in repeat:
        repeat_index = [i for i in range(len(concatPos[:j[0]].split()) \
                                         , len(concatPos[:j[0]].split()) + len(concatPos[j[0]:j[1]].split()))]
        result.append(repeat_index)

    # Add space in original sentence since
    # index in POS and setence.split() is different
    punctuation = "!@#$%^&*()_+<>?:.,;"
    parse_sentence = sentence
    for a in parse_sentence:
        if a in punctuation:
            parse_sentence = parse_sentence.replace(a, ' ' + a)

    # show detected part
    try:
        for list_1 in result:
            for index in list_1:
                detect_object.append(parse_sentence.split()[index])
            result_detect.append(' '.join(detect_object))
            detect_object = []

    except:
        result_detect = ["None"]

    try:
        detect_target_word = [l for l in result_detect if l.split()[1] == 'but']

    except:
        detect_target_word = ["None"]

    if len(detect_target_word) > 0:
        result = [j for j in detect_target_word]
        grammar_dictionary['B1_3'] = result
    else:
        result = None

    # B1_3
    repeat = []
    result = []
    detect_object = []
    result_detect = []

    # parse sentence structure
    expression_list = [r"JJ , JJ NN"]
    for i in expression_list:
        expression = i
        for match in re.finditer(expression, doc):
            start, end = match.span()
            repeat.append(match.span())

    for j in repeat:
        repeat_index = [i for i in range(len(concatPos[:j[0]].split()) \
                                         , len(concatPos[:j[0]].split()) + len(concatPos[j[0]:j[1]].split()))]
        result.append(repeat_index)

    # Add space in original sentence since
    # index in POS and setence.split() is different
    punctuation = "!@#$%^&*()_+<>?:.,;"
    parse_sentence = sentence
    for a in parse_sentence:
        if a in punctuation:
            parse_sentence = parse_sentence.replace(a, ' ' + a)

    # show detected part
    try:
        for list_1 in result:
            for index in list_1:
                detect_object.append(parse_sentence.split()[index])
            result_detect.append(' '.join(detect_object))
            detect_object = []

    except:
        result_detect = ["None"]

    try:
        detect_target_word = [l for l in result_detect]

    except:
        detect_target_word = ["None"]

    if len(detect_target_word) > 0:
        result = [j for j in detect_target_word]
        grammar_dictionary['B1_3'] = result
    else:
        result = None

    # B1_4
    repeat = []
    result = []
    detect_object = []
    result_detect = []

    # parse sentence structure
    expression_list = [r"JJR CC JJR"]
    for i in expression_list:
        expression = i
        for match in re.finditer(expression, doc):
            start, end = match.span()
            repeat.append(match.span())

    for j in repeat:
        repeat_index = [i for i in range(len(concatPos[:j[0]].split()) \
                                         , len(concatPos[:j[0]].split()) + len(concatPos[j[0]:j[1]].split()))]
        result.append(repeat_index)

    # Add space in original sentence since
    # index in POS and setence.split() is different
    punctuation = "!@#$%^&*()_+<>?:.,;"
    parse_sentence = sentence
    for a in parse_sentence:
        if a in punctuation:
            parse_sentence = parse_sentence.replace(a, ' ' + a)

    # show detected part
    try:
        for list_1 in result:
            for index in list_1:
                detect_object.append(parse_sentence.split()[index])
            result_detect.append(' '.join(detect_object))
            detect_object = []

    except:
        result_detect = ["None"]

    try:
        detect_target_word = [l for l in result_detect]

    except:
        detect_target_word = ["None"]

    if len(detect_target_word) > 0:
        result = [j for j in detect_target_word]
        grammar_dictionary['B1_4'] = result
    else:
        result = None

    # B1_6
    repeat = []
    result = []
    detect_object = []
    result_detect = []

    # parse sentence structure
    expression_list = [r"JJR CC JJR"]
    for i in expression_list:
        expression = i
        for match in re.finditer(expression, doc):
            start, end = match.span()
            repeat.append(match.span())

    for j in repeat:
        repeat_index = [i for i in range(len(concatPos[:j[0]].split()) \
                                         , len(concatPos[:j[0]].split()) + len(concatPos[j[0]:j[1]].split()))]
        result.append(repeat_index)

    # Add space in original sentence since
    # index in POS and setence.split() is different
    punctuation = "!@#$%^&*()_+<>?:.,;"
    parse_sentence = sentence
    for a in parse_sentence:
        if a in punctuation:
            parse_sentence = parse_sentence.replace(a, ' ' + a)

    # show detected part
    try:
        for list_1 in result:
            for index in list_1:
                detect_object.append(parse_sentence.split()[index])
            result_detect.append(' '.join(detect_object))
            detect_object = []

    except:
        result_detect = ["None"]

    try:
        detect_target_word = [l for l in result_detect if l.split()[0] == l.split()[2]]

    except:
        detect_target_word = ["None"]

    if len(detect_target_word) > 0:
        result = [j for j in detect_target_word]
        grammar_dictionary['B1_6'] = result
    else:
        result = None

    # A2_13
    repeat = []
    result = []
    detect_object = []
    result_detect = []

    # parse sentence structure
    expression_list = [r"JJR"]
    for i in expression_list:
        expression = i
        for match in re.finditer(expression, doc):
            start, end = match.span()
            repeat.append(match.span())

    for j in repeat:
        repeat_index = [i for i in range(len(concatPos[:j[0]].split()) \
                                         , len(concatPos[:j[0]].split()) + len(concatPos[j[0]:j[1]].split()))]
        result.append(repeat_index)

    # Add space in original sentence since
    # index in POS and setence.split() is different
    punctuation = "!@#$%^&*()_+<>?:.,;"
    parse_sentence = sentence
    for a in parse_sentence:
        if a in punctuation:
            parse_sentence = parse_sentence.replace(a, ' ' + a)

    # show detected part
    try:
        for list_1 in result:
            for index in list_1:
                detect_object.append(parse_sentence.split()[index])
            result_detect.append(' '.join(detect_object))
            detect_object = []

    except:
        result_detect = ["None"]

    try:
        detect_target_word = [l for l in result_detect]

    except:
        detect_target_word = ["None"]

    if len(detect_target_word) > 0:
        result = []
        for j in detect_target_word:
            if j not in result:
                result.append(j)
        # result = [j for j in detect_target_word if j not in result]
        grammar_dictionary['A2_13'] = result
    else:
        result = None

    # A2_15
    repeat = []
    result = []
    detect_object = []
    result_detect = []

    # parse sentence structure
    expression_list = [r"JJR NN"]
    for i in expression_list:
        expression = i
        for match in re.finditer(expression, doc):
            start, end = match.span()
            repeat.append(match.span())

    for j in repeat:
        repeat_index = [i for i in range(len(concatPos[:j[0]].split()) \
                                         , len(concatPos[:j[0]].split()) + len(concatPos[j[0]:j[1]].split()))]
        result.append(repeat_index)

    # Add space in original sentence since
    # index in POS and setence.split() is different
    punctuation = "!@#$%^&*()_+<>?:.,;"
    parse_sentence = sentence
    for a in parse_sentence:
        if a in punctuation:
            parse_sentence = parse_sentence.replace(a, ' ' + a)

    # show detected part
    try:
        for list_1 in result:
            for index in list_1:
                detect_object.append(parse_sentence.split()[index])
            result_detect.append(' '.join(detect_object))
            detect_object = []

    except:
        result_detect = ["None"]

    try:
        detect_target_word = [l for l in result_detect]

    except:
        detect_target_word = ["None"]

    if len(detect_target_word) > 0:
        result = [j for j in detect_target_word]
        grammar_dictionary['A2_15'] = result
    else:
        result = None
    # A2_20
    repeat = []
    result = []
    detect_object = []
    result_detect = []

    # parse sentence structure
    expression_list = [r"RBR JJ"]
    for i in expression_list:
        expression = i
        for match in re.finditer(expression, doc):
            start, end = match.span()
            repeat.append(match.span())

    for j in repeat:
        repeat_index = [i for i in range(len(concatPos[:j[0]].split()) \
                                         , len(concatPos[:j[0]].split()) + len(concatPos[j[0]:j[1]].split()))]
        result.append(repeat_index)

    # Add space in original sentence since
    # index in POS and setence.split() is different
    punctuation = "!@#$%^&*()_+<>?:.,;"
    parse_sentence = sentence
    for a in parse_sentence:
        if a in punctuation:
            parse_sentence = parse_sentence.replace(a, ' ' + a)

    # show detected part
    try:
        for list_1 in result:
            for index in list_1:
                detect_object.append(parse_sentence.split()[index])
            result_detect.append(' '.join(detect_object))
            detect_object = []

    except:
        result_detect = ["None"]

    try:
        detect_target_word = [l for l in result_detect]

    except:
        detect_target_word = ["None"]

    if len(detect_target_word) > 0:
        result = [j for j in detect_target_word]
        grammar_dictionary['A2_20'] = result
    else:
        result = None

    # A2_21
    repeat = []
    result = []
    detect_object = []
    result_detect = []

    # parse sentence structure
    expression_list = [r"JJR IN", r"RBR JJ IN"]
    for i in expression_list:
        expression = i
        for match in re.finditer(expression, doc):
            start, end = match.span()
            repeat.append(match.span())

    for j in repeat:
        repeat_index = [i for i in range(len(concatPos[:j[0]].split()) \
                                         , len(concatPos[:j[0]].split()) + len(concatPos[j[0]:j[1]].split()))]
        result.append(repeat_index)

    # Add space in original sentence since
    # index in POS and setence.split() is different
    punctuation = "!@#$%^&*()_+<>?:.,;"
    parse_sentence = sentence
    for a in parse_sentence:
        if a in punctuation:
            parse_sentence = parse_sentence.replace(a, ' ' + a)

    # show detected part
    try:
        for list_1 in result:
            for index in list_1:
                detect_object.append(parse_sentence.split()[index])
            result_detect.append(' '.join(detect_object))
            detect_object = []

    except:
        result_detect = ["None"]

    try:
        detect_target_word = [l for l in result_detect]

    except:
        detect_target_word = ["None"]

    if len(detect_target_word) > 0:
        result = [j for j in detect_target_word]
        grammar_dictionary['A2_21'] = result
    else:
        result = None

    # B1_22
    repeat = []
    result = []
    detect_object = []
    result_detect = []

    # parse sentence structure
    expression_list = [r"RB JJR"]
    for i in expression_list:
        expression = i
        for match in re.finditer(expression, doc):
            start, end = match.span()
            repeat.append(match.span())

    for j in repeat:
        repeat_index = [i for i in range(len(concatPos[:j[0]].split()) \
                                         , len(concatPos[:j[0]].split()) + len(concatPos[j[0]:j[1]].split()))]
        result.append(repeat_index)

    # Add space in original sentence since
    # index in POS and setence.split() is different
    punctuation = "!@#$%^&*()_+<>?:.,;"
    parse_sentence = sentence
    for a in parse_sentence:
        if a in punctuation:
            parse_sentence = parse_sentence.replace(a, ' ' + a)

    # show detected part
    try:
        for list_1 in result:
            for index in list_1:
                detect_object.append(parse_sentence.split()[index])
            result_detect.append(' '.join(detect_object))
            detect_object = []

    except:
        result_detect = ["None"]

    try:
        detect_target_word = [l for l in result_detect if l.split()[0] == 'much']

    except:
        detect_target_word = ["None"]

    if len(detect_target_word) > 0:
        result = [j for j in detect_target_word]
        grammar_dictionary['B1_22'] = result
    else:
        result = None

    # B1_23
    repeat = []
    result = []
    detect_object = []
    result_detect = []

    # parse sentence structure
    expression_list = [r"DT JJ NN JJR", r"DT NN JJR"]
    for i in expression_list:
        expression = i
        for match in re.finditer(expression, doc):
            start, end = match.span()
            repeat.append(match.span())

    for j in repeat:
        repeat_index = [i for i in range(len(concatPos[:j[0]].split()) \
                                         , len(concatPos[:j[0]].split()) + len(concatPos[j[0]:j[1]].split()))]
        result.append(repeat_index)

    # Add space in original sentence since
    # index in POS and setence.split() is different
    punctuation = "!@#$%^&*()_+<>?:.,;"
    parse_sentence = sentence
    for a in parse_sentence:
        if a in punctuation:
            parse_sentence = parse_sentence.replace(a, ' ' + a)

    # show detected part
    try:
        for list_1 in result:
            for index in list_1:
                detect_object.append(parse_sentence.split()[index])
            result_detect.append(' '.join(detect_object))
            detect_object = []

    except:
        result_detect = ["None"]

    target_word = ['little', 'bit']
    try:
        detect_target_word = [l for l in result_detect if l.split()[1] in target_word]

    except:
        detect_target_word = ["None"]

    if len(detect_target_word) > 0:
        result = [j for j in detect_target_word]
        grammar_dictionary['B1_23'] = result
    else:
        result = None

    # B1_24
    repeat = []
    result = []
    detect_object = []
    result_detect = []

    # parse sentence structure
    expression_list = [r"VBG JJR CC JJR", r"VBP RBR CC RBR"]
    for i in expression_list:
        expression = i
        for match in re.finditer(expression, doc):
            start, end = match.span()
            repeat.append(match.span())

    for j in repeat:
        repeat_index = [i for i in range(len(concatPos[:j[0]].split()) \
                                         , len(concatPos[:j[0]].split()) + len(concatPos[j[0]:j[1]].split()))]
        result.append(repeat_index)

    # Add space in original sentence since
    # index in POS and setence.split() is different
    punctuation = "!@#$%^&*()_+<>?:.,;"
    parse_sentence = sentence
    for a in parse_sentence:
        if a in punctuation:
            parse_sentence = parse_sentence.replace(a, ' ' + a)

    # show detected part
    try:
        for list_1 in result:
            for index in list_1:
                detect_object.append(parse_sentence.split()[index])
            result_detect.append(' '.join(detect_object))
            detect_object = []

    except:
        result_detect = ["None"]

    target_word = ['become', 'get', 'getting']
    try:
        detect_target_word = [l for l in result_detect if l.split()[0] in target_word]

    except:
        detect_target_word = ["None"]

    if len(detect_target_word) > 0:
        result = [j for j in detect_target_word]
        grammar_dictionary['B1_24'] = result
    else:
        result = None

    # B1_25
    repeat = []
    result = []
    detect_object = []
    result_detect = []

    # parse sentence structure
    expression_list = [r"VB RB JJR", r"VBD RB JJR"]
    for i in expression_list:
        expression = i
        for match in re.finditer(expression, doc):
            start, end = match.span()
            repeat.append(match.span())

    for j in repeat:
        repeat_index = [i for i in range(len(concatPos[:j[0]].split()) \
                                         , len(concatPos[:j[0]].split()) + len(concatPos[j[0]:j[1]].split()))]
        result.append(repeat_index)

    # Add space in original sentence since
    # index in POS and setence.split() is different
    punctuation = "!@#$%^&*()_+<>?:.,;"
    parse_sentence = sentence
    for a in parse_sentence:
        if a in punctuation:
            parse_sentence = parse_sentence.replace(a, ' ' + a)

    # show detected part
    try:
        for list_1 in result:
            for index in list_1:
                detect_object.append(parse_sentence.split()[index])
            result_detect.append(' '.join(detect_object))
            detect_object = []

    except:
        result_detect = ["None"]

    target_word = ['be', 'got']
    try:
        detect_target_word = [l for l in result_detect if l.split()[0] in target_word]

    except:
        detect_target_word = ["None"]

    if len(detect_target_word) > 0:
        result = [j for j in detect_target_word]
        grammar_dictionary['B1_25'] = result
    else:
        result = None

    # B2_26
    repeat = []
    result = []
    detect_object = []
    result_detect = []

    # parse sentence structure
    expression_list = [r"VB DT NN JJR", r"VBZ DT NN JJR"]
    for i in expression_list:
        expression = i
        for match in re.finditer(expression, doc):
            start, end = match.span()
            repeat.append(match.span())

    for j in repeat:
        repeat_index = [i for i in range(len(concatPos[:j[0]].split()) \
                                         , len(concatPos[:j[0]].split()) + len(concatPos[j[0]:j[1]].split()))]
        result.append(repeat_index)

    # Add space in original sentence since
    # index in POS and setence.split() is different
    punctuation = "!@#$%^&*()_+<>?:.,;"
    parse_sentence = sentence
    for a in parse_sentence:
        if a in punctuation:
            parse_sentence = parse_sentence.replace(a, ' ' + a)

    # show detected part
    try:
        for list_1 in result:
            for index in list_1:
                detect_object.append(parse_sentence.split()[index])
            result_detect.append(' '.join(detect_object))
            detect_object = []

    except:
        result_detect = ["None"]

    target_word = ['lot']
    try:
        detect_target_word = [l for l in result_detect if l.split()[2] in target_word]

    except:
        detect_target_word = ["None"]

    if len(detect_target_word) > 0:
        result = [j for j in detect_target_word]
        grammar_dictionary['B2_26'] = result
    else:
        result = None

    # B2_27
    repeat = []
    result = []
    detect_object = []
    result_detect = []

    # parse sentence structure
    expression_list = [r"RB JJR NN"]
    for i in expression_list:
        expression = i
        for match in re.finditer(expression, doc):
            start, end = match.span()
            repeat.append(match.span())

    for j in repeat:
        repeat_index = [i for i in range(len(concatPos[:j[0]].split()) \
                                         , len(concatPos[:j[0]].split()) + len(concatPos[j[0]:j[1]].split()))]
        result.append(repeat_index)

    # Add space in original sentence since
    # index in POS and setence.split() is different
    punctuation = "!@#$%^&*()_+<>?:.,;"
    parse_sentence = sentence
    for a in parse_sentence:
        if a in punctuation:
            parse_sentence = parse_sentence.replace(a, ' ' + a)

    # show detected part
    try:
        for list_1 in result:
            for index in list_1:
                detect_object.append(parse_sentence.split()[index])
            result_detect.append(' '.join(detect_object))
            detect_object = []

    except:
        result_detect = ["None"]

    target_word = ['much']
    try:
        detect_target_word = [l for l in result_detect if l.split()[0] in target_word]

    except:
        detect_target_word = ["None"]

    if len(detect_target_word) > 0:
        result = [j for j in detect_target_word]
        grammar_dictionary['B2_27'] = result
    else:
        result = None

    # B2_28
    repeat = []
    result = []
    detect_object = []
    result_detect = []

    # parse sentence structure
    expression_list = [r"RB JJR"]
    for i in expression_list:
        expression = i
        for match in re.finditer(expression, doc):
            start, end = match.span()
            repeat.append(match.span())

    for j in repeat:
        repeat_index = [i for i in range(len(concatPos[:j[0]].split()) \
                                         , len(concatPos[:j[0]].split()) + len(concatPos[j[0]:j[1]].split()))]
        result.append(repeat_index)

    # Add space in original sentence since
    # index in POS and setence.split() is different
    punctuation = "!@#$%^&*()_+<>?:.,;"
    parse_sentence = sentence
    for a in parse_sentence:
        if a in punctuation:
            parse_sentence = parse_sentence.replace(a, ' ' + a)

    # show detected part
    try:
        for list_1 in result:
            for index in list_1:
                detect_object.append(parse_sentence.split()[index])
            result_detect.append(' '.join(detect_object))
            detect_object = []

    except:
        result_detect = ["None"]

    try:
        detect_target_word = [l for l in result_detect if l.split()[0] == 'slightly']

    except:
        detect_target_word = ["None"]

    if len(detect_target_word) > 0:
        result = [j for j in detect_target_word]
        grammar_dictionary['B2_28'] = result
    else:
        result = None

    # C2_29
    repeat = []
    result = []
    detect_object = []
    result_detect = []

    # parse sentence structure
    expression_list = [r"RB DT JJR", r"RB JJR"]
    for i in expression_list:
        expression = i
        for match in re.finditer(expression, doc):
            start, end = match.span()
            repeat.append(match.span())

    for j in repeat:
        repeat_index = [i for i in range(len(concatPos[:j[0]].split()) \
                                         , len(concatPos[:j[0]].split()) + len(concatPos[j[0]:j[1]].split()))]
        result.append(repeat_index)

    # Add space in original sentence since
    # index in POS and setence.split() is different
    punctuation = "!@#$%^&*()_+<>?:.,;"
    parse_sentence = sentence
    for a in parse_sentence:
        if a in punctuation:
            parse_sentence = parse_sentence.replace(a, ' ' + a)

    # show detected part
    try:
        for list_1 in result:
            for index in list_1:
                detect_object.append(parse_sentence.split()[index])
            result_detect.append(' '.join(detect_object))
            detect_object = []

    except:
        result_detect = ["None"]

    target_word = ['no', 'not']
    try:
        detect_target_word = [l for l in result_detect if l.split()[0] in target_word]

    except:
        detect_target_word = ["None"]

    if len(detect_target_word) > 0:
        result = [j for j in detect_target_word]
        grammar_dictionary['C2_29'] = result
    else:
        result = None

    # C2_30
    repeat = []
    result = []
    detect_object = []
    result_detect = []

    # parse sentence structure
    expression_list = [r"RB RB RB JJR"]
    for i in expression_list:
        expression = i
        for match in re.finditer(expression, doc):
            start, end = match.span()
            repeat.append(match.span())

    for j in repeat:
        repeat_index = [i for i in range(len(concatPos[:j[0]].split()) \
                                         , len(concatPos[:j[0]].split()) + len(concatPos[j[0]:j[1]].split()))]
        result.append(repeat_index)

    # Add space in original sentence since
    # index in POS and setence.split() is different
    punctuation = "!@#$%^&*()_+<>?:.,;"
    parse_sentence = sentence
    for a in parse_sentence:
        if a in punctuation:
            parse_sentence = parse_sentence.replace(a, ' ' + a)

    # show detected part
    try:
        for list_1 in result:
            for index in list_1:
                detect_object.append(parse_sentence.split()[index])
            result_detect.append(' '.join(detect_object))
            detect_object = []

    except:
        result_detect = ["None"]

    target_word = ['not']
    try:
        detect_target_word = [l for l in result_detect if l.split()[0] in target_word]

    except:
        detect_target_word = ["None"]

    if len(detect_target_word) > 0:
        result = [j for j in detect_target_word]
        grammar_dictionary['C2_30'] = result
    else:
        result = None

    # A1_31
    repeat = []
    result = []
    detect_object = []
    result_detect = []

    # parse sentence structure
    expression_list = [r"RB JJ"]
    for i in expression_list:
        expression = i
        for match in re.finditer(expression, doc):
            start, end = match.span()
            repeat.append(match.span())

    for j in repeat:
        repeat_index = [i for i in range(len(concatPos[:j[0]].split()) \
                                         , len(concatPos[:j[0]].split()) + len(concatPos[j[0]:j[1]].split()))]
        result.append(repeat_index)

    # Add space in original sentence since
    # index in POS and setence.split() is different
    punctuation = "!@#$%^&*()_+<>?:.,;"
    parse_sentence = sentence
    for a in parse_sentence:
        if a in punctuation:
            parse_sentence = parse_sentence.replace(a, ' ' + a)

    # show detected part
    try:
        for list_1 in result:
            for index in list_1:
                detect_object.append(parse_sentence.split()[index])
            result_detect.append(' '.join(detect_object))
            detect_object = []

    except:
        result_detect = ["None"]

    target_word = ['very']
    try:
        detect_target_word = [l for l in result_detect if l.split()[0] in target_word]

    except:
        detect_target_word = ["None"]

    if len(detect_target_word) > 0:
        result = [j for j in detect_target_word]
        grammar_dictionary['A1_31'] = result
    else:
        result = None

    # A2_32
    repeat = []
    result = []
    detect_object = []
    result_detect = []

    # parse sentence structure
    expression_list = [r"RB JJ"]
    for i in expression_list:
        expression = i
        for match in re.finditer(expression, doc):
            start, end = match.span()
            repeat.append(match.span())

    for j in repeat:
        repeat_index = [i for i in range(len(concatPos[:j[0]].split()) \
                                         , len(concatPos[:j[0]].split()) + len(concatPos[j[0]:j[1]].split()))]
        result.append(repeat_index)

    # Add space in original sentence since
    # index in POS and setence.split() is different
    punctuation = "!@#$%^&*()_+<>?:.,;"
    parse_sentence = sentence
    for a in parse_sentence:
        if a in punctuation:
            parse_sentence = parse_sentence.replace(a, ' ' + a)

    # show detected part
    try:
        for list_1 in result:
            for index in list_1:
                detect_object.append(parse_sentence.split()[index])
            result_detect.append(' '.join(detect_object))
            detect_object = []

    except:
        result_detect = ["None"]

    target_word = ['really', 'so', 'quite']
    try:
        detect_target_word = [l for l in result_detect if l.split()[0] in target_word]

    except:
        detect_target_word = ["None"]

    if len(detect_target_word) > 0:
        result = [j for j in detect_target_word]
        grammar_dictionary['A2_32'] = result
    else:
        result = None

    # A2_33
    repeat = []
    result = []
    detect_object = []
    result_detect = []

    # parse sentence structure
    expression_list = [r"JJ IN"]
    for i in expression_list:
        expression = i
        for match in re.finditer(expression, doc):
            start, end = match.span()
            repeat.append(match.span())

    for j in repeat:
        repeat_index = [i for i in range(len(concatPos[:j[0]].split()) \
                                         , len(concatPos[:j[0]].split()) + len(concatPos[j[0]:j[1]].split()))]
        result.append(repeat_index)

    # Add space in original sentence since
    # index in POS and setence.split() is different
    punctuation = "!@#$%^&*()_+<>?:.,;"
    parse_sentence = sentence
    for a in parse_sentence:
        if a in punctuation:
            parse_sentence = parse_sentence.replace(a, ' ' + a)

    # show detected part
    try:
        for list_1 in result:
            for index in list_1:
                detect_object.append(parse_sentence.split()[index])
            result_detect.append(' '.join(detect_object))
            detect_object = []

    except:
        result_detect = ["None"]

    target_word = ['for', 'of']
    try:
        detect_target_word = [l for l in result_detect if l.split()[1] in target_word]

    except:
        detect_target_word = ["None"]

    if len(detect_target_word) > 0:
        result = [j for j in detect_target_word]
        grammar_dictionary['A2_33'] = result
    else:
        result = None

    # A2_34
    repeat = []
    result = []
    detect_object = []
    result_detect = []

    # parse sentence structure
    expression_list = [r"RB JJ"]
    for i in expression_list:
        expression = i
        for match in re.finditer(expression, doc):
            start, end = match.span()
            repeat.append(match.span())

    for j in repeat:
        repeat_index = [i for i in range(len(concatPos[:j[0]].split()) \
                                         , len(concatPos[:j[0]].split()) + len(concatPos[j[0]:j[1]].split()))]
        result.append(repeat_index)

    # Add space in original sentence since
    # index in POS and setence.split() is different
    punctuation = "!@#$%^&*()_+<>?:.,;"
    parse_sentence = sentence
    for a in parse_sentence:
        if a in punctuation:
            parse_sentence = parse_sentence.replace(a, ' ' + a)

    # show detected part
    try:
        for list_1 in result:
            for index in list_1:
                detect_object.append(parse_sentence.split()[index])
            result_detect.append(' '.join(detect_object))
            detect_object = []

    except:
        result_detect = ["None"]

    target_word = ['too']
    try:
        detect_target_word = [l for l in result_detect if l.split()[0] in target_word]

    except:
        detect_target_word = ["None"]

    if len(detect_target_word) > 0:
        result = [j for j in detect_target_word]
        grammar_dictionary['A2_34'] = result
    else:
        result = None

    # A2_35
    repeat = []
    result = []
    detect_object = []
    result_detect = []

    # parse sentence structure
    expression_list = [r"RB JJ IN"]
    for i in expression_list:
        expression = i
        for match in re.finditer(expression, doc):
            start, end = match.span()
            repeat.append(match.span())

    for j in repeat:
        repeat_index = [i for i in range(len(concatPos[:j[0]].split()) \
                                         , len(concatPos[:j[0]].split()) + len(concatPos[j[0]:j[1]].split()))]
        result.append(repeat_index)

    # Add space in original sentence since
    # index in POS and setence.split() is different
    punctuation = "!@#$%^&*()_+<>?:.,;"
    parse_sentence = sentence
    for a in parse_sentence:
        if a in punctuation:
            parse_sentence = parse_sentence.replace(a, ' ' + a)

    # show detected part
    try:
        for list_1 in result:
            for index in list_1:
                detect_object.append(parse_sentence.split()[index])
            result_detect.append(' '.join(detect_object))
            detect_object = []

    except:
        result_detect = ["None"]

    target_word = ['too']
    try:
        detect_target_word = [l for l in result_detect if l.split()[0] in target_word]

    except:
        detect_target_word = ["None"]

    if len(detect_target_word) > 0:
        result = [j for j in detect_target_word]
        grammar_dictionary['A2_35'] = result
    else:
        result = None

    # B1_36
    repeat = []
    result = []
    detect_object = []
    result_detect = []

    # parse sentence structure
    expression_list = [r"RB JJ NN"]
    for i in expression_list:
        expression = i
        for match in re.finditer(expression, doc):
            start, end = match.span()
            repeat.append(match.span())

    for j in repeat:
        repeat_index = [i for i in range(len(concatPos[:j[0]].split()) \
                                         , len(concatPos[:j[0]].split()) + len(concatPos[j[0]:j[1]].split()))]
        result.append(repeat_index)

    # Add space in original sentence since
    # index in POS and setence.split() is different
    punctuation = "!@#$%^&*()_+<>?:.,;"
    parse_sentence = sentence
    for a in parse_sentence:
        if a in punctuation:
            parse_sentence = parse_sentence.replace(a, ' ' + a)

    # show detected part
    try:
        for list_1 in result:
            for index in list_1:
                detect_object.append(parse_sentence.split()[index])
            result_detect.append(' '.join(detect_object))
            detect_object = []

    except:
        result_detect = ["None"]

    try:
        detect_target_word = [l for l in result_detect]

    except:
        detect_target_word = ["None"]

    if len(detect_target_word) > 0:
        result = [j for j in detect_target_word]
        grammar_dictionary['B1_36'] = result
    else:
        result = None

    # B1_37
    repeat = []
    result = []
    detect_object = []
    result_detect = []

    # parse sentence structure
    expression_list = [r"JJ RB"]
    for i in expression_list:
        expression = i
        for match in re.finditer(expression, doc):
            start, end = match.span()
            repeat.append(match.span())

    for j in repeat:
        repeat_index = [i for i in range(len(concatPos[:j[0]].split()) \
                                         , len(concatPos[:j[0]].split()) + len(concatPos[j[0]:j[1]].split()))]
        result.append(repeat_index)

    # Add space in original sentence since
    # index in POS and setence.split() is different
    punctuation = "!@#$%^&*()_+<>?:.,;"
    parse_sentence = sentence
    for a in parse_sentence:
        if a in punctuation:
            parse_sentence = parse_sentence.replace(a, ' ' + a)

    # show detected part
    try:
        for list_1 in result:
            for index in list_1:
                detect_object.append(parse_sentence.split()[index])
            result_detect.append(' '.join(detect_object))
            detect_object = []

    except:
        result_detect = ["None"]

    target_word = ['enough']
    try:
        detect_target_word = [l for l in result_detect if l.split()[1] in target_word]

    except:
        detect_target_word = ["None"]

    if len(detect_target_word) > 0:
        result = [j for j in detect_target_word]
        grammar_dictionary['B1_37'] = result
    else:
        result = None

    # B1_38
    repeat = []
    result = []
    detect_object = []
    result_detect = []

    # parse sentence structure
    expression_list = [r"PDT DT JJ"]
    for i in expression_list:
        expression = i
        for match in re.finditer(expression, doc):
            start, end = match.span()
            repeat.append(match.span())

    for j in repeat:
        repeat_index = [i for i in range(len(concatPos[:j[0]].split()) \
                                         , len(concatPos[:j[0]].split()) + len(concatPos[j[0]:j[1]].split()))]
        result.append(repeat_index)

    # Add space in original sentence since
    # index in POS and setence.split() is different
    punctuation = "!@#$%^&*()_+<>?:.,;"
    parse_sentence = sentence
    for a in parse_sentence:
        if a in punctuation:
            parse_sentence = parse_sentence.replace(a, ' ' + a)

    # show detected part
    try:
        for list_1 in result:
            for index in list_1:
                detect_object.append(parse_sentence.split()[index])
            result_detect.append(' '.join(detect_object))
            detect_object = []

    except:
        result_detect = ["None"]

    target_word = ['quite']
    try:
        detect_target_word = [l for l in result_detect if l.split()[0] in target_word]

    except:
        detect_target_word = ["None"]

    if len(detect_target_word) > 0:
        result = [j for j in detect_target_word]
        grammar_dictionary['B1_38'] = result
    else:
        result = None

    # B1_39
    repeat = []
    result = []
    detect_object = []
    result_detect = []

    # parse sentence structure
    expression_list = [r"RB JJ TO"]
    for i in expression_list:
        expression = i
        for match in re.finditer(expression, doc):
            start, end = match.span()
            repeat.append(match.span())

    for j in repeat:
        repeat_index = [i for i in range(len(concatPos[:j[0]].split()) \
                                         , len(concatPos[:j[0]].split()) + len(concatPos[j[0]:j[1]].split()))]
        result.append(repeat_index)

    # Add space in original sentence since
    # index in POS and setence.split() is different
    punctuation = "!@#$%^&*()_+<>?:.,;"
    parse_sentence = sentence
    for a in parse_sentence:
        if a in punctuation:
            parse_sentence = parse_sentence.replace(a, ' ' + a)

    # show detected part
    try:
        for list_1 in result:
            for index in list_1:
                detect_object.append(parse_sentence.split()[index])
            result_detect.append(' '.join(detect_object))
            detect_object = []

    except:
        result_detect = ["None"]

    target_word = ['too']
    try:
        detect_target_word = [l for l in result_detect if l.split()[0] in target_word]

    except:
        detect_target_word = ["None"]

    if len(detect_target_word) > 0:
        result = [j for j in detect_target_word]
        grammar_dictionary['B1_39'] = result
    else:
        result = None

    # B2_40
    repeat = []
    result = []
    detect_object = []
    result_detect = []

    # parse sentence structure
    expression_list = [r"JJ RB TO"]
    for i in expression_list:
        expression = i
        for match in re.finditer(expression, doc):
            start, end = match.span()
            repeat.append(match.span())

    for j in repeat:
        repeat_index = [i for i in range(len(concatPos[:j[0]].split()) \
                                         , len(concatPos[:j[0]].split()) + len(concatPos[j[0]:j[1]].split()))]
        result.append(repeat_index)

    # Add space in original sentence since
    # index in POS and setence.split() is different
    punctuation = "!@#$%^&*()_+<>?:.,;"
    parse_sentence = sentence
    for a in parse_sentence:
        if a in punctuation:
            parse_sentence = parse_sentence.replace(a, ' ' + a)

    # show detected part
    try:
        for list_1 in result:
            for index in list_1:
                detect_object.append(parse_sentence.split()[index])
            result_detect.append(' '.join(detect_object))
            detect_object = []

    except:
        result_detect = ["None"]

    target_word = ['enough']
    try:
        detect_target_word = [l for l in result_detect if l.split()[1] in target_word]

    except:
        detect_target_word = ["None"]

    if len(detect_target_word) > 0:
        result = [j for j in detect_target_word]
        grammar_dictionary['B2_40'] = result
    else:
        result = None
    # B2_41
    repeat = []
    result = []
    detect_object = []
    result_detect = []

    # parse sentence structure
    expression_list = [r"RB DT JJ"]
    for i in expression_list:
        expression = i
        for match in re.finditer(expression, doc):
            start, end = match.span()
            repeat.append(match.span())

    for j in repeat:
        repeat_index = [i for i in range(len(concatPos[:j[0]].split()) \
                                         , len(concatPos[:j[0]].split()) + len(concatPos[j[0]:j[1]].split()))]
        result.append(repeat_index)

    # Add space in original sentence since
    # index in POS and setence.split() is different
    punctuation = "!@#$%^&*()_+<>?:.,;"
    parse_sentence = sentence
    for a in parse_sentence:
        if a in punctuation:
            parse_sentence = parse_sentence.replace(a, ' ' + a)

    # show detected part
    try:
        for list_1 in result:
            for index in list_1:
                detect_object.append(parse_sentence.split()[index])
            result_detect.append(' '.join(detect_object))
            detect_object = []

    except:
        result_detect = ["None"]

    target_word = ['rather']
    try:
        detect_target_word = [l for l in result_detect if l.split()[0] in target_word]

    except:
        detect_target_word = ["None"]

    if len(detect_target_word) > 0:
        result = [j for j in detect_target_word]
        grammar_dictionary['B2_41'] = result
    else:
        result = None

    # C1_42
    repeat = []
    result = []
    detect_object = []
    result_detect = []

    # parse sentence structure
    expression_list = [r"RB JJ"]
    for i in expression_list:
        expression = i
        for match in re.finditer(expression, doc):
            start, end = match.span()
            repeat.append(match.span())

    for j in repeat:
        repeat_index = [i for i in range(len(concatPos[:j[0]].split()) \
                                         , len(concatPos[:j[0]].split()) + len(concatPos[j[0]:j[1]].split()))]
        result.append(repeat_index)

    # Add space in original sentence since
    # index in POS and setence.split() is different
    punctuation = "!@#$%^&*()_+<>?:.,;"
    parse_sentence = sentence
    for a in parse_sentence:
        if a in punctuation:
            parse_sentence = parse_sentence.replace(a, ' ' + a)

    # show detected part
    try:
        for list_1 in result:
            for index in list_1:
                detect_object.append(parse_sentence.split()[index])
            result_detect.append(' '.join(detect_object))
            detect_object = []

    except:
        result_detect = ["None"]

    target_word = ['absolutely', 'extremely', 'incredibly', 'totally']
    try:
        detect_target_word = [l for l in result_detect if l.split()[0] in target_word]

    except:
        detect_target_word = ["None"]

    if len(detect_target_word) > 0:
        result = [j for j in detect_target_word]
        grammar_dictionary['C1_42'] = result
    else:
        result = None

    # A1_44
    repeat = []
    result = []
    detect_object = []
    result_detect = []

    # parse sentence structure
    expression_list = [r"JJ NN"]
    for i in expression_list:
        expression = i
        for match in re.finditer(expression, doc):
            start, end = match.span()
            repeat.append(match.span())

    for j in repeat:
        repeat_index = [i for i in range(len(concatPos[:j[0]].split()) \
                                         , len(concatPos[:j[0]].split()) + len(concatPos[j[0]:j[1]].split()))]
        result.append(repeat_index)

    # Add space in original sentence since
    # index in POS and setence.split() is different
    punctuation = "!@#$%^&*()_+<>?:.,;"
    parse_sentence = sentence
    for a in parse_sentence:
        if a in punctuation:
            parse_sentence = parse_sentence.replace(a, ' ' + a)

    # show detected part
    try:
        for list_1 in result:
            for index in list_1:
                detect_object.append(parse_sentence.split()[index])
            result_detect.append(' '.join(detect_object))
            detect_object = []

    except:
        result_detect = ["None"]

    try:
        detect_target_word = [l for l in result_detect]

    except:
        detect_target_word = ["None"]

    if len(detect_target_word) > 0:
        result = [j for j in detect_target_word]
        grammar_dictionary['A1_44'] = result
    else:
        result = None

    # A1_45
    repeat = []
    result = []
    detect_object = []
    result_detect = []

    # parse sentence structure
    expression_list = [r"VBZ JJ"]
    for i in expression_list:
        expression = i
        for match in re.finditer(expression, doc):
            start, end = match.span()
            repeat.append(match.span())

    for j in repeat:
        repeat_index = [i for i in range(len(concatPos[:j[0]].split()) \
                                         , len(concatPos[:j[0]].split()) + len(concatPos[j[0]:j[1]].split()))]
        result.append(repeat_index)

    # Add space in original sentence since
    # index in POS and setence.split() is different
    punctuation = "!@#$%^&*()_+<>?:.,;"
    parse_sentence = sentence
    for a in parse_sentence:
        if a in punctuation:
            parse_sentence = parse_sentence.replace(a, ' ' + a)

    # show detected part
    try:
        for list_1 in result:
            for index in list_1:
                detect_object.append(parse_sentence.split()[index])
            result_detect.append(' '.join(detect_object))
            detect_object = []

    except:
        result_detect = ["None"]

    try:
        detect_target_word = [l for l in result_detect]

    except:
        detect_target_word = ["None"]

    if len(detect_target_word) > 0:
        result = [j for j in detect_target_word]
        grammar_dictionary['A1_45'] = result
    else:
        result = None

    # A2_46
    repeat = []
    result = []
    detect_object = []
    result_detect = []

    # parse sentence structure
    expression_list = [r"JJ NN"]
    for i in expression_list:
        expression = i
        for match in re.finditer(expression, doc):
            start, end = match.span()
            repeat.append(match.span())

    for j in repeat:
        repeat_index = [i for i in range(len(concatPos[:j[0]].split()) \
                                         , len(concatPos[:j[0]].split()) + len(concatPos[j[0]:j[1]].split()))]
        result.append(repeat_index)

    # Add space in original sentence since
    # index in POS and setence.split() is different
    punctuation = "!@#$%^&*()_+<>?:.,;"
    parse_sentence = sentence
    for a in parse_sentence:
        if a in punctuation:
            parse_sentence = parse_sentence.replace(a, ' ' + a)

    # show detected part
    try:
        for list_1 in result:
            for index in list_1:
                detect_object.append(parse_sentence.split()[index])
            result_detect.append(' '.join(detect_object))
            detect_object = []

    except:
        result_detect = ["None"]

    try:
        target_word = ['main', 'only']
        detect_target_word = [l for l in result_detect if l.split()[0] in target_word]

    except:
        detect_target_word = ["None"]

    if len(detect_target_word) > 0:
        result = [j for j in detect_target_word]
        grammar_dictionary['A2_46'] = result
    else:
        result = None

    # B1_49
    repeat = []
    result = []
    detect_object = []
    result_detect = []

    # parse sentence structure
    expression_list = [r"JJ"]
    for i in expression_list:
        expression = i
        for match in re.finditer(expression, doc):
            start, end = match.span()
            repeat.append(match.span())

    for j in repeat:
        repeat_index = [i for i in range(len(concatPos[:j[0]].split()) \
                                         , len(concatPos[:j[0]].split()) + len(concatPos[j[0]:j[1]].split()))]
        result.append(repeat_index)

    # Add space in original sentence since
    # index in POS and setence.split() is different
    punctuation = "!@#$%^&*()_+<>?:.,;"
    parse_sentence = sentence
    for a in parse_sentence:
        if a in punctuation:
            parse_sentence = parse_sentence.replace(a, ' ' + a)

    # show detected part
    try:
        for list_1 in result:
            for index in list_1:
                detect_object.append(parse_sentence.split()[index])
            result_detect.append(' '.join(detect_object))
            detect_object = []

    except:
        result_detect = ["None"]

    try:
        detect_target_word = [l for l in result_detect if l[0] == 'a']

    except:
        detect_target_word = ["None"]

    if len(detect_target_word) > 0:
        result = [j for j in detect_target_word]
        grammar_dictionary['B1_49'] = result
    else:
        result = None

    # B1_51
    repeat = []
    result = []
    detect_object = []
    result_detect = []

    # parse sentence structure
    expression_list = [r"VBZ PRP JJ", r"VB JJ NNS JJ", r"VB PRP JJ"]
    for i in expression_list:
        expression = i
        for match in re.finditer(expression, doc):
            start, end = match.span()
            repeat.append(match.span())

    for j in repeat:
        repeat_index = [i for i in range(len(concatPos[:j[0]].split()) \
                                         , len(concatPos[:j[0]].split()) + len(concatPos[j[0]:j[1]].split()))]
        result.append(repeat_index)

    # Add space in original sentence since
    # index in POS and setence.split() is different
    punctuation = "!@#$%^&*()_+<>?:.,;"
    parse_sentence = sentence
    for a in parse_sentence:
        if a in punctuation:
            parse_sentence = parse_sentence.replace(a, ' ' + a)

    # show detected part
    try:
        for list_1 in result:
            for index in list_1:
                detect_object.append(parse_sentence.split()[index])
            result_detect.append(' '.join(detect_object))
            detect_object = []

    except:
        result_detect = ["None"]

    try:
        target_word = ['makes', 'make', 'made', 'making']
        detect_target_word = [l for l in result_detect if l.split()[0] in target_word]

    except:
        detect_target_word = ["None"]

    if len(detect_target_word) > 0:
        result = [j for j in detect_target_word]
        grammar_dictionary['B1_51'] = result
    else:
        result = None

    # B1_52
    repeat = []
    result = []
    detect_object = []
    result_detect = []

    # parse sentence structure
    expression_list = [r"NN JJ"]
    for i in expression_list:
        expression = i
        for match in re.finditer(expression, doc):
            start, end = match.span()
            repeat.append(match.span())

    for j in repeat:
        repeat_index = [i for i in range(len(concatPos[:j[0]].split()) \
                                         , len(concatPos[:j[0]].split()) + len(concatPos[j[0]:j[1]].split()))]
        result.append(repeat_index)

    # Add space in original sentence since
    # index in POS and setence.split() is different
    punctuation = "!@#$%^&*()_+<>?:.,;"
    parse_sentence = sentence
    for a in parse_sentence:
        if a in punctuation:
            parse_sentence = parse_sentence.replace(a, ' ' + a)

    # show detected part
    try:
        for list_1 in result:
            for index in list_1:
                detect_object.append(parse_sentence.split()[index])
            result_detect.append(' '.join(detect_object))
            detect_object = []

    except:
        result_detect = ["None"]

    try:
        target_word = ['nothing', 'somewhere', 'nowhere', 'something']
        detect_target_word = [l for l in result_detect if l.split()[0] in target_word]

    except:
        detect_target_word = ["None"]

    if len(detect_target_word) > 0:
        result = [j for j in detect_target_word]
        grammar_dictionary['B1_52'] = result
    else:
        result = None

    # B2_53
    repeat = []
    result = []
    detect_object = []
    result_detect = []

    # parse sentence structure
    expression_list = [r"JJ NN"]
    for i in expression_list:
        expression = i
        for match in re.finditer(expression, doc):
            start, end = match.span()
            repeat.append(match.span())

    for j in repeat:
        repeat_index = [i for i in range(len(concatPos[:j[0]].split()) \
                                         , len(concatPos[:j[0]].split()) + len(concatPos[j[0]:j[1]].split()))]
        result.append(repeat_index)

    # Add space in original sentence since
    # index in POS and setence.split() is different
    punctuation = "!@#$%^&*()_+<>?:.,;"
    parse_sentence = sentence
    for a in parse_sentence:
        if a in punctuation:
            parse_sentence = parse_sentence.replace(a, ' ' + a)

    # show detected part
    try:
        for list_1 in result:
            for index in list_1:
                detect_object.append(parse_sentence.split()[index])
            result_detect.append(' '.join(detect_object))
            detect_object = []

    except:
        result_detect = ["None"]

    try:
        target_word = ['real', 'absolute', 'complete']
        detect_target_word = [l for l in result_detect if l.split()[0] in target_word]

    except:
        detect_target_word = ["None"]

    if len(detect_target_word) > 0:
        result = [j for j in detect_target_word]
        grammar_dictionary['B1_53'] = result
    else:
        result = None

    # B2_54
    repeat = []
    result = []
    detect_object = []
    result_detect = []

    # parse sentence structure
    expression_list = [r"JJ NN"]
    for i in expression_list:
        expression = i
        for match in re.finditer(expression, doc):
            start, end = match.span()
            repeat.append(match.span())

    for j in repeat:
        repeat_index = [i for i in range(len(concatPos[:j[0]].split()) \
                                         , len(concatPos[:j[0]].split()) + len(concatPos[j[0]:j[1]].split()))]
        result.append(repeat_index)

    # Add space in original sentence since
    # index in POS and setence.split() is different
    punctuation = "!@#$%^&*()_+<>?:.,;"
    parse_sentence = sentence
    for a in parse_sentence:
        if a in punctuation:
            parse_sentence = parse_sentence.replace(a, ' ' + a)

    # show detected part
    try:
        for list_1 in result:
            for index in list_1:
                detect_object.append(parse_sentence.split()[index])
            result_detect.append(' '.join(detect_object))
            detect_object = []

    except:
        result_detect = ["None"]

    try:
        target_word = ['present', 'future', 'former']
        detect_target_word = [l for l in result_detect if l.split()[0] in target_word]

    except:
        detect_target_word = ["None"]

    if len(detect_target_word) > 0:
        result = [j for j in detect_target_word]
        grammar_dictionary['B1_54'] = result
    else:
        result = None

    # C1_55
    repeat = []
    result = []
    detect_object = []
    result_detect = []

    # parse sentence structure
    expression_list = [r"VBN"]
    for i in expression_list:
        expression = i
        for match in re.finditer(expression, doc):
            start, end = match.span()
            repeat.append(match.span())

    for j in repeat:
        repeat_index = [i for i in range(len(concatPos[:j[0]].split()) \
                                         , len(concatPos[:j[0]].split()) + len(concatPos[j[0]:j[1]].split()))]
        result.append(repeat_index)

    # Add space in original sentence since
    # index in POS and setence.split() is different
    punctuation = "!@#$%^&*()_+<>?:.,;"
    parse_sentence = sentence
    for a in parse_sentence:
        if a in punctuation:
            parse_sentence = parse_sentence.replace(a, ' ' + a)

    # show detected part
    try:
        for list_1 in result:
            for index in list_1:
                detect_object.append(parse_sentence.split()[index])
            result_detect.append(' '.join(detect_object))
            detect_object = []

    except:
        result_detect = ["None"]

    try:
        detect_target_word = [l for l in result_detect if l[-2] + l[-1] == 'ed']

    except:
        detect_target_word = ["None"]

    if len(detect_target_word) > 0:
        result = [j for j in detect_target_word]
        grammar_dictionary['C1_55'] = result
    else:
        result = None

    # A1_57
    repeat = []
    result = []
    detect_object = []
    result_detect = []

    # parse sentence structure
    expression_list = [r"JJS"]
    for i in expression_list:
        expression = i
        for match in re.finditer(expression, doc):
            start, end = match.span()
            repeat.append(match.span())

    for j in repeat:
        repeat_index = [i for i in range(len(concatPos[:j[0]].split()) \
                                         , len(concatPos[:j[0]].split()) + len(concatPos[j[0]:j[1]].split()))]
        result.append(repeat_index)

    # Add space in original sentence since
    # index in POS and setence.split() is different
    punctuation = "!@#$%^&*()_+<>?:.,;"
    parse_sentence = sentence
    for a in parse_sentence:
        if a in punctuation:
            parse_sentence = parse_sentence.replace(a, ' ' + a)

    # show detected part
    try:
        for list_1 in result:
            for index in list_1:
                detect_object.append(parse_sentence.split()[index])
            result_detect.append(' '.join(detect_object))
            detect_object = []

    except:
        result_detect = ["None"]

    try:
        detect_target_word = [l for l in result_detect]

    except:
        detect_target_word = ["None"]

    if len(detect_target_word) > 0:
        result = [j for j in detect_target_word]
        grammar_dictionary['A1_57'] = result
    else:
        result = None

    # A2_58
    repeat = []
    result = []
    detect_object = []
    result_detect = []

    # parse sentence structure
    expression_list = [r"DT JJS NN"]
    for i in expression_list:
        expression = i
        for match in re.finditer(expression, doc):
            start, end = match.span()
            repeat.append(match.span())

    for j in repeat:
        repeat_index = [i for i in range(len(concatPos[:j[0]].split()) \
                                         , len(concatPos[:j[0]].split()) + len(concatPos[j[0]:j[1]].split()))]
        result.append(repeat_index)

    # Add space in original sentence since
    # index in POS and setence.split() is different
    punctuation = "!@#$%^&*()_+<>?:.,;"
    parse_sentence = sentence
    for a in parse_sentence:
        if a in punctuation:
            parse_sentence = parse_sentence.replace(a, ' ' + a)

    # show detected part
    try:
        for list_1 in result:
            for index in list_1:
                detect_object.append(parse_sentence.split()[index])
            result_detect.append(' '.join(detect_object))
            detect_object = []

    except:
        result_detect = ["None"]

    try:
        detect_target_word = [l for l in result_detect]

    except:
        detect_target_word = ["None"]

    if len(detect_target_word) > 0:
        result = [j for j in detect_target_word]
        grammar_dictionary['A2_58'] = result
    else:
        result = None

    # A2_59
    repeat = []
    result = []
    detect_object = []
    result_detect = []

    # parse sentence structure
    expression_list = [r"DT JJS NNS IN DT NN"]
    for i in expression_list:
        expression = i
        for match in re.finditer(expression, doc):
            start, end = match.span()
            repeat.append(match.span())

    for j in repeat:
        repeat_index = [i for i in range(len(concatPos[:j[0]].split()) \
                                         , len(concatPos[:j[0]].split()) + len(concatPos[j[0]:j[1]].split()))]
        result.append(repeat_index)

    # Add space in original sentence since
    # index in POS and setence.split() is different
    punctuation = "!@#$%^&*()_+<>?:.,;"
    parse_sentence = sentence
    for a in parse_sentence:
        if a in punctuation:
            parse_sentence = parse_sentence.replace(a, ' ' + a)

    # show detected part
    try:
        for list_1 in result:
            for index in list_1:
                detect_object.append(parse_sentence.split()[index])
            result_detect.append(' '.join(detect_object))
            detect_object = []

    except:
        result_detect = ["None"]

    try:
        detect_target_word = [l for l in result_detect]

    except:
        detect_target_word = ["None"]

    if len(detect_target_word) > 0:
        result = [j for j in detect_target_word]
        grammar_dictionary['A2_59'] = result
    else:
        result = None

    # A2_63
    repeat = []
    result = []
    detect_object = []
    result_detect = []

    # parse sentence structure
    expression_list = [r"JJS"]
    for i in expression_list:
        expression = i
        for match in re.finditer(expression, doc):
            start, end = match.span()
            repeat.append(match.span())

    for j in repeat:
        repeat_index = [i for i in range(len(concatPos[:j[0]].split()) \
                                         , len(concatPos[:j[0]].split()) + len(concatPos[j[0]:j[1]].split()))]
        result.append(repeat_index)

    # Add space in original sentence since
    # index in POS and setence.split() is different
    punctuation = "!@#$%^&*()_+<>?:.,;"
    parse_sentence = sentence
    for a in parse_sentence:
        if a in punctuation:
            parse_sentence = parse_sentence.replace(a, ' ' + a)

    # show detected part
    try:
        for list_1 in result:
            for index in list_1:
                detect_object.append(parse_sentence.split()[index])
            result_detect.append(' '.join(detect_object))
            detect_object = []

    except:
        result_detect = ["None"]

    try:
        detect_target_word = [l for l in result_detect if l[-3] + l[-2] + l[-1] == 'est']

    except:
        detect_target_word = ["None"]

    if len(detect_target_word) > 0:
        result = [j for j in detect_target_word]
        grammar_dictionary['A2_63'] = result
    else:
        result = None

    # A2_64
    repeat = []
    result = []
    detect_object = []
    result_detect = []

    # parse sentence structure
    expression_list = [r"JJS"]
    for i in expression_list:
        expression = i
        for match in re.finditer(expression, doc):
            start, end = match.span()
            repeat.append(match.span())

    for j in repeat:
        repeat_index = [i for i in range(len(concatPos[:j[0]].split()) \
                                         , len(concatPos[:j[0]].split()) + len(concatPos[j[0]:j[1]].split()))]
        result.append(repeat_index)

    # Add space in original sentence since
    # index in POS and setence.split() is different
    punctuation = "!@#$%^&*()_+<>?:.,;"
    parse_sentence = sentence
    for a in parse_sentence:
        if a in punctuation:
            parse_sentence = parse_sentence.replace(a, ' ' + a)

    # show detected part
    try:
        for list_1 in result:
            for index in list_1:
                detect_object.append(parse_sentence.split()[index])
            result_detect.append(' '.join(detect_object))
            detect_object = []

    except:
        result_detect = ["None"]

    try:
        detect_target_word = [l for l in result_detect if l[-4] + l[-3] + l[-2] + l[-1] == 'iest']

    except:
        detect_target_word = ["None"]

    if len(detect_target_word) > 0:
        result = [j for j in detect_target_word]
        grammar_dictionary['A2_64'] = result
    else:
        result = None

    # A2_65: can not detect PRP
    repeat = []
    result = []
    detect_object = []
    result_detect = []

    # parse sentence structure
    expression_list = [r"PRP.JJS NN"]
    for i in expression_list:
        expression = i
        for match in re.finditer(expression, doc):
            start, end = match.span()
            repeat.append(match.span())

    for j in repeat:
        repeat_index = [i for i in range(len(concatPos[:j[0]].split()) \
                                         , len(concatPos[:j[0]].split()) + len(concatPos[j[0]:j[1]].split()))]
        result.append(repeat_index)

    # Add space in original sentence since
    # index in POS and setence.split() is different
    punctuation = "!@#$%^&*()_+<>?:.,;"
    parse_sentence = sentence
    for a in parse_sentence:
        if a in punctuation:
            parse_sentence = parse_sentence.replace(a, ' ' + a)

    # show detected part
    try:
        for list_1 in result:
            for index in list_1:
                detect_object.append(parse_sentence.split()[index])
            result_detect.append(' '.join(detect_object))
            detect_object = []

    except:
        result_detect = ["None"]

    try:
        detect_target_word = [l for l in result_detect]

    except:
        detect_target_word = ["None"]

    if len(detect_target_word) > 0:
        result = [j for j in detect_target_word]
        grammar_dictionary['A2_65'] = result
    else:
        result = None
    # A2_67
    repeat = []
    result = []
    detect_object = []
    result_detect = []

    # parse sentence structure
    expression_list = [r"DT JJS"]
    for i in expression_list:
        expression = i
        for match in re.finditer(expression, doc):
            start, end = match.span()
            repeat.append(match.span())

    for j in repeat:
        repeat_index = [i for i in range(len(concatPos[:j[0]].split()) \
                                         , len(concatPos[:j[0]].split()) + len(concatPos[j[0]:j[1]].split()))]
        result.append(repeat_index)

    # Add space in original sentence since
    # index in POS and setence.split() is different
    punctuation = "!@#$%^&*()_+<>?:.,;"
    parse_sentence = sentence
    for a in parse_sentence:
        if a in punctuation:
            parse_sentence = parse_sentence.replace(a, ' ' + a)

    # show detected part
    try:
        for list_1 in result:
            for index in list_1:
                detect_object.append(parse_sentence.split()[index])
            result_detect.append(' '.join(detect_object))
            detect_object = []

    except:
        result_detect = ["None"]

    try:
        detect_target_word = [l for l in result_detect]

    except:
        detect_target_word = ["None"]

    if len(detect_target_word) > 0:
        result = [j for j in detect_target_word]
        grammar_dictionary['A2_67'] = result
    else:
        result = None

    # B1_70
    repeat = []
    result = []
    detect_object = []
    result_detect = []

    # parse sentence structure
    expression_list = [r"DT JJS NN"]
    for i in expression_list:
        expression = i
        for match in re.finditer(expression, doc):
            start, end = match.span()
            repeat.append(match.span())

    for j in repeat:
        repeat_index = [i for i in range(len(concatPos[:j[0]].split()) \
                                         , len(concatPos[:j[0]].split()) + len(concatPos[j[0]:j[1]].split()))]
        result.append(repeat_index)

    # Add space in original sentence since
    # index in POS and setence.split() is different
    punctuation = "!@#$%^&*()_+<>?:.,;"
    parse_sentence = sentence
    for a in parse_sentence:
        if a in punctuation:
            parse_sentence = parse_sentence.replace(a, ' ' + a)

    # show detected part
    try:
        for list_1 in result:
            for index in list_1:
                detect_object.append(parse_sentence.split()[index])
            result_detect.append(' '.join(detect_object))
            detect_object = []

    except:
        result_detect = ["None"]

    try:
        detect_target_word = [l for l in result_detect if l.split()[0] + ' ' + l.split()[1] == 'the best']

    except:
        detect_target_word = ["None"]

    if len(detect_target_word) > 0:
        result = [j for j in detect_target_word]
        grammar_dictionary['B1_70'] = result
    else:
        result = None

    # B1_71
    repeat = []
    result = []
    detect_object = []
    result_detect = []

    # parse sentence structure
    expression_list = [r"CD IN DT JJS"]
    for i in expression_list:
        expression = i
        for match in re.finditer(expression, doc):
            start, end = match.span()
            repeat.append(match.span())

    for j in repeat:
        repeat_index = [i for i in range(len(concatPos[:j[0]].split()) \
                                         , len(concatPos[:j[0]].split()) + len(concatPos[j[0]:j[1]].split()))]
        result.append(repeat_index)

    # Add space in original sentence since
    # index in POS and setence.split() is different
    punctuation = "!@#$%^&*()_+<>?:.,;"
    parse_sentence = sentence
    for a in parse_sentence:
        if a in punctuation:
            parse_sentence = parse_sentence.replace(a, ' ' + a)

    # show detected part
    try:
        for list_1 in result:
            for index in list_1:
                detect_object.append(parse_sentence.split()[index])
            result_detect.append(' '.join(detect_object))
            detect_object = []

    except:
        result_detect = ["None"]

    try:
        detect_target_word = [l for l in result_detect if
                              l.split()[0] + ' ' + l.split()[1] + ' ' + l.split()[2] == 'one of the']

    except:
        detect_target_word = ["None"]

    if len(detect_target_word) > 0:
        result = [j for j in detect_target_word]
        grammar_dictionary['B1_71'] = result
    else:
        result = None

    # B1_72
    repeat = []
    result = []
    detect_object = []
    result_detect = []

    # parse sentence structure
    expression_list = [r"DT JJS NN TO"]
    for i in expression_list:
        expression = i
        for match in re.finditer(expression, doc):
            start, end = match.span()
            repeat.append(match.span())

    for j in repeat:
        repeat_index = [i for i in range(len(concatPos[:j[0]].split()) \
                                         , len(concatPos[:j[0]].split()) + len(concatPos[j[0]:j[1]].split()))]
        result.append(repeat_index)

    # Add space in original sentence since
    # index in POS and setence.split() is different
    punctuation = "!@#$%^&*()_+<>?:.,;"
    parse_sentence = sentence
    for a in parse_sentence:
        if a in punctuation:
            parse_sentence = parse_sentence.replace(a, ' ' + a)

    # show detected part
    try:
        for list_1 in result:
            for index in list_1:
                detect_object.append(parse_sentence.split()[index])
            result_detect.append(' '.join(detect_object))
            detect_object = []

    except:
        result_detect = ["None"]

    try:
        detect_target_word = [l for l in result_detect if
                              l.split()[0] + ' ' + l.split()[1] == 'the best' and l.split()[-1] == 'to']

    except:
        detect_target_word = ["None"]

    if len(detect_target_word) > 0:
        result = [j for j in detect_target_word]
        grammar_dictionary['B1_72'] = result
    else:
        result = None

    # B2_74
    repeat = []
    result = []
    detect_object = []
    result_detect = []

    # parse sentence structure
    expression_list = [r"IN RB DT RBS JJ"]
    for i in expression_list:
        expression = i
        for match in re.finditer(expression, doc):
            start, end = match.span()
            repeat.append(match.span())

    for j in repeat:
        repeat_index = [i for i in range(len(concatPos[:j[0]].split()) \
                                         , len(concatPos[:j[0]].split()) + len(concatPos[j[0]:j[1]].split()))]
        result.append(repeat_index)

    # Add space in original sentence since
    # index in POS and setence.split() is different
    punctuation = "!@#$%^&*()_+<>?:.,;"
    parse_sentence = sentence
    for a in parse_sentence:
        if a in punctuation:
            parse_sentence = parse_sentence.replace(a, ' ' + a)

    # show detected part
    try:
        for list_1 in result:
            for index in list_1:
                detect_object.append(parse_sentence.split()[index])
            result_detect.append(' '.join(detect_object))
            detect_object = []

    except:
        result_detect = ["None"]

    try:
        detect_target_word = [l for l in result_detect if l.split()[0] + ' ' + l.split()[1] == 'by far']

    except:
        detect_target_word = ["None"]

    if len(detect_target_word) > 0:
        result = [j for j in detect_target_word]
        grammar_dictionary['B2_74'] = result
    else:
        result = None

    # B2_76
    repeat = []
    result = []
    detect_object = []
    result_detect = []

    # parse sentence structure
    expression_list = [r"DT JJS NN TO"]
    for i in expression_list:
        expression = i
        for match in re.finditer(expression, doc):
            start, end = match.span()
            repeat.append(match.span())

    for j in repeat:
        repeat_index = [i for i in range(len(concatPos[:j[0]].split()) \
                                         , len(concatPos[:j[0]].split()) + len(concatPos[j[0]:j[1]].split()))]
        result.append(repeat_index)

    # Add space in original sentence since
    # index in POS and setence.split() is different
    punctuation = "!@#$%^&*()_+<>?:.,;"
    parse_sentence = sentence
    for a in parse_sentence:
        if a in punctuation:
            parse_sentence = parse_sentence.replace(a, ' ' + a)

    # show detected part
    try:
        for list_1 in result:
            for index in list_1:
                detect_object.append(parse_sentence.split()[index])
            result_detect.append(' '.join(detect_object))
            detect_object = []

    except:
        result_detect = ["None"]

    try:
        detect_target_word = [l for l in result_detect]

    except:
        detect_target_word = ["None"]

    if len(detect_target_word) > 0:
        result = [j for j in detect_target_word]
        grammar_dictionary['B2_76'] = result
    else:
        result = None

    # C1_78
    repeat = []
    result = []
    detect_object = []
    result_detect = []

    # parse sentence structure
    expression_list = [r"DT JJS NN JJ"]
    for i in expression_list:
        expression = i
        for match in re.finditer(expression, doc):
            start, end = match.span()
            repeat.append(match.span())

    for j in repeat:
        repeat_index = [i for i in range(len(concatPos[:j[0]].split()) \
                                         , len(concatPos[:j[0]].split()) + len(concatPos[j[0]:j[1]].split()))]
        result.append(repeat_index)

    # Add space in original sentence since
    # index in POS and setence.split() is different
    punctuation = "!@#$%^&*()_+<>?:.,;"
    parse_sentence = sentence
    for a in parse_sentence:
        if a in punctuation:
            parse_sentence = parse_sentence.replace(a, ' ' + a)

    # show detected part
    try:
        for list_1 in result:
            for index in list_1:
                detect_object.append(parse_sentence.split()[index])
            result_detect.append(' '.join(detect_object))
            detect_object = []

    except:
        result_detect = ["None"]

    try:
        list_1 = ['possible', 'or']
        detect_target_word = [l for l in result_detect if
                              l.split()[-1] in list_1 or l.split()[-2] + ' ' + l.split()[-1] == 'by far']

    except:
        detect_target_word = ["None"]

    if len(detect_target_word) > 0:
        result = [j for j in detect_target_word]
        grammar_dictionary['C1_78'] = result
    else:
        result = None

    # C1_79
    repeat = []
    result = []
    detect_object = []
    result_detect = []

    # parse sentence structure
    expression_list = [r"DT JJS NN"]
    for i in expression_list:
        expression = i
        for match in re.finditer(expression, doc):
            start, end = match.span()
            repeat.append(match.span())

    for j in repeat:
        repeat_index = [i for i in range(len(concatPos[:j[0]].split()) \
                                         , len(concatPos[:j[0]].split()) + len(concatPos[j[0]:j[1]].split()))]
        result.append(repeat_index)

    # Add space in original sentence since
    # index in POS and setence.split() is different
    punctuation = "!@#$%^&*()_+<>?:.,;"
    parse_sentence = sentence
    for a in parse_sentence:
        if a in punctuation:
            parse_sentence = parse_sentence.replace(a, ' ' + a)

    # show detected part
    try:
        for list_1 in result:
            for index in list_1:
                detect_object.append(parse_sentence.split()[index])
            result_detect.append(' '.join(detect_object))
            detect_object = []

    except:
        result_detect = ["None"]

    try:
        list_1 = ['possible', 'or']
        detect_target_word = [l for l in result_detect if
                              l.split()[0] + ' ' + l.split()[1] == 'the faintest' or l.split()[0] + ' ' + l.split()[
                                  1] == 'the slightest']

    except:
        detect_target_word = ["None"]

    if len(detect_target_word) > 0:
        result = [j for j in detect_target_word]
        grammar_dictionary['C1_79'] = result
    else:
        result = None

    return grammar_dictionary

