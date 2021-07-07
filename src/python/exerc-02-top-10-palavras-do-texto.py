#
# filename   : exerc-02-top-10-palavras-do-texto.py
# Description:
# Docs       :
#

# list of files to be processed
list_files = ['file-06-trecho-livro-filosofia.txt', 'file-07-trecho-livro-literatura.txt', 'file-08-trecho-livro-biblia-ezequiel-25.txt']
enconding_utf8 = "utf8"

list_words_ignore = ['a', 'as', 'o', 'os', 'e', 'de', 'da', 'das', 'do', 'dos', 'um', 'uns', 'uma', 'umas', 'que', 'por', 'porque']
str_chars_ignore = '0123456789,.;/\\?![]^~{}`"\'!@#$%&*()-_=+' + '—'

# loop files ...
for filename in list_files:
  with open(filename, 'r', encoding=enconding_utf8) as file:
    list_lines = file.read().splitlines()
    dict_unique_words = dict()
    num_line = 0
    # loop lines in file ...
    for line in list_lines:
      num_line += 1
      for i in range(len(str_chars_ignore)):
        line = line.replace(str_chars_ignore[i], ' ')
      line_adjusted = ' ' + line.lower() + ' '
      list_words_line = line_adjusted.split(' ')
      num_word = 0
      # loop list_words_line ...
      for word in list_words_line:
        if len(word) > 0:
          num_word += 1
          flag_ignore = 0
          if word in list_words_ignore:
            flag_ignore = 1
          dict_values = dict_unique_words.get(word)
          counter = 1
          str_line_word = 'L' + str(num_line) + '-' + 'W' + str(num_word)
          if not dict_values:
            dict_values = {'counter': counter, 'flag_ignore': flag_ignore, 'line_word': [ str_line_word ] }
          else:
            if dict_values['counter']:
              counter = dict_values['counter'] + 1
            list_line_word = list()
            if dict_values['line_word']:
              list_line_word = dict_values['line_word']
            list_line_word.append(str_line_word)
            dict_values['counter'] = counter
            dict_values['flag_ignore'] = flag_ignore
            dict_values['line_word'] = list_line_word
          # update unique words conter
          dict_unique_words.update({word: dict_values})
    # print('dict_unique_words: ', dict_unique_words)
    list_unique_words_sorted = sorted(dict_unique_words.items(), key=lambda x: x[1]['counter'], reverse=True)
    # print('list_unique_words_sorted: ', list_unique_words_sorted)

    # Report
    print(f'* {filename}:')
    num_top10 = 0
    for item in list_unique_words_sorted:
      if num_top10 < 10 and item[1]['flag_ignore'] == 0:
        num_top10 += 1
        word = item[0]
        counter = item[1]['counter']
        line_word =  item[1]['line_word']
        print(f'  {num_top10}: {word} ({counter}) - {line_word}')

