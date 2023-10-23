func isPowerOfFour(n int) bool {
    var x int = 1
    for x < n {
        x *= 4
    }
    return x == n
}