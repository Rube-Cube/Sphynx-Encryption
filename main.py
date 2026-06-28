'''main program loop'''
import encrypt_decrypt
from encrypt_decrypt import encrypt_char, decrypt_char, hash_string
import priming
from priming import prime_hash

def construct_prompt(prompt: str, type: int=0) -> str:
    if type == 0:
        return prompt + ":\n    "
    if type == 1:
        return prompt + "\n    "

def main():
    prompts = {
        encrypt_char: "encrypt",
        decrypt_char: "decrypt",
    }
    while True:
        #get input
        desired_function = input(construct_prompt("What would you like to do?\nEncrypt: e\nDecrypt: d\nQuit: q", 1))
        if desired_function == "q":
            print("Thank you for trying my encryption, please give feedback!")
            break
        if desired_function == "e":
            functionality = encrypt_char
        if desired_function == "d":
            functionality = decrypt_char

        func_text = input(construct_prompt(f"Enter text to {prompts[functionality]}"))
        key = input(construct_prompt("Enter key"))
        primed_key = prime_hash(key)
        print(f"{prompts[functionality]}ed message:\n{hash_string(func_text, primed_key, functionality)}")

        input("Press 'Enter' to continue...")
        print("\n\n\n")




if __name__ == "__main__":
    main()