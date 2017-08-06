package main

import (
    "fmt"
    "os"
    "log"
    "bufio"
)

func main() {
    if len(os.Args) == 1 {
        log.Fatal(os.Args)
    }

    file, err := os.Open(os.Args[1])
    if err != nil {
        log.Fatal(err)
    }
    defer file.Close()

    scanner := bufio.NewScanner(file)

    i := 0
    for scanner.Scan() {
        i += 1
    }
    fmt.Println(i, os.Args[1])
}
