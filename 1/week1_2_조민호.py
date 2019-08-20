N = int(input())

word_pair_dict ={}

for i in range(N):
    one_line = input()
    word_pair = one_line.split()
    word_pair_dict[word_pair[1]] = word_pair[0]

encoded_line = input()
encoded_words = encoded_line.split()
two_layer_decoded_word_list = []
for encoded_word in encoded_words:
    one_layer_decoded_word= word_pair_dict[encoded_word]
    two_layer_decoded_word = ''
    for character in one_layer_decoded_word:
        decoded_char = chr(ord(character)-1) if(character!='a') else 'z'
        two_layer_decoded_word += decoded_char
    two_layer_decoded_word_list.append(two_layer_decoded_word)

print(' '.join(two_layer_decoded_word_list))
    





