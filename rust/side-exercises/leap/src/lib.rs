pub fn is_leap_year(year: i32) -> bool {
    let four: bool            = (year % 4)   == 0;
    let hundred: bool         = (year % 100) == 0;
    let four_hundred: bool    = (year % 400) == 0;

    return (four && !hundred) || four_hundred;
}
