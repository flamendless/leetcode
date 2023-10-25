func kthGrammar(n int, k int) int {
    var x int = int(math.Pow(2, float64(n - 1)))
    
    var l int = 1
    var r int = x
    var c int = 0
    
    for i := 0; i < n - 1; i++ {
        var m int = l + int((r - l) / 2)
        if k <= m {
            r = m
        } else {
            l = m + 1
            if c == 0 {
                c = 1
            } else {
                c = 0
            }
        }
    }
    return c
}