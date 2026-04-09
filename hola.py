def distances_from_average(test_list):
    popo=sum(test_list)/len(test_list)
    result=[]
    for i in test_list:
        distance=i-popo
        result.append(distance)
    return [result]
print(distances_from_average([1,2,10,13]))