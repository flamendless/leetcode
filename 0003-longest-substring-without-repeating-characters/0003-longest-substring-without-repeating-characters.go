func lengthOfLongestSubstring(s string) int {
    if (len(s) == 0) || (len(s) == 1) {
        return len(s)
    }
    
	var slow int = 0
	var fast int = 1

	var set map[byte]bool = make(map[byte]bool)
	set[s[slow]] = true

	var res float64 = -1

	for {
		if (slow >= fast) || (fast > len(s)-1) {
			res = math.Max(res, float64(fast-slow))
			break
		}

		if _, exists := set[s[fast]]; exists {
			res = math.Max(res, float64(fast-slow))
			slow += 1
			fast = slow + 1
			for k := range set {
				delete(set, k)
			}
			set[s[slow]] = true
		} else {
			set[s[fast]] = true
			fast += 1
		}
	}

	return int(res)
}