// function bt(value, left, right) {
//   return {
//     value,
//     left,
//     right,
//   };
// }

export default class Zipper {
  constructor (t, o, p) {
    this.tree = t
    if (p) {
      this.parent = p
    } else {
      this.parent = null
    }

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
      return new Zipper(this.tree.left, this.originalTree, this)
    } else {
      return null
    }
  }

  right () {
    if (this.tree.right) {
      return new Zipper(this.tree.right, this.originalTree, this)
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
    if (this.tree.value) {
      return this.tree.value
    } else {
      return null
    }
  }

  up () {
    return this.parent
  }
}
