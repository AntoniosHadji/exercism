package hamming

import "errors"

// Distance calculates hamming distance of two genome strings
func Distance(a, b string) (int, error) {
	// if runes are important, get runes as slice that can be indexed
	// a_runes := []rune(a)
	// b_runes := []rune(b)

	if len(a) != len(b) {
		return 0, errors.New("mismatch in string lengths")
	}

	result := 0
	// , c would return type rune in c
	for i := range a {
		// if a_runes[i] != b_runes[i] {
		// indexing into string returns a byte
		// a[i], b[i] are unicode code points, not actual text character
		if a[i] != b[i] {
			result++
		}
	}

	return result, nil
}
