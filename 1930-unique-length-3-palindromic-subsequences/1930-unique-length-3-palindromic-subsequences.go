func countPalindromicSubsequence(s string) int {
    const a = 'a'
    chars := make([]int, 26)
    for _, ch := range s {
        idx := ch - a
        chars[idx]++
    }
    
    res := 0
    
    for i, n := range chars {
        if n < 2 {
            continue
        }
        l := 0
        r := len(s) - 1
        ch := byte(a + i)
        for {
            if s[l] == ch {
                break
            }
            l++
        }
        for {
            if s[r] == ch {
                break
            }
            r--
        }
        
        d := make([]int, 26)
        l++
        for l < r {
            idx := s[l] - a
            d[idx]++
            l++
        }
        
        for _, n := range d {
            if n >= 1 {
                res++
            }
        }
    }
    
    return res
}