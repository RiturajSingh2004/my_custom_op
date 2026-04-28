import torch
import my_custom_op

x = torch.tensor([1.0, 2.0, 3.0])
y = my_custom_op.my_op(x)

print(y)  # tensor([3., 6., 11.])