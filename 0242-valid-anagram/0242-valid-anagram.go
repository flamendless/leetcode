func isAnagram(s string, t string) bool {
    ls := len(s)
    lt := len(t)
    if ls != lt {
        return false
    }
    
    ds := map[rune]int{}
    dt := map[rune]int{}
    
    for _, ch := range s {
        ds[ch]++
    }
    for _, ch := range t {
        dt[ch]++
    }
    
    for k, v := range ds {
        if dt[k] != v {
            return false
        }
    }
    
    return true
}