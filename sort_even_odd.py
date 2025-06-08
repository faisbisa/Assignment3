def sort_even_odd_desc(arr):
    even_nums = [x for x in arr if x % 2 == 0]
    odd_nums = [x for x in arr if x % 2 != 0]

    even_nums.sort(reverse=True)
    odd_nums.sort(reverse=True)

    return even_nums + odd_nums


if __name__ == "__main__":
    input_arr = [3, 2, 5, 1, 8, 9, 6]
    output_arr = sort_even_odd_desc(input_arr)
    print(output_arr)
