export default class Zipper {
  constructor (t, p) {
    this.tree = Object.assign({}, t)
    if (p) {
      this.parent = p
    } else {
      this.parent = null
    }
  }

  static fromTree (obj) {
    return new Zipper(obj, null)
  }

  toTree () {
    let t = this
    while (t.parent !== null) {
      t = t.parent
    }
    return t.tree
  }

  left () {
    if (this.tree.left) {
      return new Zipper(this.tree.left, this)
    } else {
      return null
    }
  }

  right () {
    if (this.tree.right) {
      return new Zipper(this.tree.right, this)
    } else {
      return null
    }
  }

  setValue (v) {
    this.tree.value = v
    return this
  }

  setLeft (o) {
    this.tree.left = o
    return this
  }

  setRight (o) {
    this.tree.right = o
    return this
  }

  value () {
    return this.tree.value
  }

  up () {
    return this.parent
  }
}
