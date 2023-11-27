func knightDialer(n int) int {
    const MOD = 1000000007
    moves := [10]int{1, 1, 1, 1, 1, 1, 1, 1, 1, 1}

    res := 10
    for i := 1; i < n; i++ {
        next := make([]int, 10)
        next[0] = moves[4] + moves[6]
        next[1] = moves[6] + moves[8]
        next[2] = moves[7] + moves[9]
        next[3] = moves[4] + moves[8]
        next[4] = moves[0] + moves[3] + moves[9]
        next[5] = 0
        next[6] = moves[0] + moves[1] + moves[7]
        next[7] = moves[2] + moves[6]
        next[8] = moves[1] + moves[3]
        next[9] = moves[2] + moves[4]

        res = 0
        for i := range moves {
            moves[i] = next[i] % MOD
            res = (res + moves[i]) % MOD
        }
    }

    return res
}