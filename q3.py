def are_anagrams(s1, s2):
    return sorted(s1.lower()) == sorted(s2.lower())

# Example usage
print(are_anagrams("Listen", "Silent"))  
print(are_anagrams("Hello", "World")) 