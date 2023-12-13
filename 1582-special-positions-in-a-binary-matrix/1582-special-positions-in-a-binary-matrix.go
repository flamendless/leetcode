func numSpecial(mat [][]int) int {
    rows := len(mat)
    cols := len(mat[0])
    res := 0

    for i := 0; i < rows; i++ {
        checkCol := -1
        for j := 0; j < cols; j++ {
            if mat[i][j] == 1 {
                if checkCol == -1 {
                    checkCol = j
                } else {
                    checkCol = -1
                    break
                }
            }
        }
        if checkCol == -1 {
            continue
        }
        special := 1
        for k := 0; k < rows; k++ {
            if k == i {
                continue
            }
            if mat[k][checkCol] == 1 {
                special = 0
				mat[0][checkCol] = 1
                break
            }
        }
        res += special
    }
    return res 
}