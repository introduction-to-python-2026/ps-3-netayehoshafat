def approximate_pi(n_terms):
    if n_terms == 0:
        return 0
    Leib_sum = 0
    for n in range(n_terms):
        Leib_sum += ((-1) ** n) / ((2 * n) + 1)
    approximate_pi = 4.0 * Leib_sum
    return approximate_pi
