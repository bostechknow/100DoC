package main

import (
	"fmt"
)

func main() {
	for i := 0; i < 10; i++ {
		fmt.Println(i)
	}

	n := 0

	for n < 5 {
		fmt.Println(n)
		n++
	}

	arr := []string{"Hi", "Hello", "Sup"}

	for index, value := range arr {
		fmt.Println("index:", index, "value:", value)
	}

	m := make(map[string]string)
	m["a"] = "alpha"
	m["x"] = "xray"
	m["m"] = "mike"

	for key, value := range m {
		fmt.Println("key:", key, "value:", value)
	}
}
