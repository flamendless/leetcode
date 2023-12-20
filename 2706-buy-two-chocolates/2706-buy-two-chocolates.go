func buyChoco(prices []int, money int) int {
    cheaper := math.MaxInt
    cheap := math.MaxInt

    for _, price := range prices {
        if price < cheaper {
            cheap = cheaper
            cheaper = price
        } else if price < cheap {
            cheap = price
        }
    }
    
    rem := money - cheaper - cheap
    if rem < 0 {
        return money
    }
    return rem
}