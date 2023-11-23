func checkArithmeticSubarrays(nums []int, l []int, r []int) []bool {
    ll := len(l)
    res := make([]bool, ll)
    for i := 0; i < ll; i++ {
        res[i] = true
        size := r[i] - l[i] + 1
        if size < 2 {
            res[i] = false
            continue
        }
        arr := make([]int, size)
        copy(arr, nums[l[i]:r[i]+1])
        sort.Ints(arr)
        diff := arr[1] - arr[0]
        for j := 2; j < len(arr); j++ {
            if arr[j] - arr[j-1] != diff {
                res[i] = false
                break
            }
        }
    }
    return res
}