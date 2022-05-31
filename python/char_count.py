from functools import cmp_to_key

def char_count(str):
  chars ={}
  for char in str:
    if char != " ":
      if char in chars:
        chars[char] += 1
      else:
        chars[char] = 1
  # //turn char dict to list
  list_of_chars = []
  for key,val in chars.items():
    list_of_chars.append([key]+ [val])
    print(sorted(list_of_chars, key=lambda x : (-x[1], x[0])))
  return sorted(list_of_chars, key=lambda x : (-x[1], x[0]))
  # print(list_of_chars)

# print(char_count("an apple a day will keep the doctor away"))


