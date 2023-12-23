func isPathCrossing(path string) bool {
    dirs := map[rune][2]int{
        'N': {0, -1},
        'S': {0, 1},
        'W': {-1, 0},
        'E': {1, 0},
    }
    
    x := 0
    y := 0
    
    visited := map[[2]int]bool{}
    visited[[2]int{x, y}] = true
    
    
    for _, ch := range path {      
        d, _ := dirs[ch]
        x += d[0]
        y += d[1]
        np := [2]int{x, y}
        if visited[np] {
            return true
        }
        visited[np] = true
    }
    return false
}