func searchInsert(nums []int, target int) int {
    var l int = len(nums)
    if target > nums[l - 1] {
        return l
    }
    
    var idx int = 0
    for {
        if nums[idx] == target {
            break
        }
        
        if nums[idx] > target {
            break
        }
        
        idx += 1
    }
    
    return idx
}