package space

/* Given an age in seconds, calculate how old someone would be on:
   - Earth: orbital period 365.25 Earth days, or 31557600 seconds
   - Mercury: orbital period 0.2408467 Earth years
   - Venus: orbital period 0.61519726 Earth years
   - Mars: orbital period 1.8808158 Earth years
   - Jupiter: orbital period 11.862615 Earth years
   - Saturn: orbital period 29.447498 Earth years
   - Uranus: orbital period 84.016846 Earth years
   - Neptune: orbital period 164.79132 Earth years
*/

type Planet string

func Age(seconds float64, planet Planet) float64 {
	base := seconds / 86400 / 365.25
	if planet == "Mercury" {
		return base / 0.2408467
	} else if planet == "Venus" {
		return base / 0.61519726
	} else if planet == "Mars" {
		return base / 1.8808158
	} else if planet == "Jupiter" {
		return base / 11.862615
	} else if planet == "Saturn" {
		return base / 29.447498
	} else if planet == "Uranus" {
		return base / 84.016846
	} else if planet == "Neptune" {
		return base / 164.79132
	}
	// base case is earth years
	return base
}

/* Go Notes
It is usually clearer and always faster to use the built-in string comparison
operators ==, <, >, and so on.
https://golang.org/pkg/strings/#Compare
*/
