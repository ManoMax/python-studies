# coding: utf-8
# Aluno: Gabriel Max Vieira Matos
# Matricula: 117110060
# Questão: Sequeeze - CC (UFCG)

def squeeze(nums):
	for i in range(len(nums)-1, 0, -1):
		if nums[i] == nums[i-1]:
			nums.pop(i)
	return nums

nums = [3, 1, 1, 1, 4, 7, 3, 3, 2, 7]
assert squeeze(nums) == [3, 1, 4, 7, 3, 2, 7]
