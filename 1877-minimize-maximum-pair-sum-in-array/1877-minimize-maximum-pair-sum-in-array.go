func minPairSum(nums []int) int {
    l := 0
    r := len(nums) - 1
    res := 0
    
    sort.Ints(nums)
    for {
        if l >= r {
            break
        }
        sum := nums[l] + nums[r]
        if sum > res {
            res = sum
        }
        l++
        r--
    }
    
    return res
}