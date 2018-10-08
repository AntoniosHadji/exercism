export class Cipher {
  constructor (key) {
    // char code 97-122
    let reGoodKey = /^[a-z]+$/
    if (!reGoodKey.test(key)) {
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

  encode (s, direction) {
    let result = ''
    for (let i = 0; i < s.length; i++) {
      result += String.fromCharCode(
        this._wrap(s.charCodeAt(i) + this._shift(i, direction))
      )
    }
    return result
  }

  decode (s) {
    return this.encode(s, 'decode')
  }

  _shift (i, direction = 'encode') {
    if (i >= this.key.length) {
      i = i % this.key.length
    }
    const shift = this.key.charCodeAt(i) - 97
    if (direction === 'decode') {
      return -1 * shift
    }
    return shift
  }

  _wrap (v) {
    // this is harder to read than if statement
    // and more calculation
    // return (v - 97) >= 0 ? ((v - 97) % 26) + 97 : ((v - 97) % 26) + 123
    if (v < 97) {
      return v + 26
    } else if (v > 122) {
      return v - 26
    } else {
      return v
    }
  }
}
