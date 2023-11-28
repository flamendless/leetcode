func numberOfWays(corridor string) int {
    const MOD = 1000000007
    total := 0
    for _, v := range corridor {
        if v == 'S' {
            total++
        }
    }
    if (total == 0) || (total % 2 != 0) {
        return 0
    }

    prev := 0
    free := 0
    res := 1
    for i, v := range corridor {
        if v != 'S' {
            continue
        }
        free++
        if free == 3 {
            res = (res * (i - prev)) % MOD
            free = 1
        }
        prev = i
    }

    return res
}