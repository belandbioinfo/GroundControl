set pagination off
set logging file gdb.txt
set logging on
file Test_Vec
b constructors_test
run
commands
bt
continue
end
info breakpoints
r
set logging off
quit
