func hammingWeight(num uint32) int {
    return bits.OnesCount(uint(num))
}