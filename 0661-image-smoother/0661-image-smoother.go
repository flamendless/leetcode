type Dir struct {
    y int
    x int
}

func imageSmoother(img [][]int) [][]int {
    dirs := [8]Dir{
        {y: -1, x: 0}, // N
        {y: -1, x: 1}, //NE
        {y: 0, x: 1}, // E
        {y: 1, x: 1}, // SE
        {y: 1, x: 0}, // S
        {y: 1, x: -1}, // SW
        {y: 0, x: -1}, // W
        {y: -1, x: -1}, // NW
    } 
    
    ll := len(img)
    
    res := make([][]int, ll)
    for i := 0; i < ll; i++ {
        res[i] = make([]int, len(img[i]))
    }
    
    for y := 0; y < ll; y++ {
        for x := 0; x < len(img[y]); x++ {
            sum := img[y][x]
            n := 1
            temp_y := y
            temp_x := x
            
            for i := 0; i < len(dirs); i++ {
                temp_y = y + dirs[i].y
                temp_x = x + dirs[i].x
                if temp_y >= 0 && temp_y < ll && temp_x >= 0 && temp_x < len(img[y]) {
                    sum += img[temp_y][temp_x]
                    n++
                }
            }
            res[y][x] = sum/n
        }
    }
    
    return res
}