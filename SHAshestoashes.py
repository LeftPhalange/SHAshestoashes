import Bruteforce

hash_to_compare = raw_input("Please enter a SHA1 hash to brute force: ")
list_url = raw_input("Please enter a URL for your password list (if left blank, default will be used): ")
choices = raw_input("Select one of the following:\n(1) Simple hash decryption (one term)\n"
                "(2) Salted hashes\n(3) Two terms (complete)\n"
                    "Enter your option here: ")

if list_url == "":
    list_url = \
        "https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/" \
        "10-million-password-list-top-1000000.txt"

b = Bruteforce.Bruteforce (list_url, hash_to_compare)
if choices == "1":
    verbosity = raw_input("Would you like verbosity? (Y/N): ")
    if verbosity == "Y" or verbosity == "y":
        verbosity = True
    else:
        verbosity = False
    b.crack(verbosity, 0)
elif choices == "2":
    salt = raw_input ("Please enter in the hashed salt: ")
    before_or_after = raw_input("Does the salt go before or after the string? (B/A): ")
    if before_or_after == "B":
        before_or_after = False
    else:
        before_or_after = True
    b.crack_with_salt(salt, b.hash, False, 0, before_or_after)
elif choices == "3":
    b.crack_two_terms_complete(b.hash)
else:
    print ("Not a valid option, please run the script again and follow the prompts.")
