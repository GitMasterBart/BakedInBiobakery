#!/usr/bin/expect

spawn ssh -p 4235 bengels@bioinf.nl
expect "password"
send "4pRGxj7(\r"

expect "$"
send "ls"
expect "$ "
#send "exit\r"
#interact
