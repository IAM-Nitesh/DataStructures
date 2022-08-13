if __name__ == '__main__':
    N = int(input())
    out_list = []

    for _ in range(N):
        command, *command_list = input().split()
        inp_list = [int(i) for i in command_list]

        if command == "insert":
            out_list.insert(inp_list[0], inp_list[1])
            # print(out_list)
        elif command == "print":
            print(out_list)
        elif command == "remove":
            out_list.remove(inp_list[0])
            # print(out_list)
        elif command == "append":
            out_list.append(inp_list[0])
            # print(out_list)
        elif command == "sort":
            out_list.sort()
            # print(out_list)
        elif command == "pop":
            out_list.pop()
            # print(out_list)
        elif command == "reverse":
            out_list.reverse()
            # print(out_list)


'''
12
insert 0 5
insert 1 10
insert 0 6
print
remove 6
append 9
append 1
sort
print
pop
reverse
print
'''