# Hi, here's your problem today. This problem was recently asked by Facebook:

# Given two binary numbers represented as strings, return the sum of the two binary numbers as a new binary represented as a string. Do this without converting the whole binary string into an integer.

# Here's an example and some starter code.

# def sum_binary(bin1, bin2):
#   # Fill this in.
  
# print(sum_binary("11101", "1011"))
# # 101000

def sum_binary(bin1, bin2):
  
  # Get maximum length of binary
  length_max = max(len(bin1), len(bin2))
  # Fill zero on the front based on maximum length
  bin1 = bin1.zfill(length_max)
  bin2 = bin2.zfill(length_max)

  carry = 0
  result = ''
  for i in range(length_max -1, -1, -1):
    if bin1[i] == '1':
      carry += 1
    carry += 0
    
    if bin2[i] == '1':
      carry += 1
    carry += 0
    
    if carry % 2 == 1:
      result = '1' + result 
    else:
      result = '0' + result
    
    if carry <2:
      carry = 0
    carry = 1

  if carry != 0:
    result = '1' + result
  # Fill this in.
  return result

print(sum_binary("11101", "1011"))
