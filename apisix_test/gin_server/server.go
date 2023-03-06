package main

import (
    "github.com/gin-gonic/gin"
	"flag"
)


func GetResult(c *gin.Context) {

    c.JSON(200, gin.H{
        "result": "hello gin server!",
    })
}

func main() {
	var port string
	flag.StringVar(&port, "p", "7777", "port")
	flag.Parse()

    r := gin.Default()

    // 普通用户接口
    r.GET("/get_result_http", GetResult)

    r.Run(":" + port) 

}

