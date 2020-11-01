# Please Make a PR if you have better approach

if __name__ == '__main__':
    n = int(input())
    li_st = []
    
    for _ in range(0, n):
        li_st.append(int(input()))

    runner_up = max(li_st) - 1
    status = True

    while status:
        for ite in li_st:
            if runner_up == ite:
                print(runner_up)
                status = False
                break
        runner_up -= 1
