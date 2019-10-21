// bob is a chat bot
// use this instead: https://golang.org/pkg/strings/
package bob

import "regexp"

// Hey takes a comment and returns a response
func Hey(remark string) string {

	switch {

	case regexp.MustCompile(`^\s+$`).MatchString(remark) || len(remark) == 0:
		return "Fine. Be that way!"

	case regexp.MustCompile(`^[A-Z\s]+\?\s*$`).MatchString(remark):
		return "Calm down, I know what I'm doing!"

	case regexp.MustCompile(`.+\?\s*$`).MatchString(remark):
		return "Sure."

	case regexp.MustCompile(`^[0-9,\s]+$`).MatchString(remark):
		return "Whatever."

	case regexp.MustCompile(`^[^a-z]+[\!\s]*$`).MatchString(remark):
		return "Whoa, chill out!"

	default:
		return "Whatever."

	}

}

// https://golang.org/doc/effective_go.html#commentary
