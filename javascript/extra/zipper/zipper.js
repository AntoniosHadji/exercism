export default class Zipper {
  constructor (t) {
    this.tree = t
  }

  static fromTree (t) {
    return new Zipper(t)
  }

  toTree () {
    return this.tree
  }

  left () {
    if (this.tree.left) {
      return new Zipper(this.tree.left)
    } else {
      return null
    }
  }

  right () {
    return new Zipper(this.tree.right)
  }

  value () {
    return this.tree.value
  }
}
