func isPalindrome(x int) bool {
    var s string = strconv.Itoa(x)
    
    var l int = 0
    var r int = len(s) - 1
    
    for l < r {
        if s[l] != s[r] {
            return false
        }
        
        l += 1
        r -= 1
    }
    
    return true
}