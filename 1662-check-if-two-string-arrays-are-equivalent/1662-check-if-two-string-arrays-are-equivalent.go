func arrayStringsAreEqual(word1 []string, word2 []string) bool {
    sb1 := strings.Builder{}
    for _, word := range word1 {
        sb1.WriteString(word)
    }
    
    sb2 := strings.Builder{}
    for _, word := range word2 {
        sb2.WriteString(word)
    }
    
    return sb1.String() == sb2.String()
}