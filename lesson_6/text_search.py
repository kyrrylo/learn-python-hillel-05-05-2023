from time import time


text = """
Python — высокоуровневый язык программирования общего назначения, который относится к интерпретируемым языкам.
То есть написанный на Python код интерпретируется в момент обращения программой-интерпретатором без предварительной
компиляции.
Создатель Python — нидерландский инженер Гвидо ван Россум, известный энтузиаст разработки, который сейчас работает в
Microsoft. Язык программирования «пайтон» — сайд-проект ван Россума. Гвидо считал существующие языки сложными для
понимания и изучения, поэтому начал работать над собственным проектом. Ван Россум планировал сделать одновременно
простой и мощный язык, и так в 1991 году он представил Python."""

set_stop_words = {'который', 'к', 'то', 'на', 'в', 'без', 'для', 'и', 'он', 'так'}
list_stop_words = ['который', 'к', 'то', 'на', 'в', 'без', 'для', 'и', 'он', 'так']
tuple_stop_words = ('который', 'к', 'то', 'на', 'в', 'без', 'для', 'и', 'он', 'так')
punctuation = ',.!?-+"—«»'

"""примеры замены символов пунктуация
x = 'Гвидо ван Россум, известный энтузиаст разработки, который!,'
print(x.strip('!,'))
print(x.replace(',', '').replace('!', ''))
for punctuation_symbol in punctuation:
    text = text.replace(punctuation_symbol, '')
print(text)
"""
# токенизация текста - применяется в семантическом (смысловом) анализе текста

raw_words = text.split()  # raw - сырьё, необработанные слова

N_EXPERIMENTS = 100000
# Set
t0 = time()
for i in range(N_EXPERIMENTS):
    processed_words = list()  # сейчас обработаем
    for word in raw_words:
        word = word.lower()
        word = word.strip(punctuation)
        if not word:  # если слово пустое
            continue  # прервать текущую итерацию и перейти к следующей
        if word in set_stop_words:  # поиск по сету
            continue
        processed_words.append(word)

t_set = time() - t0

# Tuple
t0 = time()
for i in range(N_EXPERIMENTS):
    processed_words = list()  # сейчас обработаем
    for word in raw_words:
        word = word.lower()
        word = word.strip(punctuation)
        if not word:  # если слово пустое
            continue  # прервать текущую итерацию и перейти к следующей
        if word in tuple_stop_words:  # поиск по сету
            continue
        processed_words.append(word)

t_tuple = time() - t0

# List
t0 = time()
for i in range(N_EXPERIMENTS):
    processed_words = list()  # сейчас обработаем
    for word in raw_words:
        word = word.lower()
        word = word.strip(punctuation)
        if not word:  # если слово пустое
            continue  # прервать текущую итерацию и перейти к следующей
        if word in list_stop_words:  # поиск по сету
            continue
        processed_words.append(word)

t_list = time() - t0

# Results
print(f'Set: {round(t_set, 2)}s')
print(f'Tuple: {round(t_tuple, 2)}s')
print(f'List: {t_list:.2f}s')
# https://pyformat.info/

# sort
# min
# max
# sum
# pop
# remove

# enumerate
