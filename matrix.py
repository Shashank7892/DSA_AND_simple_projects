def negative(grid):
    print(grid)
    
    lo,hi=0,len(grid)-1
    count=0
    
    while lo<=hi:
        print(grid[lo])
        low,high=0,len(grid[lo])-1
        print(low)
        print(high)
        while low<=high:
            mid=(low+high)//2
            guess=grid[lo][mid]
            print(guess)
            
            if guess < 0:
                high=mid-1
            else:
                low=mid+1
        count+=len(grid[lo])-low
        lo+=1
    print(count)

grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
negative(grid)
