package main

import (
	"fmt"
	"net"
	"os"
	"bytes"
	"encoding/binary"
)

func main() {
	netListen, err := net.Listen("tcp", "test.mm.com:5800")
	CheckError(err)

	defer netListen.Close()

	Log("Waiting for clients")
	for {
		conn, err := netListen.Accept()
		if err != nil {
			continue
		}

		Log(conn.RemoteAddr().String(), " tcp connect success")
		go handleConnection(conn)
	}
}


func Unpack(buffer []byte) []byte {
	length :=uint32(len(buffer))
	var i uint32
	for i=0;i<length;i++{
		if length< 318{
			break
		}
		acceptDataHead :=buffer[i:i+14]
		if(string(acceptDataHead) != "www.redocn.com"){
			break
		}
		acceptDataDesc:=buffer[i+14:i+314]
		Log("receive data desc:", string(acceptDataDesc))

		var acceptDataLength uint32
		buf := bytes.NewReader(buffer[i+314:i+318])
		binary.Read(buf,binary.BigEndian,&acceptDataLength)
		Log("receive data length:",acceptDataLength)

		if(length<318+acceptDataLength){
			break
		}else{
			Log("receive data length:",string(buffer[i+318:i+318+acceptDataLength]))
			Log("===============end============================")
			return  buffer[i+318+acceptDataLength:]
		}
	}
	if i == length {
		return make([]byte, 0)
	}
	return buffer[i:]
}

func handleConnection(conn net.Conn) {
	buffer := make([]byte, 1024)
	//tmpBuffer := make([]byte,0)
	//readerChannel := make(chan []byte, 1024)
	for {
		n, err := conn.Read(buffer)
		if err != nil {
			Log(conn.RemoteAddr().String(), " connection error: ", err)
			return
		}
		Log("receive data:",string(buffer[n:]))
		//tmpBuffer = Unpack(append(tmpBuffer, buffer[:n]...))
	}
}


 
	fmt.Println(v...)
}

func CheckError(err error) {
	if err != nil {
		fmt.Fprintf(os.Stderr, "Fatal error: %s", err.Error())
		os.Exit(1)
	}
}