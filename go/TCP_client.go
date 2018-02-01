package main

import (
	"bufio"
	"fmt"
	"net"
	"os"
)

func main() {
	if len(os.Args) != 3 {
		fmt.Println("usage: TCP_client <host> <port>")
		os.Exit(1)
	}

	conn, err := net.Dial("tcp", os.Args[1]+":"+os.Args[2])
	if err != nil {
		fmt.Println("Conection error")
		os.Exit(2)
	}

	defer conn.Close()

	input := bufio.NewReader(os.Stdin)
	var request string
	var reply = make([]byte, 1024)

	for {
		request, _ = input.ReadString('\n')
		conn.Write([]byte(request))
		conn.Read(reply)
		fmt.Print(string(reply))
	}

}
