const c = require('./collatz-conjecture.js')
const Benchmark = require('benchmark')

const suite = new Benchmark.Suite()

suite.add('recursive calls', function () {
  c.stepsRecursive(10000)
}).add('while loop', function () {
  c.stepsWhile(10000)
}).on('cycle', function (event) {
  console.log(String(event.target))
}).on('complete', function () {
  console.log('Fastest is ' + this.filter('fastest').map('name'))
}).run({ 'async': true })
