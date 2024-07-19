
img = [[0]*6 for i in range(5)]

def print_array(arr):
    for i in arr:
        for j in i:
            print(j, end=" ")
        print()

def conv(image, filter, threshold):
    # image size: (n,n)
    # filter size: (k,k) with k << n

# 이미지 사이즈가 n,n이고 filter 사이즈가 k,k
# 각 k,k크기대로 대응하는 픽셀의 값을 곱해 k,k사이즈의 픽셀들 합을 구해야함

# 비교해서 threshold값을 넘기면 그 위치의 k,k를 반환해야함
    for i in image:
        for j in filter:
            sum = i * j

print_array(img)