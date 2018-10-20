function steps (num) {
  return stepsRecursive(num)
}

function stepsWhile (num) {
  if (num <= 0) throw new Error('Only positive numbers are allowed')

  let count = 0
  while (num !== 1) {
    if (num % 2 === 0) {
      num = num / 2
    } else {
      num = 3 * num + 1
    }
    count++
  }

  return count
}

// test code to compare recursive calls to while loop
function stepsRecursive (num) {
  if (num <= 0) throw new Error('Only positive numbers are allowed')

  if (num === 1) {
    return 0
  } else if (num % 2 === 0) {
    return 1 + steps(num / 2)
  } else {
    return 1 + steps(3 * num + 1)
  }
}

module.exports = { steps, stepsRecursive, stepsWhile }

// inconclusive results with benchmarkjs
// at first while loop is faster, then recursive showed 2x+ speedup with no
// code change
//
// recursive calls x 14,524,286 ops/sec ±0.91% (86 runs sampled)
// while loop x 7,256,519 ops/sec ±0.66% (90 runs sampled)
// Fastest is recursive calls

// recursive calls x 5,263,785 ops/sec ±0.77% (86 runs sampled)
// while loop x 7,124,185 ops/sec ±0.67% (85 runs sampled)
// Fastest is while loop
