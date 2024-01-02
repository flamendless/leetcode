func findMatrix(nums []int) [][]int {
    sort.Ints(nums)
    matrix := [][]int{}
    n := 0
    
    for i, num := range nums {
        if (i != 0) && (num == nums[i - 1]) {
            n++
        } else {
            n = 0
        }
        
        if len(matrix) < (n + 1) {
            matrix = append(matrix, []int{num})
        } else {
            matrix[n] = append(matrix[n], num)
        }
    }
    return matrix
}