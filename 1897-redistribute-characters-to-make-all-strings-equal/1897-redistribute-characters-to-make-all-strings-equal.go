func makeEqual(words []string) bool {
    ll := len(words)
    c := map[string]int{}
    
    greedy_ret := false
    
    for _, word := range words {
        for _, ch := range word {
            sch := string(ch)
            c[sch]++
            v, _ := c[sch]
            if v % ll != 0 {
                greedy_ret = true
            } else {
                greedy_ret = false
            }
        }
    }
    
    if greedy_ret {
        return false
    }
    
    for _, v := range c {
        if v % ll != 0 {
            return false
        }
    }
    
    return true
}