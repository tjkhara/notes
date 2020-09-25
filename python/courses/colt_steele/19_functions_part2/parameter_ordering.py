# 1. parameters
# 2. *args
# 3. default parameters
# 4. **kwargs

def display_info(a, b, *args, instructor="Colt", **kwargs):
	return [a,b,args, instructor, kwargs]

print(display_info(1,2,3,4,5,6,instructor="TJ", Name="TJ"))