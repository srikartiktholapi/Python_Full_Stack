mv =memoryview(b"hello")
Bytes = b"hello"
# print(type(Bytes))
# array=[1,2,3,4]
# print(type(array))
# vector=(1,2,3)
# print(type(vector))
# martix=[[1,2,3],[4,5,6]]
# print(type(martix))
# data_set={1,2,3,4}
# print(type(data_set))
# dictionary ={"Name" :"Sri Kartik","Class":"2"}
# print(dictionary)
# print(type(dictionary))
print(mv)
print(Bytes)
print(type(Bytes.decode("utf-8")))
print(Bytes.decode("utf-8"))
print(mv.tobytes())
print(mv.tobytes().decode("utf-8"))
print(type(mv.tobytes().decode("utf-8")))
r=range(5)
print(type(r))
print(list(r))
fs=frozenset([1,2,3,3,2,2])
set1={1,2,3}
set1.add(5)
print(set1)
print(fs)




