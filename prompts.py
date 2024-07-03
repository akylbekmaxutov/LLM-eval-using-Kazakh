def math_english_instructions(row):
    prompt = f'''You have the Math Question in Kazakh language with 4 choices
    Question: {row['question']}
    Choices are:
    a) {row['a']}
    b) {row['b']}
    c) {row['c']}
    d) {row['d']}
    Solve the question and give the letter showing the correct answer. Give only the letter without any explanation and symbols.'''
    return prompt

def math_kazakh_instructions(row):
    prompt = f'''Келесі сұрақты оқып, берілген төрт варианттардың қайсысы дұрыс екендігін таңда.
    Сұрақ: {row['question']}
    Варианттар:
    a) {row['a']}
    b) {row['b']}
    c) {row['c']}
    d) {row['d']}
    тек дұрыс жауапты көрсететін әріпті ғана бер. Ештеңені түсіндірме, артық текст, таңба керек емес.
    '''
    return prompt

def spelling_english_instructions(row):
    prompt = f'''You are given a sentence in Kazakh. The sentence includes some spelling mistakes.
    Sentence: {row['Sentence with Mistake']}
    Do not modify the sentence; find the mistakes and fix them.
    Give the correct sentence only without any explanation.'''
    return prompt

def spelling_kazakh_instructions(row):
    prompt = f'''Саған қазақша сөйлем беріледі. Сөйлемде бірнеше синтаксистік қателері бар.
    Сөйлем: {row['Sentence with Mistake']}
    Сөйлемді өзгертпей, тек қателерді тауып, оларды дұрыста.
    Жауап ретінде тек дұрыс сөйлемді бер. Ештеңені түсіндірме.'''
    return prompt

def belebele_english_instructions(row):
    prompt = f'''You are given a text, question and 4 choices in Kazakh.
    Text: {row['flores_passage']}
    Question: {row['question']}
    Choices:
    1: {row['mc_answer1']}
    2: {row['mc_answer2']}
    3: {row['mc_answer3']}
    4: {row['mc_answer4']}
    Read the text, and by answering the question choose which of the options is correct.
    Give only the integer indicating the correct choice without any explanation.'''
    return prompt

def belebele_kazakh_instructions(row):
    prompt = f'''Саған қазақ тіліндегі мәтін, сұрақ және 4 вариант беріледі.
    Мәтін: {row['flores_passage']}
    Сұрақ: {row['question']}
    Варианттар:
    1: {row['mc_answer1']}
    2: {row['mc_answer2']}
    3: {row['mc_answer3']}
    4: {row['mc_answer4']}
    Мәтінді оқып және сұраққа жауап бере отырып, берілген варианттардың қайсысы дұрыс екенін таңда.
    Жауап ретінде тек санды ғана бер. Ештеңені түсіндірме. Артық сөздермен таңбалар керек емес.'''
    return prompt

def copa_english_instructions(row):
    prompt = f'''You are given case and options.
    Case: {row['p_contents_kz']}
    Options:
    1) {row['a1_contents_kz']}
    2) {row['a2_contents_kz']}
    Which option (1 or 2) is the {row['asks-for_eng']} of the case.
    Give only integer without any explanation or extra symbols.'''
    return prompt

def copa_kazakh_instructions(row):
    prompt = f'''Саған жағдай мен опциялар беріледі.
    Жағдай: {row['p_contents_kz']}
    Опциялар:
    1) {row['a1_contents_kz']}
    2) {row['a2_contents_kz']}
    Қай опция (1 немесе 2) берілген жағдайдың {row['asks-for_kz']}.
    Жауап ретінде тек санды ғана бер. Ештеңені түсіндірме.'''
    return prompt

def flores_english_instructions(row):
    prompt = f'''You are a translator. Translate the given Kazakh sentence into English, Russian, and Turkish.
    Kazakh sentence: {row['Kazakh']}
    Give the response in the JSON format with three keys: English, Russian, Turkish, where
    English: english translation,
    Russian: russian translation,
    Turkish: turkish translation.
    '''
    return prompt

def flores_kazakh_instructions(row):
    prompt = f'''Сіз аудармашысыз. Берілген қазақша сөйлемді ағылшын, орыс, түрік тілдеріне аударыңыз.
    Қазақша сөйлем: {row['Kazakh']}
    Жауап JSON форматында болу керек. Кілттер:
    English: ағылшынша аударым,
    Russian: орысша аударым,
    Turkish: түрікше аударым.
    '''
    return prompt

def kazqad_english_instructions(row):
    prompt = f'''You will be given a text in Kazakh language and question related to this text.
    Read the text first and answer to the question.
    Text: {row['context']}
    Questions: {row['question']}
    Give the exact answer. Do not explain your choice.
    '''
    return prompt

def kazqad_kazakh_instructions(row):
    prompt = f'''Сізге мәтін және сол мәтінге сай сұрақ беріледі.
    Мәтінді оқып, сұраққа жауап беріңіз.
    Мәтін: {row['context']}
    Сұрақ: {row['question']}
    Нақты жауап беріңіз. Шешіміңізді түсіндіріп қажет емес.
    '''
    return prompt

def kazqad_english_instructions_closed(row):
    prompt = f'''answer to the question.
    Question: {row['question']}
    Give the exact answer. Do not explain your choice.
    '''
    return prompt