// ES6 syntax
export default class Year {
  constructor (y) {
    this.yr = y
  }

  isLeap () {
    // abc is truthy if not evenly divisible
    let a = this.yr % 4
    let b = this.yr % 100
    let c = this.yr % 400

    // divisible by 4
    if (!a) {
      // divisible by 100 not 400
      if (!b && c) return false

      return true
    } else {
      // not divisible by 4
      return false
    }
  }
}
