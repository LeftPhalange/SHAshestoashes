import hashlib
import urllib2
import os
import time


class Bruteforce:
    def __init__(self, list_url, hash):
        self.list_url = list_url
        self.hash = hash

    def enumerate_list(self):
        return urllib2.urlopen(self.list_url).read().split(os.linesep)

    @staticmethod
    def check_hash_string(string_a, string_b):
        h = hashlib.sha1(string_a)
        h2 = hashlib.sha1(string_b)
        return h.hexdigest() == h2.hexdigest()

    def crack(self, verbosity, time_in_between):
        if time_in_between < 0:
            print ("The operation cannot sleep less than zero seconds. Enter a non-negative integer.")
        count = 0
        if verbosity is True or verbosity is False:
            print ("Cracking " + self.hash + "...")
            token_list = self.enumerate_list()
            for token in token_list:
                if verbosity is True:
                    print (token)
                hex_obj = hashlib.sha1(token)  # new instance of hashlib.sha1()
                new_hex = hex_obj.hexdigest()
                result = self.check_hash_string(self.hash, new_hex)
                if verbosity is True:
                    print ("Attempting hash " + new_hex)
                if result is True:
                    print ("Found it. Decrypted: " + token)
                    print ("It took %d times to get it." % count)
                    return token
                elif result is False and verbosity is True:
                    print ("Attempt failed, moving on...")
                count = count + 1
                if time_in_between > 0:
                    time.sleep(time_in_between)
            if result is False:
                print ("Hash not found. Choose a different word dictionary.")
                return None
        else:
            print ("Wrong type has been used to define the verbosity. Please use True or False.")

    # computationally intensive function
    def crack_with_salt(self, salt, expected_hash, verbosity, time_in_between, concatenate_after):
        b = Bruteforce(self.list_url, salt)
        salt_decrypted = b.crack(verbosity, time_in_between)
        # Salt found, time to enumerate after or before the term
        token_list = self.enumerate_list()  # get list
        count = 0  # we need to keep a track of how many attempts there are
        for term in token_list: # showtime, go through the list
            if concatenate_after is True:  # concatenation rules that the user defined
                new_term = term + salt_decrypted  # after
            else:
                new_term = salt_decrypted + term  # before
            hex_obj = hashlib.sha1(new_term)
            resulting_hash = hex_obj.hexdigest()  # get new hash to compare (as we hash each term in the list, too)
            if resulting_hash == expected_hash:  # found it!
                print("Found it! Term found: %s" % term)
                print("Salted string (decrypted): %s" % new_term)
                print("Took about %d times to find this salted hash." % count)
                return new_term  # return the found salted string
            count = count + 1
            if time_in_between > 0:
                time.sleep(time_in_between)
        print ("Salted hash hasn't been found.")  # well, we tried, this wouldn't be called if we returned a valid term

    # most computationally intensive function, will evaluate a term against the rest of the list...
    # ...and the cycle continues
    def crack_two_terms_complete(self, verbosity, space_in_between, ignore_same_term):  # used with spaces
        count = 0
        for term in self.enumerate_list():  # for loop will go through defined list
            for second_term in self.enumerate_list():
                if verbosity is True and ignore_same_term is False:
                    print ("Comparing %s with %s..." % (term, second_term))
                elif verbosity is True and (ignore_same_term is True and term != second_term):
                    print ("Comparing %s with %s..." % (term, second_term))
                term_to_use = ""
                if space_in_between is True:  # there is a space in between
                    term_to_use = term + " " + second_term # new phrase
                else: # opposite of above
                    term_to_use = term + second_term
                print (term_to_use)
                hex_obj = hashlib.sha1(term_to_use)
                new_term = hex_obj.hexdigest()  # new term hashed
                if ignore_same_term is False:  # same term is evaluated
                    if new_term == self.hash:
                        print ("Found term: %s" % term_to_use)
                        print ("Took about %d times to find this two term hash." % count)
                        return str(term_to_use)
                    else:
                        if verbosity is True:
                            print ("Continuing the loop...")
                elif ignore_same_term is True and term != second_term:  # ignoring if two terms are the same
                    if new_term == self.hash:
                        print ("Found term: %s" % term_to_use)
                        print ("Took about %d times to find this two term hash." % count)
                        return str(term_to_use)
                    else:
                        if verbosity is True:
                            print ("Continuing the loop...")
                count = count + 1
        print ("Two term hash wasn't found.")

    def crack_two_terms_pairs(self, verbosity, space_in_between):  # used with spaces
        count = 0
        term_list = self.enumerate_list()
        for i in range (0, len(term_list) - 1):
            term_to_find = ""
            if space_in_between is True:
                term_to_find = term_list[i] + " " + term_list[i + 1]
            else:
                term_to_find = term_list[i] + term_list[i + 1]
            hex_obj = hashlib.sha1(term_to_find)
            new_hash = hex_obj.hexdigest()
            if new_hash == self.hash:
                print ("Found it: " % term_to_find)
                print ("Found in %d attempts." % count)
            count = count + 1
        print ("Two term hash wasn't found.")

