func numberGame(nums []int) []int {
    sort.Ints(nums)
    res := []int{}

    i := 0
    for {
        if i >= len(nums) {
            break
        }
        alice := nums[i]
        bob := nums[i + 1]
        
        res = append(res, bob)
        res = append(res, alice)
        
        i += 2
    }
    
    return res
}