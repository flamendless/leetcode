func largestGoodInteger(num string) string {
    l := 0
    r := 1
    
    n := -1
    c := ""
    
    for {
        if l == r || r > len(num)-1 {
            break
        }
        if num[l] == num[r] {
            r++
            
            if (r - l) >= 3 {
                lch := string(num[l])
                x, _ := strconv.Atoi(lch)
                if x > n {
                    c = strings.Repeat(lch, 3)
                    n = x
                }
            }
        } else {
            l = r
            r++
        }
    }
    return c
}