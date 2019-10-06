extern crate chrono;
use chrono::{DateTime, Duration, Utc};

// Returns a Utc DateTime one billion seconds after start.
pub fn after(start: DateTime<Utc>) -> DateTime<Utc> {
    // 1_000_000_000 in scientific notation is (1e9 as i64)
    // scientific notation produces type float
    start + Duration::seconds(1_000_000_000)
}
