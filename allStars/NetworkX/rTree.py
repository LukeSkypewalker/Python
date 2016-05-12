from rtree import index



idx = index.Index()

left, bottom, right, top = (1.0, 1.0, 1.0, 1.0)
idx.insert(1, (left, bottom, right, top))
idx.insert(2, (4, 4, 4, 4))
res=list(idx.nearest((3, 3, 3, 3), 1))
print(res)





