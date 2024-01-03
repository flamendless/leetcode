func findPeaks(mountain []int) []int {
    res := []int{}
    for i := 1; i < len(mountain)-1; i++ {
        if mountain[i-1] < mountain[i] && mountain[i+1] < mountain[i] {
            res = append(res, i) 
        }
    }
    return res
}