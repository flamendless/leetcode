func lengthOfLastWord(s string) int {
    s = strings.TrimSpace(s)
    var l []string = strings.Split(s, " ")
    var last *string = &l[len(l) - 1]
    return len(*last)
}