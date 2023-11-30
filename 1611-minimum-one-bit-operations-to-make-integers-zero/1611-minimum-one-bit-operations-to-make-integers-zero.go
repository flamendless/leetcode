func minimumOneBitOperations(n int) int {
    if n <= 1 {
        return n
    }
    k := -1
    for i := 1; i <= n; i <<= 1 {
        k++
    }
    return ((1 << (k + 1)) - 1) - minimumOneBitOperations(n - (1 << k))
}