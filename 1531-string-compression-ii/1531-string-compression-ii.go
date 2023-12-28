type Key struct {
    i int
    k int
    prev string
    prev_count int
}

func getLengthOfOptimalCompression(s string, k int) int {
    cache := map[Key]int{}   
    
    ls := len(s)
    
    calc := func(key Key) int{return 0}
    
    calc = func(key Key) int {
        v, exists := cache[key]
        if exists {
            return v
        }
        
        i := key.i
        k := key.k
        prev := key.prev
        prev_count := key.prev_count
        
        if k < 0 {
            return 9999999
        }
        if i == ls {
            return 0
        }
        
        res := 0
        
        if string(s[i]) == prev {
            inc := 0
            if prev_count == 1 || prev_count == 9 || prev_count == 99 {
                inc = 1
            }
            res = inc + calc(Key{i + 1, k, prev, prev_count + 1})
        } else {
            a := calc(Key{i + 1, k - 1, prev, prev_count})
            b := 1 + calc(Key{i + 1, k, string(s[i]), 1})
            if a <= b {
                res = a
            } else {
                res = b
            }
        }
        
        cache[key] = res
        return res
    }
    
    
    return calc(Key{0, k, string(""), 0})
}