# Mencari Substring yang Cocok dalam Sebuah String

# get matching substrings in string
# initializing string
test_str = "GFG is a good website"

# initializing potential substrings
tes_list = ['GFG', 'site', 'CS', 'Geeks', 'tutorial']

# Mencetak string asli
print('The original string is: ' + test_str)

# Mencetak list potensial substring
print('The original list is: ' + str(tes_list))

# Menggunakan list comprehension
# Mencari substring yang cocok dalam string
res = [sub for sub in tes_list if sub in test_str]

# Mencetak hasilnya
print('The list of found substrings: ' + str(res))
