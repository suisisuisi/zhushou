package main

import (
	"fmt"
	"net"
	"os"
	"bytes"
	"encoding/binary"
	//"log"
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

func Log(v ...interface{}) {
    fmt.Println(v...)
}

const(
	ConstHeader  = "www.redocn.com"
	ConstHeaderLength = 14
	ConstDescLength = 300
	ConstSaveDataLength = 4
)

func Unpack(buffer []byte) []byte {
	length :=uint32(len(buffer))
	var i uint32
	for i=0;i<length;i++{

		if length < i + ConstHeaderLength + ConstDescLength + ConstSaveDataLength{
			break
		}

		headerBufferStart := i
		headerBufferEnd   := i + ConstHeaderLength
		header :=buffer[headerBufferStart:headerBufferEnd]
		if(string(header) != ConstHeader){
			break
		}

		descBufferStart := headerBufferEnd
		descBufferEnd   := descBufferStart + ConstDescLength
		desc := buffer[descBufferStart:descBufferEnd]
		Log("data desc:", string(desc))


		saveDataLengthBufferStart := descBufferEnd
		saveDataLengthBufferEnd   := saveDataLengthBufferStart + ConstSaveDataLength
		var acceptDataLength uint32
		buf := bytes.NewReader(buffer[saveDataLengthBufferStart:saveDataLengthBufferEnd])
		binary.Read(buf,binary.BigEndian,&acceptDataLength)
		//Log("data length:",acceptDataLength)

		saveDataBufferStart := saveDataLengthBufferEnd
		saveDataBufferEnd   := saveDataBufferStart + acceptDataLength
		if saveDataBufferEnd  > length {
			break
		}else{
			Log("receive data:",string(buffer[saveDataBufferStart:saveDataBufferEnd]))
			Log("===============end============================")
			//i += saveDataBufferEnd - 1
			i += ConstHeaderLength + ConstDescLength +  ConstSaveDataLength + acceptDataLength - 1
			fmt.Println(i)
		}
	}
	if i >= length {
		return make([]byte, 0)
	}
	return buffer[i:]
}


func handleConnection(conn net.Conn) {
	buffer := make([]byte, 1024)
	tmpBuffer := make([]byte,0)
	for {
		n, err := conn.Read(buffer)
		if err != nil {
			Log(conn.RemoteAddr().String(), " connection error: ", err)
			return
		}
		tmpBuffer = Unpack(append(tmpBuffer, buffer[:n]...))
	}
}


func CheckError(err error) {
	if err != nil {
		fmt.Fprintf(os.Stderr, "Fatal error: %s", err.Error())
		os.Exit(1)
	}
}