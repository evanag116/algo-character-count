def char_count(str):
  ans_dict = {i: str.count(i) for i in set(str.replace(" ", ""))}
  letters = sorted(ans_dict)
  counts = sorted(ans_dict.values(), reverse=True)
  res = []

  for num in range(len(counts)):
    for letter in letters:
      if counts[num] == str.count(letter):
        res.append([letter, counts[num]])
        letters.remove(letter)
        break

  return res

