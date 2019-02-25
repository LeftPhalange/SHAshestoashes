import Bruteforce
import hashlib

list_url = \
    "https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/" \
    "10-million-password-list-top-1000000.txt"

# testing program hash (letmein, after 15 attempts)
b = Bruteforce.Bruteforce(list_url, "b7a875fc1ea228b9061041b7cec4bd3c52ab3ce3")
b.crack (False, 0)

# medium hacker hash (vjhtrhsvdctcegth, after 999967 attempts)
b = Bruteforce.Bruteforce(list_url, "801cdea58224c921c21fd2b183ff28ffa910ce31")
b.crack (False, 0)

# for salted hashes, keep in mind that this works only with known phrases in the list that
# ...are concatenated to the original phrase

# leet hacker hash (slayerharib)
# it took...
# - 216 times to get the salt phrase: slayer
# - 546154 times to use slayer with each phrase enumerated in the list, and we got: slayerharib
b = Bruteforce.Bruteforce(list_url, "ece4bb07f2580ed8b39aa52b7f7f918e43033ea1")
b.crack_with_salt("f0744d60dd500c92c0d37c16174cc58d3c4bdd8e",
                  "ece4bb07f2580ed8b39aa52b7f7f918e43033ea1", False, 0, False)

# graduate student (I am not one, but hey, I'm up for a challenge)

# when instantiating a Bruteforce object for two terms, use the expected hash you
# would get from both terms

b = Bruteforce.Bruteforce(list_url, "34302959e138917ce9339c0b30ec50e650ce6b40")
b.crack_two_terms_pairs(False, True)