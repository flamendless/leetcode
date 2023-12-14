func onesMinusZeros(grid [][]int) [][]int {
    nrows := len(grid)
    ncols := len(grid[0])
    diff := make([][]int, nrows)
    for i := 0; i < len(grid); i++ {
        diff[i] = make([]int, ncols)
    }

    var rows []int
    var cols []int
    
    for _, v := range(grid) {
        row := 0
        for _, w := range(v) {
            if w == 0 {
                row -= 1
            } else {
                row += 1
            }
        }
        rows = append(rows, row)
    }

    for i := 0; i < ncols; i++{
        col := 0
        for _, w := range(grid) {
            if w[i] == 0 {
                col -= 1
            } else {
                col += 1
            }
        }
        cols = append(cols, col)
    }

    for i, v := range(diff) {
        for j ,_ := range(v) {
            v[j] = rows[i] + cols[j]
        }
    }
    return diff

}