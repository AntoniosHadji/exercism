export const isPangram = (sentence) => {
  const regex = /[a-z]/
  const letters = Array.from(sentence.toLowerCase()).filter(x => regex.test(x));
  const s = new Set(letters)

  return s.size == 26
};
