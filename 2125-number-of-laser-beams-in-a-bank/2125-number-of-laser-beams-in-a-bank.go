func numberOfBeams(bank []string) int {
    prev := 0
    res := 0
    
    for _, str := range bank {
        count := 0
        bs := []byte(str)
        for _, b := range bs {
            if b == '1' {
                count++
            }
        }
        
        if count > 0 {
            res += (prev * count)
            prev = count
        }
    }
    
    return res
}