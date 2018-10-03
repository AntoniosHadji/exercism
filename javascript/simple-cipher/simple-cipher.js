export class Cipher {
  constructor (key) {
    let reAccept = /^[a-z]+$/
    if (!reAccept.test(key)) {
      throw new Error('Bad key')
    }

    if (!key) {
      key = ''
      for (let i = 0; i < 100; i++) {
        key += String.fromCharCode(Math.round(Math.random() * 25, 0) + 97)
      }
    }
    this.key = key
  }

  encode (s) {
    let result = ''
    for (let i = 0; i < s.length; i++) {
      let shift = this._shift(i)
      result += String.fromCharCode(this._wrap(s.charCodeAt(i) + shift))
    }
    return result
  }

  decode (s) {
    let result = ''
    for (let i = 0; i < s.length; i++) {
      let shift = this._shift(i)
      result += String.fromCharCode(this._wrap(s.charCodeAt(i) - shift))
    }
    return result
  }

  _shift (i) {
    if (i >= this.key.length) {
      i = i % this.key.length
    }
    return this.key.charCodeAt(i) - 97
  }

  _wrap (v) {
    if (v < 97) {
      return v + 26
    } else if (v > 122) {
      return v - 26
    } else {
      return v
    }
  }
}
