# SoraV2

A lightweight interpreter for the Sora programming language, featuring dynamic typing, variable management, and basic arithmetic operations.

# I understand you're interested in seeing the code for SoraV2. Unfortunately, it's not available for public sharing right now. Because of bugs and some other issues.

## Features

- Dynamic type handling (strings, integers, floats)
- Variable assignment and management
- String interpolation
- Basic arithmetic operations
- Variable state display
- Function support with parameters

## Usage

### Basic Example

```python
from sora import SoraInterpreter

sora_code = """
@sora{
name := "Alice"
age := 25
height := 5.8

print: Name: $name
print: Age: $age
print: Height: $height

show_vars
}
"""

interpreter = SoraInterpreter()
result = interpreter.parse_and_execute(sora_code)
print(result)
```

### Function Example

```python
sora_code = """
@sora{
func calculate_area(length, width)
    area := length * width
    print: Area is: $area
end

call calculate_area(10, 20)
}
"""
```

### String Handling

Strings can be defined with or without quotes:
```python
sora_code = """
@sora{
name := "Alice"

city := New York

print: $name lives in $city
}
"""
```

## Syntax Guide

### Variable Assignment
```
variable_name := value
```

### Printing
```
print: Your message here
```

### Variable Interpolation
```
print: Hello $variable_name
```

### Function Definition
```
func function_name(param1, param2)
    # Function body
end
```

### Function Call
```
call function_name(arg1, arg2)
```

### Show Variables
```
show_vars
```


## Type System

- Strings: Can be defined with or without quotes
- Integers: Whole numbers
- Floats: Decimal numbers
- Automatic type inference based on value

## Features in Detail

### Variable Management
- Dynamic variable creation and updating
- Automatic type inference
- Variable state display with `show_vars`

### String Handling
- Support for quoted and unquoted strings
- String interpolation with `$variable`
- Automatic string type detection

### Arithmetic Operations
- Basic operations: +, -, *, /
- Type-aware calculations
- Automatic numeric type conversion

### Functions
- Parameter support
- Local variable scope
- Return value handling

## Examples

### Basic Arithmetic
```python
@sora{
x := 10
y := 20
sum := x + y
print: Sum is: $sum
}
```

### Function Usage
```python
@sora{
func greet(name, age)
    print: Hello $name, you are $age years old!
end

call greet(Alice, 25)
}
```

## Contributing

Contributions are welcome! Please feel free to submit pull requests.

## License

This project is licensed under the  GNU GENERAL PUBLIC LICENSE - see the LICENSE file for details.
