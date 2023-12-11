func findSpecialInteger(arr []int) int {
	l := 0
    r := len(arr)/4
	
	for arr[l] != arr[r] {
        l++
        r++	
	}
    return arr[l]
}