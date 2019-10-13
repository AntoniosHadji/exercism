export default class Triangle {
  constructor (a, b, c) {
    this.a = a
    this.b = b
    this.c = c
  }

  kind () {
    if (!(this.a + this.b >= this.c) ||
        !(this.a + this.c >= this.b) ||
        !(this.b + this.c >= this.a) ||
        this.a <= 0 || this.b <= 0 || this.c <= 0) {
      throw new Error('invalid triangle')
    }

    if (this.a === this.b && this.a === this.c && this.b === this.c) {
      return 'equilateral'
    }

    if (this.a === this.b || this.a === this.c || this.b === this.c) {
      return 'isosceles'
    }

    if (this.a !== this.b && this.a !== this.c && this.b !== this.c) {
      return 'scalene'
    }
  }
}
