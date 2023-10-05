func middle_out(s string, left int, right int) int {
    var l int = left;
    var r int = right;
    for {
        if l >= 0 && r < len(s) && s[l] == s[r] {
            l--;
            r++;
        } else {
            break
        }

    }
    return r - l - 1;
}

func longestPalindrome(s string) string {
    if len(s) < 1 {
        return "";
    }
        
    var left int = 0;
    var right int = 0;
    
    for i := 0; i < len(s); i++ {
        var len_a int = middle_out(s, i, i);
        var len_b int = middle_out(s, i, i + 1);
        var higher int = int(math.Max(float64(len_a), float64(len_b)));
        if higher > right - left {
            left = i - (higher  - 1)/2;
            right = i + higher/2;
        }
    }
    
    return s[left:right+1];
}