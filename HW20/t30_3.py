def hamming_dist(s1: str, s2: str) -> int:
    if len(s1) != len(s2):
        raise ValueError("Strings must have same length")
    
    return sum(c1 != c2 for c1, c2 in zip(s1, s2))
