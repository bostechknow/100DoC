package main

import (
	"fmt"
)

func main() {
	a := [5]int{7, 2, 9, 11, 15}
	b := []int{2, 19, 5, 21}
	b = append(b, 7)
	fmt.Println(a, b)
}
