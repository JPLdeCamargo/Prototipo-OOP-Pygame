output = {'up': True, 'down': True, 'right': False, 'left': False, 'quit': False}
output2 = {'up': False, 'd1wn': False, 'right': False, 'left': False, 'quit': False}
for output1, value1 in output.items():
    for output_2, value2 in output2.items():
        if output1 == output_2:
            output2[output_2] = value1
print(output)
print(output2)