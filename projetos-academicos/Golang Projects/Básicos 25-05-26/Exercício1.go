package main

import "fmt"

func main() {

	var nome string
	var idade int
	var peso float64

	fmt.Print("Digite seu nome: ")
	fmt.Scan(&nome)
	fmt.Print("Digite seu idade: ")
	fmt.Scan(&idade)
	fmt.Print("Digite seu peso: ")
	fmt.Scan(&peso)

	fmt.Print("Olá ", nome, " Sua idade é: ", idade, " e seu peso é: ", peso)
}
