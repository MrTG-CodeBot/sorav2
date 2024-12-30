from sora import SoraInterpreter

sora_code = """
@sora{

name := "Alice"
print: Hello $name!

age := 25
print: Your age is $age

height := 5.8
print: Your height is $height

x := 10
y := 20
sum := x + y
print: $x + $y = $sum

show_vars

}
"""

interpreter = SoraInterpreter()
result = interpreter.parse_and_execute(sora_code)
print(result)
