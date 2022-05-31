# #Restful APIs
# import requests
# import json

# # response = requests.get("https://api.stackexchange.com//2.3/badges?order=desc&sort=rank&site=stackoverflow")
# # print(response.json())


# response = requests.get("https://jsonplaceholder.typicode.com/posts")
# print(response.json())

# #post method
# {
# 	"userid": 1'
# 	"id": 1,
# 	"title": "python class",
# 	"body": "This is a pythin class"
# }


#Assert statement
def get_average(scores):
	assert len(scores) != 0, "The list is empty"
	return sum(scores) / len(scores)

score1 = [54, 24, 44, 66]
print("Average of score 1: ", get_average(score1))

score2 = []
print("Average of score 1: ", get_average(score2))

print("William")