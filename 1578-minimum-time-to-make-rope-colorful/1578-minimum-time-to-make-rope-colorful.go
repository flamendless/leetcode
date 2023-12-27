func minCost(colors string, neededTime []int) int {
    l := len(colors)
    res := 0
    
    cost := neededTime[0]
    for i := 1; i < l; i++ {
        c := colors[i]
        p := colors[i-1]
        if c != p {
            cost = neededTime[i]
            continue
        }
        
        t := neededTime[i]
        
        if t < cost {
            res += t
        } else {
            res += cost
        }
        
        if t > cost {
            cost = t
        }
    }
    
    return res
}