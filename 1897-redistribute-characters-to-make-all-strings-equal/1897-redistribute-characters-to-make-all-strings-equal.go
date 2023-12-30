func makeEqual(words []string) bool {
    c := map[string]int{}
    
    for _, word := range words {
        for _, ch := range word {
            c[string(ch)]++
        }
    }
    
    ll := len(words)
    for _, v := range c {
        if v % ll != 0 {
            return false
        }
    }
    
    return true
}