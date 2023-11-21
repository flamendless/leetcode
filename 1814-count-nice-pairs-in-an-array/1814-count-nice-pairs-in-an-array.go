func rev(n int) int {
    res := 0
    for x := n; x != 0; x /= 10 {
        res = (res * 10) + (x % 10)
    }
    return res
}

func countNicePairs(nums []int) int {
    m := make(map[int]int)
    mod := int(1e9 + 7)
    res := 0
    
    for i := 0; i < len(nums); i++ {
        n := nums[i]
        cur := n - rev(n)
        res += m[cur]
        res %= mod
        m[cur]++
    }
    
    return res
}