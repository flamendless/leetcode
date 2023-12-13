func maxProduct(nums []int) int {
    sort.Ints(nums)
    i := nums[len(nums)-2]
    j := nums[len(nums)-1]
    return (i-1)*(j-1)
}