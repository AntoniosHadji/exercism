export const isPangram = (sentence) => {
  // short circuit if performance sensitive
  // if (sentence.length == 0) { return false };
  let dict = []
  const regex = /[a-z]/

  for (let letter of sentence) {
    let l = letter.toLowerCase()
    if (regex.test(l) && !dict.includes(l)) {
      dict.push(l)
    }
  }

  return dict.length == 26
};
