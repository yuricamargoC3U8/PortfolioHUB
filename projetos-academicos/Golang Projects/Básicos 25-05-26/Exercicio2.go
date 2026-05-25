package main

import "fmt"

func main() {
	var base2 float64
	var altura2 float64

	fmt.Print("Digite a base: ")
	fmt.Scan(&base2)
	fmt.Print("Digite a altura: ")
	fmt.Scan(&altura2)
	fmt.Print("A área é: ", base2*altura2)
}
