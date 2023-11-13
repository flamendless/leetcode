func sortVowels(s string) string {
    VOWELS := map[rune]bool{
        'A':true,
        'E':true,
        'I':true,
        'O':true,
        'U':true,
        'a':true,
        'e':true,
        'i':true,
        'o':true,
        'u':true,
    }
    
    vowels := []rune{}
    for _, ch := range s {
        _, exists := VOWELS[ch]
        if exists {
            vowels = append(vowels, ch)
        }
    }
    
    sort.Slice(vowels, func(i, j int) bool {
        return vowels[i] < vowels[j]
    })
    
    runes := []rune(s)
    var j int
    for i, v := range runes {
        _, exists := VOWELS[v]
        if exists {
            runes[i]= vowels[j]
            j++
        }
    }
    
    return string(runes)
}