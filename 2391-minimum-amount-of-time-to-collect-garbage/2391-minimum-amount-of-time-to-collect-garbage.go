func garbageCollection(garbage []string, travel []int) int {
    ps := make([]int, len(travel) + 1)
    for i := 1; i < len(ps); i++ {
        ps[i] = ps[i-1] + travel[i-1]
    }
    
    last := map[byte]int{
        'M': 0,
        'P': 0,
        'G': 0,
    }
    res := 0
    
    for i := 0; i < len(garbage); i++ {
        for j := 0; j < len(garbage[i]); j++ {
            g := garbage[i][j]
            last[g] = i
            res++
        }
    }
    
    res += ps[last['M']] + ps[last['P']] + ps[last['G']]
    return res
}