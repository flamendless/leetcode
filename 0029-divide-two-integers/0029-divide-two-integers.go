func divide(dividend int, divisor int) int {
    var max int = math.MaxInt32
    var min int = math.MinInt32
    
    if (dividend == min) && (divisor == -1) {
        return max
    }
    if ((dividend == max) && (divisor == max)) ||
        ((dividend == min) && (divisor == min)) {
        return 1
    }
    if (dividend == min) && (divisor == max) {
        return -1
    }
    if (dividend == max && divisor == min) {
        return 0
    }
    return dividend/divisor
}