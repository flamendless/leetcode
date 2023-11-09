func countHomogenous(s string) int {
    var mod int = int(math.Pow(10, 9) + 7)
    
    var prev rune
    var v int
    var res int = 0
    
    for _, c := range s {
        if prev != c {
            v = 0
            prev = c
        }
        v++
        res += v 
    }
    
    return res % mod
}