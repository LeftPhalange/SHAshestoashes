# SHAshestohashes

This is a project made for my Blockchain & Applications course at Georgia State University, and this is used to crack SHA1 hashes, utilizing a dictionary or password list of some sort, in Python 2.7.

## Getting started

To begin brute forcing SHA1 hashes with this class library, make a new instance of the Bruteforce class:

```b = Bruteforce(list_url, hash)```

list_url: The URL needed to fetch a list or dictionary that could be commonly used words and phrases.

hash: The hash that you want to crack.

You have the following functions in Bruteforce.py:

``enumerate_list(self):`` This is meant to be used internally, but this is going to split strings with the respective newline constant of your operating system, to have Python recognize the needed array.

``crack(self, verbosity):`` This is the main event -- the function used to crack SHA1 hashes using the dictionary URL that you had specified when making a new instance of the Bruteforce object. If found, a count will be printed for how many attempts it took. As with any brute-forcing technology, it's computationally intensive. Returns the decrypted term.

verbosity: Enable or disable verbosity using True or False. When enabled, hashes that are being evaluated are put on display.

``crack_with_salt(self, salt, expected_hash, verbosity, time_in_between, concatenate_after):`` Most computationally intensive function in the library. Decrypts salt term using the list, then enumerates through the list again, concatenating both "decrypted" terms together (under your conditions, before or after) until the expected hash is found. Returns the decrypted term.

salt: The salted phrase (hashed)
expected_hash: The hash you expect to get, this is the original term with the salted term concatenated either after or before.
verbosity: Enables verbosity in that it will show what hex strings are being compared to, and displaying what term is being enumerated in the list.
time_in_between: Time in between evaluating terms. Measured in seconds.

``check_hash_string(self, string_a, string_b):`` Compares hashes.

string_a: String to compare to string_b.
string_b: String to compare to string_a.

``crack_two_terms(verbosity, space_in_between, ignore_same_term):`` Cracking two terms in a list to find the expected hash.

verbosity: Defined by True or False, shows what hashes are being evaluated.
space_in_between: Defined by True or False, is there a space between the term and the other term? True for yes, False for no.
ignore_same_term: Evaluate the same term, True (no) or False (yes)?

Client.py is a great starting point, and is shown how it can be implemented.

## How do I get to use this?

You can transfer Bruteforce.py to your working Python 2.7 environment, in the same directory as the py file you're using.

When used in a client Python script, this is how you can get the Bruteforce object to work:

```import Bruteforce```

In your respective client code, you can instantiate the object like this:

```bf = Bruteforce.Bruteforce(list_url, hash)```

bf can be whatever name you want the object to be in your client class.

### Libraries used (all built-in as of Python 2.7):

urllib2, hexlib, os, time

### Could this be used with other encryption methods (AES, other forms of SHA, for instance)?

This library leaves room for modification to do just that... but SHAshestohashes sounds cool.

### Any password lists I should use?

As a model, I used this password list: https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-1000000.txt

There is indeed room for creativity in that respect.

### For running the solutions in the assignment (Blockchain & Applications)...

Run Client.py with Bruteforce.py present in the same directory. All solutions are posted in there (graduate student has been attempted but this takes a long time to iterate through the list of each phrase, this uses the crack_two_terms function).

In a command-line interpreter (Command Prompt in Windows, Terminal on macOS or another UNIX based operating system), enter the following command, with those files in the working directory:

UNIX:
``python ./Client.py``

Windows:
``C:\path\to\python27\python.exe Client.py``

(C:\ should be your respective drive letter, where the Python binary is. Using Python 2.7 is recommended.)

#### Update (2/25/2019, 7:25 PM)

Since in the instructions, that getting raw input is required, a new Python script is made (SHAshestoashes.py).

Follow the instructions above (respective of UNIX or Windows to use Python to call the script.)