my_global_var = 1


def my_function():
    # Only accessible within my_function()
    my_local_var = 2
    print(my_global_var)
    print(my_local_var)
my_block_var = 1

for _ in range(10):
    # Accessible anywhere
    my_block_var += my_global_var
    print()
print(my_global_var)
print(my_block_var)
my_function()
