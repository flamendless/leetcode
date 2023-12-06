func totalMoney(n int) int {
    res := 0
    
    monday := 0
    inc := 0
    for i := 0; i < n; i++ {
        if i % 7 == 0 {
            monday += 1
            inc = monday
        } else {
            inc++
        }
        res += inc
    }
    
    return res
}