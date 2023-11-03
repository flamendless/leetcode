func buildArray(target []int, n int) []string {
    set := make(map[int]bool)
    for _, n := range target {
        set[n] = true
    }
    
    res := []string{}
    
    for i := 1; i <= target[len(target)-1]; i++ {
        _, ok := set[i]
        if ok {
            res = append(res, "Push")   
        } else {
            res = append(res, "Push")
            res = append(res, "Pop")
        }
    }
    
    return res
}