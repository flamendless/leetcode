func findMissingAndRepeatedValues(grid [][]int) []int {
    d := map[int]int{}
    a := []int{}
    
    duplicate := 0
    
    for _, y := range grid {
        for _, x := range y {
            d[x]++
            count, _ := d[x]
            if count > 1 {
                duplicate = x
            } else {
                a = append(a, x)
            }   
        }
    }
    
    missing := len(a) + 1
    
    sort.Ints(a)
    for i := 0; i < len(a); i++ {
        expected := i + 1
        got := a[i]
        if expected != got {
            missing = expected
            break
        }
    }
    
    return []int{duplicate, missing}
}