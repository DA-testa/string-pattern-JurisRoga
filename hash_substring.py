# python3

def read_input():
    # this function needs to aquire input both from keyboard and file
    # as before, use capital i (input from keyboard) and capital f (input from file) to choose which input type will follow
    parbaude = input().strip()
    if parbaude == "I":
        pattern = input().rstrip()
        text = input().rstrip()
    elif parbaude == "F":
        vieta = input().strip()
        with open ("tests/" + vieta, mode= 'r') as fails:
            pattern = fails.readline().rstrip()
            text = fails.readline().rstrip()
    
    # after input type choice
    # read two lines 
    # first line is pattern 
    # second line is text in which to look for pattern 
    
    # return both lines in one return
    
    # this is the sample return, notice the rstrip function
    return (pattern, text)

def print_occurrences(output):
    # this function should control output, it doesn't need any return
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    Q = 256
    B = 13
    pattern_hash = 0
    text_hash = 0
    occurances = []
    # this function should find the occurances using Rabin Karp alghoritm 
    pattern_len = len(pattern)
    text_len = len(text)
    for i in range(pattern_len):
        pattern_hash = (pattern_hash * Q + ord(pattern[i])) % B
        text_hash = (text_hash * Q + ord(text[i])) % B
    
    for i in range(text_len - pattern_len+1):
        if pattern_hash == text_hash:
            if pattern == text[i:i+pattern_len]:
                occurances.append(i)
        if i < text_len - pattern_len:
            text_hash = (Q* (text_hash-ord(text[i])* pow(Q, pattern_len-1, B)) + ord(text[i+pattern_len])) % B
            if text_hash < 0:
                text_hash += B
    # and return an iterable variable
    return occurances


# this part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

