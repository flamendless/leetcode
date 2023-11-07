func eliminateMaximum(dist []int, speed []int) int {
    length := len(dist)
    arriveTime := make([]float64, length)
    
    for i := 0; i < length; i++ {
        arriveTime[i] = float64(dist[i])/float64(speed[i])
    }
    
    sort.Float64s(arriveTime)
    
    for i, at := range arriveTime {
        if at <= float64(i) {
            return i
        }
    }
    
    return length
}