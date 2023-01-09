// Package weather provides weather forescasts.
package weather

// CurrentCondition reports the current weather conditions.
var CurrentCondition string

// CurrentLocation records the location for which the conditions are valid.
var CurrentLocation string

// Forecast takes condition and location strings and returns string report.
func Forecast(city, condition string) string {
	CurrentLocation, CurrentCondition = city, condition
	return CurrentLocation + " - current weather condition: " + CurrentCondition
}
