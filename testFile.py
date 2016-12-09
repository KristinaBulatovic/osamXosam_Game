import pickle

file = open("bazaTina.db", "rb")

sve = pickle.load(file)
print(len(sve[1]))
print(len(sve[2]))

file.close()

"""
s = [1,2,3,4,5]

if(s.startswith([1,2,3])):
    print("Da")
"""
