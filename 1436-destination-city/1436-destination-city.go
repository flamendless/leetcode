func destCity(paths [][]string) string {
    d := make(map[string]bool)
    for _, path := range paths {
        from := path[0]
        to := path[1]
        d[from] = true
        _, exists := d[to]
        if !exists {
            d[to] = false
        }
    }
    
    for city, visited := range d {
        if !visited {
            return city
        }
    }
    
    return ""
}