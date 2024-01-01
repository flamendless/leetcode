func findContentChildren(g []int, s []int) int {
    lg := len(g)
    ls := len(s)
    
    sort.Ints(g)
    sort.Ints(s)
    
    l := 0
    r := 0
    
    for (l < lg) && (r < ls) {
        if s[r] >= g[l] {
            l++
            r++
        } else {
            r++
        }
    }
    
    return l
}