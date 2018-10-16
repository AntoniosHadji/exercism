export default class Zipper {
  constructor (t, o) {
    this.tree = t
    if (!o) {
      this.originalTree = t
    } else {
      this.originalTree = o
    }
  }

  static fromTree (t) {
    return new Zipper(t)
  }

  toTree () {
    return this.originalTree
  }

  left () {
    if (this.tree.left) {
      return new Zipper(this.tree.left, this.originalTree)
    } else {
      return null
    }
  }

  right () {
    if (this.tree.right) {
      return new Zipper(this.tree.right, this.originalTree)
    } else {
      return null
    }
  }

  value () {
    if (this.tree.value) {
      return this.tree.value
    } else {
      return null
    }
  }

  up () {
    // TODO: up must return parent node
    return null
  }
}
