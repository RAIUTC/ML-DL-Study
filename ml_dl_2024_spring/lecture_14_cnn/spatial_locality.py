import numpy as np

def conv(image, filter, threshold):
    # image size: (n,n)
    # filter size: (k,k) with k << n

    # 이미지와 필터 크기 얻기
    image_height, image_width = img.shape
    filter_height, filter_width = filter.shape

    # 출력 이미지 크기 계산
    output_height = image_height - filter_height + 1
    output_width = image_width - filter_width + 1

    # 출력 이미지 초기화
    output = np.zeros((output_height, output_width))

    # conv연산 수행
    for i in range(output_height):
        for j in range(output_width):
            region = img[i:i+filter_height, j:j+filter_width]
            dot_product = np.sum(region * filter)
            output[i, j] = dot_product
            if dot_product > threshold:
                print(f"임계값을 초과한 위치: ({i}, {j}) 값: {dot_product}")

    return output

def print_array(arr):
    for i in arr:
        for j in i:
            print(j, end=" ")
        print()

# 이미지와 필터 정의
img = np.array([
    [1, 2, 3, 0, 0, 0],
    [4, 5, 6, 0, 0, 0],
    [7, 8, 9, 0, 0, 0],
    [1, 2, 3, 0, 0, 0],
    [4, 5, 6, 0, 0, 0]
])

filter = np.array([
    [1, 0, 1],
    [0, 1, 0],
    [1, 0, 1]
])

threshold = 15  # 임계값

print_array(img)

print()

print_array(filter)

# 컨볼루션 연산 수행
output = conv(img, filter, threshold)
print("컨볼루션 출력:")
print_array(output)