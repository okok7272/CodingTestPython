words = input().upper()
#소문자를 대문자로
special_words = list(set(words))
cnt_list = []
for i in special_words:
    cnt = words.count(i)
    cnt_list.append(cnt)

if cnt_list.count(max(cnt_list))>1:
    print('?')
else:
    max_index = cnt_list.index(max(cnt_list))
    print(special_words[max_index])

