import time

# 1 & 7. For loop 1-100 and Range with steps
# Real-world: Generating even-numbered IDs or skipping steps in a sequence
print("---1 & 7 Numbers 1-100 & Range with Steps ---")
for i in range(1, 101):
    print(i, end=" " if i % 10 != 0 else "\n")

print("\nEven numbers from 0 to 20:")
for even in range(0, 21, 2):
    print(even, end=" ")
print("\n")


# 2. While loop for a countdown timer
# Real-world: A rocket launch or a microwave timer
print("--- 2. Countdown Timer ---")
timer = 5
while timer > 0:
    print(f"Commencing launch in... {timer}")
    time.sleep(0.5) # Reduced for demo purposes
    timer -= 1
print("Liftoff! 🚀\n")


# 4 & 8. Break, Continue, and Conditions
# Real-world: A security scanner skipping safe files but stopping at a virus
print("--- 4 & 8. Break/Continue with Conditions ---")
files = ["doc1", "doc2", "VIRUS", "doc3", "corrupt", "doc4"]

for file in files:
    if file == "corrupt":
        print(f"  [!] Skipping {file}...")
        continue # Skip to next file
    if file == "VIRUS":
        print(f"  [X] System Alert: {file} found! Shutting down.")
        break # Exit loop entirely
    print(f"  Scanning {file}...")
print()


# 5. Iterate over string characters
# Real-world: Validating password strength or formatting text
print("--- 5. String Iteration ---")
user_input = "Admin123"
print(f"Analyzing password: {user_input}")
for char in user_input:
    print(f"  Character check: {char}")
print()


# 6. Multiplication table
# Real-world: Building a basic calculator or data grid
print("--- 6. Multiplication Table (7s) ---")
num = 7
for i in range(1, 11):
    result = num * i
    print(f"{num} x {i} = {result}")