user={
    1:'abu',
    2:'said'

}

print(user.get(2))
print(user)
print('said' in user.keys())
print('said' in user.values())
print('said' in user.items())
print('said' in user)

print("print keys: ")
for key,values in user.items():
    print(user[key])