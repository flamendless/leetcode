func restoreArray(adjacentPairs [][]int) []int {
    adj := make(map[int][]int)
    for _, v := range adjacentPairs {
        a, b := v[0], v[1]
        adj[a] = append(adj[a], b)
        adj[b] = append(adj[b], a)
    }
    
    var head int
    for k, v := range adj {
        if len(v) == 1 {
            head = k
            break
        }
    }
    
    var res []int
    q := []int{head}
    visited := map[int]bool{head: true}
    for len(q) > 0 {
        popped := q[0]
        q = q[1:]
        res = append(res, popped)
        for _, n := range adj[popped] {
            _, exists := visited[n]
            if exists {
                continue
            }
            visited[n] = true
            q = append(q, n)
        }
    }
    
    return res
}