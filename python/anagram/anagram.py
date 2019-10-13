def find_anagrams(word, candidates):
    test = sorted(word.lower())
    valid_candidates = [
            candidate for candidate in candidates
            if word.lower() != candidate.lower()
            ]
    return [candidate for candidate in valid_candidates
            if test == sorted(candidate.lower())
            ]
