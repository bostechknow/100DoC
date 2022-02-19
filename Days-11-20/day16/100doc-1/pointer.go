package main

import (
	"fmt"
)

func main() {
	z := 42
	fmt.Println("real:", z)
	fmt.Println("pointer:", &z)

	r := 51
	fmt.Println("real:", r)
	inc(&r)
	fmt.Println("inc'ed:", r)
}

func inc(x *int) {
	*x++
}
