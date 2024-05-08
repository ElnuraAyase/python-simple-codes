#1 any input form the user to be printed
print( "enter todo:")
user_outp = input()
print(user_outp)
# 2 same but different way 
prompt =  "enter todo: "
user1_txt = input(prompt) 
print(user1_txt) 

# 3make multile todos
user_prompt = "enter todo: "
#do not put number before variable
todo1= input(user_prompt) 
todo2 = input(user_prompt)
todo3 = input(user_prompt)
#creating list for mult variables
todos = [todo1, todo2, todo3]
print(todos) 

# add info about type of value associated with variable (string,int or list ,etc.) 
print(type(todos) # output will be <class 'list>
print (type(user_prompt) # output will be < class  'str'>

#automate the todos
