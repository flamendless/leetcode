func isReachableAtTime(sx int, sy int, fx int, fy int, t int) bool {
    xd := float64(math.Abs(float64(sx - fx)))
    yd := float64(math.Abs(float64(sy - fy)))
    md1 := int(math.Min(xd, yd))
    md2 := int(math.Abs(yd - xd))
    md := md1 + md2
    if md == 0 {
        return t != 1
    }
    return t >= md
}