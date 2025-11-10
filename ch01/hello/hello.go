package main

import (
	"fmt"
	"math/rand"
)

func main() {
	rand.Seed(1)

	dice := rand.Intn(6) + 1
	fmt.Print(dice)
}
