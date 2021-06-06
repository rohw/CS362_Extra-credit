def find_targetsum(numberlist, list_size, target_sum):
    target_list = []
    list_size -= 1
    frontindex = 0
    nextindex = list_size

    while nextindex > frontindex:
        if (numberlist[frontindex] + numberlist[nextindex] == target_sum):
            target_list.append(numberlist[frontindex])
            target_list.append(numberlist[nextindex])
            break
        elif (numberlist[frontindex] + numberlist[nextindex] > target_sum):
            nextindex = nextindex - 1
        else:
            frontindex = frontindex + 1
    return target_list


if __name__ == "__main__":
    numberlist = [2, 7, 11, 15]
    list_size = len(numberlist)
    target_sum = 9
    print(find_targetsum(numberlist, list_size, target_sum))
