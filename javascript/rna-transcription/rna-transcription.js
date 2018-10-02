export function toRna (dna) {
  if (dna.length === 0) return ''

  // test that dna contains only GCTA characters
  const re = /^[GCTA]+$/
  if (!re.test(dna)) {
    throw new Error('Invalid input DNA.')
  }

  const translate = {
    'G': 'C',
    'C': 'G',
    'T': 'A',
    'A': 'U'
  }

  let dnaArr = dna.split('')
  let rna = dnaArr.map(c => translate[c])
  return rna.join('')
}
