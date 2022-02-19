package main

import (
	"fmt"
)

func main() {
	vertices := make(map[string]int)

	vertices["triangles"] = 2
	vertices["square"] = 3
	vertices["dodecagon"] = 12
	vertices["hexagon"] = 6

	delete(vertices, "hexagon")

	fmt.Println(vertices)
	fmt.Println(vertices["square"])
}
