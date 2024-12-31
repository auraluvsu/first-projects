package main

import "fmt"

func main() {
	myarray := []string{"Nasir", "Imani", "Gary", "Natalie"}
	mynewarray := append(myarray, "Ramiah")
	fmt.Println("My array length is: ", len(myarray))
	fmt.Println("My new array length is: ", len(mynewarray))
}
