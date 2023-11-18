func maxFrequency(nums []int, k int) int {
    sort.Ints(nums)
    res := 0
    l := 0
    sum := 0
    
    for r := 0; r < len(nums); r++ {
        sum += nums[r]
        
        for (nums[r] * (r - l + 1)) > sum + k {
            sum -= nums[l]
            l++
        }
         
        if (r - l + 1) > res {
            res = r - l+1
        }
    }
    
    return res
}