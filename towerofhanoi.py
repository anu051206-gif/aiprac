count = 0
def hanoi(n, source, auxiliary, destination):
    global count
    if n == 1:
        print(source, "->", destination)
        count += 1
        return

    hanoi(n-1, source, destination, auxiliary)
    print(source, "->", destination)
    count += 1
    hanoi(n-1, auxiliary, source, destination)

n = int(input("Enter number of disks: "))
hanoi(n, 'A', 'B', 'C')

print("Total moves : ", count)
