from sora import SoraInterpreter

sora_code = """
@sora{
name := "John Doe"
age := 30
height := 5.11
balance := 1000.50

print: User Profile:
print: Name: $name
print: Age: $age
print: Height: $height
print: Balance: $balance

initial_balance := 1000
deposit := 500.50
withdrawal := 200
final_balance := initial_balance + deposit - withdrawal
print: Banking:
print: Initial: $initial_balance
print: After transactions: $final_balance

first_name := "John"
last_name := "Doe"
full_name := first_name + " " + last_name
print: Generated full name: $full_name

# Save user profile
write_file data/profile.txt, Name: $name\nAge: $age\nBalance: $balance
print: Profile saved. Content:
print: $read_file data/profile.txt

write_file data/transactions.txt, Deposit: +$deposit\nWithdrawal: -$withdrawal\nFinal Balance: $final_balance
print: Transaction log:
print: $read_file data/transactions.txt

log: User profile created for $name
log: Transactions processed for account

print: Current variable state:
show_vars
}
"""

interpreter = SoraInterpreter()
result = interpreter.parse_and_execute(sora_code)
print("\nProgram Output:")
print("-" * 50)
print(result)
