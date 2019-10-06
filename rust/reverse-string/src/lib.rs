use unicode_segmentation::UnicodeSegmentation;

pub fn reverse(input: &str) -> String {
    //  input.chars().rev().collect()
    //  true to use extended graphemes
    UnicodeSegmentation::graphemes(input, true).rev().collect()
}
