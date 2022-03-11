package main

import (
    	"fmt"
    	"os"
	"strings"
	"bufio"
	"strconv"
)

func check(e error) {
    if e != nil {
        panic(e)
    }
}


func main() {
	position := make(map[string]int)
	position["direction"] = 0
	position["depth"] = 0

	file, err := os.Open("input.txt")
	check(err)
	defer file.Close()

	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		line := scanner.Text()
		fields := strings.Fields(line)
		command := fields[0]
		amount, err := strconv.Atoi(fields[1])
		check(err)

		fmt.Print(command)
		fmt.Print(" ", amount, "\n")
	}
}
