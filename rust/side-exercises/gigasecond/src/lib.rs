extern crate chrono;
use chrono::{DateTime, Utc, Duration};

// Returns a Utc DateTime one billion seconds after start.
pub fn after(start: DateTime<Utc>) -> DateTime<Utc> {
    let x: i64 = 10;
    start.checked_add_signed(Duration.seconds(x.pow(9)))
}
