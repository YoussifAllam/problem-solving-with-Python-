def bubbleSort(arr):
	n = len(arr)
	
	for i in range(n):
		swapped = False

		for j in range(0, n-i-1):

			if arr[j] > arr[j+1]:
				arr[j], arr[j+1] = arr[j+1], arr[j]
				swapped = True
		if (swapped == False):
			break



if __name__ == "__main__":
	n=int(input())
	list1=list(input().split())
	list1=[int(i) for i in list1]
	bubbleSort(list1)

	for i in range(len(list1)):
		print("%d" % list1[i], end=" ")


