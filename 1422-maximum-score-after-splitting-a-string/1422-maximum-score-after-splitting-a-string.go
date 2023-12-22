func maxScore(s string) int {
    zeroes := 0
    ones := 0
    for _, ch := range s {
        if ch == '1' {
            ones++
        }
    }
    
    res := 0
    
    for i := 0; i < len(s) - 1; i++ {
        if s[i] == '0' {
            zeroes++
        } else if s[i] == '1' {
            ones--
        }
        
        sum := zeroes + ones
        if sum > res {
            res = sum
        }
    }
    
    return res
}