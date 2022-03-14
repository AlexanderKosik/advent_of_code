package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func check(e error) {
	if e != nil {
		panic(e)
	}
}

func processCommand(pos *map[string]int, cmd string, amount int) {
	if cmd == "forward" {
		(*pos)["forward"] += amount
	} else if cmd == "down" {
		(*pos)["depth"] += amount
	} else if cmd == "up" {
		(*pos)["depth"] -= amount
	}
}

func main() {
	position := make(map[string]int)
	position["forward"] = 0
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
		processCommand(&position, command, amount)
	}
	r := position["forward"] * position["depth"]
	fmt.Println("Result is", r)
}
