from sora import SoraInterpreter

sora_code = """
@sora{

name := "Alice"
age := 25
height := 5.8

func greet(person)
    print: Hello $person!
end

func add_numbers(x, y)
    sum := x + y
    print: Sum of $x and $y is $sum
end

func process_data(name, age)
    print: Processing data for $name
    next_age := age + 1
    print: Next year age will be $next_age
end

call greet(name)
call add_numbers(10, 20)
call process_data(name, age)

show_vars
}
"""

interpreter = SoraInterpreter()
result = interpreter.parse_and_execute(sora_code)
print("\nProgram Output:")
print("-" * 50)
print(result)
