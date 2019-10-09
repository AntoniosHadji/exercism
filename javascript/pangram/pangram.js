export const isPangram = (sentence) => {
  if (sentence.length == 0) { return false };
  dict = {}
  regex = /[a-z]+/
  for (letter of sentence) {
    l = letter.toLowerCase()
    if (!regex.test(l)) continue
    if (dict.hasOwnProperty(l)) {
      return false
    } else {
      dict[l] = 1
    }
  }
  return true
};
