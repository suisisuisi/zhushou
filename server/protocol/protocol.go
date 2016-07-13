package protocol

import (
	"bytes"
	"encoding/binary"
)

//整形转换成字节
func IntToBytes(n int) []byte {
	x := int32(n)

	bytesBuffer := bytes.NewBuffer([]byte{})
	binary.Write(bytesBuffer, binary.BigEndian, x)
	return bytesBuffer.Bytes()
}

//字节转换成整形
func BytesToInt(b []byte) int {
	bytesBuffer := bytes.NewBuffer(b)

	var x int32
	binary.Read(bytesBuffer, binary.BigEndian, &x)

	return int(x)
}

//4个字节转换成整形
func Bytes4ToInt(b []byte) int {
	xx := make([]byte, 4)
	if len(b) == 2 {
		xx = []byte{b[0], b[1], 0, 0}
	} else {
		xx = b
	}

	m := len(xx)
	nb := make([]byte, 4)
	for i := 0; i < 4; i++ {
		nb[i] = xx[m - i - 1]
	}
	bytesBuffer := bytes.NewBuffer(nb)

	var x int32
	binary.Read(bytesBuffer, binary.BigEndian, &x)

	return int(x)
}

func Unpack()