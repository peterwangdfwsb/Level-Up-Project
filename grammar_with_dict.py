import en_core_web_sm
import spacy
import re

def grammar_opt(sentence):
    '''grammar detection for input sentence
     1. spacy for POS
     2. regex to find the matching index in the sentence
     3. match index between POS part and input sentence part'''

    
    # remove abbreviation
    sentence=sentence.replace("'re"," are")
    sentence=sentence.replace("n't"," not")
    sentence=sentence.replace("'s"," is")

    # POS
    en_nlp = en_core_web_sm.load()
    concatPos = ''
    doc = en_nlp(sentence)
    for word in doc:
        concatPos += word.tag_ + " "

    doc = concatPos
  
    repeat = []
    result = []
    detect_object = []
    result_detect = []
    
    # Define Level
    level = {'JJ CC JJ':'A1',"JJR CC JJR":'B2', 'JJ IN':'B1'}
    level_grammar = []

    # parse sentence structure
    expression_list = [r"JJ CC JJ",r"JJR CC JJR",r"JJ IN"]
    for i in expression_list:
        expression = i
        for match in re.finditer(expression, doc):
            start, end = match.span()
            repeat.append(match.span())
            level_grammar.append(level[expression])
    

    for j in repeat:
        repeat_index = [i for i in range(len(concatPos[:j[0]].split()) \
                                         , len(concatPos[:j[0]].split()) + len(concatPos[j[0]:j[1]].split()))]
        result.append(repeat_index)
       
    
    
    # add space in original sentence since
    # index in POS and setence.split() is different
    punctuation = "!@#$%^&*()_+<>?:.,;"
    parse_sentence = sentence
    for a in parse_sentence:
        if a in punctuation:
            parse_sentence = parse_sentence.replace(a, ' ' + a)

    # show detected part
    for list_1 in result:
      for index in list_1:
        detect_object.append(parse_sentence.split()[index])
      result_detect.append(' '.join(detect_object))
      detect_object = []

    level_detection = {}
    for i in range(len(result_detect)):
      if level_grammar[i] in level_detection:
        level_detection[level_grammar[i]].append(result_detect[i])
      else:
        level_detection[level_grammar[i]] = [result_detect[i]]

    return level_detection
