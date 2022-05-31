from functools import cmp_to_key

def char_count(str):
  #create empty dictionary
  chars ={}
  #add character count into dictionary
  for char in str:
    if char != " ":
      if char in chars:
        chars[char] += 1
      else:
        chars[char] = 1
  # turn char dictionary to list of characters
  list_of_chars = []
  for key,val in chars.items():
    list_of_chars.append([key]+ [val])
  #sort list of characters
  sorted_list_of_chars = sorted(list_of_chars, key=lambda x : (-x[1], x[0]))
  ##return sorted list of characters
  return sorted_list_of_chars 

char_count("an apple a day will keep the doctor away")


