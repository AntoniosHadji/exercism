// bob is a chat bot
package bob

import "regexp"

// Hey takes a comment and returns a response
func Hey(remark string) string {
	var onlyWhitespace = regexp.MustCompile(`^\s+$`)
	var question = regexp.MustCompile(`.+\?\s*$`)
	var q_all_caps_with_whitespace = regexp.MustCompile(`^[A-Z\s]+\?\s*$`)
	var numbers_comma_whitespace = regexp.MustCompile(`^[0-9,\s]+$`)
	var everything_not_lower_case = regexp.MustCompile(`^[^a-z]+[\!\s]*$`)

	if onlyWhitespace.MatchString(remark) || len(remark) == 0 {
		return "Fine. Be that way!"
	} else if q_all_caps_with_whitespace.MatchString(remark) {
		return "Calm down, I know what I'm doing!"
	} else if question.MatchString(remark) {
		return "Sure."
	} else if numbers_comma_whitespace.MatchString(remark) {
		return "Whatever."
	} else if everything_not_lower_case.MatchString(remark) {
		return "Whoa, chill out!"
	} else {
		return "Whatever."
	}
}

// https://golang.org/doc/effective_go.html#commentary
