alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
            's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
def cypher(start_text, shift_amount, cypher_direction):
    stop_text = ""
    if cypher_direction == "decode":
            shift_amount *= -1
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = (position + shift_amount) % len(alphabet)
            stop_text += alphabet[new_position]
        else:
            stop_text+= char
            
    print(f"The {direction}d text is {stop_text}")       
#from art import logo
#print(logo)
cypher(start_text= text, shift_amount= shift, cypher_direction= direction)        
#instead of using the %len(value) function we can also add another alphabet list
 