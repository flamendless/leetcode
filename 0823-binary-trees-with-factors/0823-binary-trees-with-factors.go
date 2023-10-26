func numFactoredBinaryTrees(arr []int) int {
    const MOD int64 = 1e9 + 7
    
    sort.Ints(arr)
    
    var s map[int]bool = make(map[int]bool)
    for _, x := range arr {
        s[x] = true
    }
    
    var c map[int]int64 = make(map[int]int64)
    for _, x := range arr {
        c[x] = 1
    }
    
    for _, i := range arr {
        var sfi int = int(math.Sqrt(float64(i)))
        for _, j := range arr {
            if j > int(sfi) {
                break
            }
            
            ij := i/j
            if ((i % j) == 0) && s[ij] {
                t := (c[j] * c[ij]) % MOD
                if ij == j {
                    c[i] = (c[i] + t) % MOD
                } else {
                    c[i] = (c[i] + (t * 2)) % MOD
                }
            }
        }
    }
    
    var res int64 = 0
    for _, v := range c {
        res = (res + v) % MOD
    }
    return int(res)
}