// Package twofer returns a string
package twofer

import "fmt"

// ShareWith contructs and returns a string
func ShareWith(name string) string {
	if len(name) == 0 {
		name = "you"
	}
	return fmt.Sprintf("One for %v, one for me.", name)
}
