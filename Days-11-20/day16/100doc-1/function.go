package main

import (
	"errors"
	"fmt"
	"math"
)

func main() {
	result := mult(5, 12)
	fmt.Println(result)

	mini, err := sqrt(25)

	if err != nil {
		fmt.Println(err)
	} else {
		fmt.Println(mini)
	}

	neg, err := sqrt(-52)

	if err != nil {
		fmt.Println(err)
	} else {
		fmt.Println(neg)
	}
}

func mult(x int, y int) int {
	return x * y
}

func sqrt(x float64) (float64, error) {
	if x < 0 {
		return 0, errors.New("Undefined for negative numbers")
	}

	return math.Sqrt(x), nil
}
