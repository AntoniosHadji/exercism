// ES6 module / class syntax
export default class Year {
  constructor (y) {
    this.yr = y
  }

  isLeap () {
    // abc is truthy if not evenly divisible
    const a = this.yr % 4
    const b = this.yr % 100
    const c = this.yr % 400

    // divisible by 4
    if (!a) {
      // divisible by 100 not 400
      if (!b && c) return false

      return true
    }
    // not divisible by 4
    return false
  }
}
