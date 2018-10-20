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

var orbitalPeriods = map[Planet]float64{
	"Earth":   1.0,
	"Mercury": 0.2408467,
	"Venus":   0.61519726,
	"Mars":    1.8808158,
	"Jupiter": 11.862615,
	"Saturn":  29.447498,
	"Uranus":  84.016846,
	"Neptune": 164.79132,
}

func Age(seconds float64, planet Planet) float64 {
	base := seconds / 86400 / 365.25
	// base case is earth years
	return base / orbitalPeriods[planet]
}

/* Go Notes
This version, although looking more advanced than a series of if else statements,
is substantially slower on benchmark.  96ns/op vs 37ns/op for if/else if

It is usually clearer and always faster to use the built-in string comparison
operators ==, <, >, and so on.
https://golang.org/pkg/strings/#Compare
*/
