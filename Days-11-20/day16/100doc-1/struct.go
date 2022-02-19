package main

import (
	"fmt"
)

type person struct {
	name string
	age  int
	job  string
}

func main() {
	p := person{name: "Tom", age: 27, job: "Con-man"}
	fmt.Println(p)
	fmt.Println(p.job)
}
