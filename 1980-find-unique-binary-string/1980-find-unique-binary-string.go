func findDifferentBinaryString(nums []string) string {
    res := make([]byte, len(nums))
    for i := range nums {
        if nums[i][i] == '0' {
            res[i] = '1'
        } else {
            res[i] = '0'
        }
    }
    return string(res)
}