######################
# Data Structures
######################

# Veri Yapılarına giriş ve hızlı özet
# Sayılar : int, float, complex
# Karakter Dizileri Strings : str 
# Boolean (True-False) : bool
# Listeler :list
# Sözlükler : dict
# Demetler : tuple
# Kümeler : set


# Sayılar : integer
x = 46
type(x)

# Sayılar : float
pi = 3.14
type(pi)

# Sayılar : complex
a = 2j
type(a) 

# Karakter Dizileri Strings : str
greeting = "Hello, World!"                 
type(greeting)
# Boolean (True-False) : bool
is_raining = False
type(is_raining)                

# Listeler :list            
my_list = [1, 2, 3, "four", 5.0]
type(my_list)
# Sözlükler : dict (sözlükler key-value pear yaposona sahip olmalı)
my_dict = {"name": "Alice", "age": 30, "city": "New York"}
type(my_dict)

# Demetler : tuple
my_tuple = (1, 2, 3, "four", 5.0)
type(my_tuple)


# Kümeler : set
my_set = {1, 2, 3, "four", 5.0}
type(my_set)        


############################
# Sayılar (Numbers): int, float, complex
############################

a = 5 
b = 10.5

a * 3 
a / 7 
a * b / 10
a ** 2


# Tipleri değiştirmek 
int(b)
float(a)
int(a * b / 10)

c = a * b / 10 
int(c)


# Karakter Dizileri (Strings): str

print("John")
print('John')

"John's book"

# Çok Satırlı Karakter Dizileri

long_str = """" Veri Yapıları Python'da veri yapıları, verileri düzenlemek ve depolamak için kullanılan özel türlerdir. Python'da yaygın olarak kullanılan veri yapıları şunlardır:
    1. Listeler (Lists): Değiştirilebilir, sıralı koleksiyonlardır. Farklı türdeki öğeleri içerebilirler.
    2. Sözlükler (Dictionaries): Anahtar-değer çiftlerini depolayan değiştirilebilir koleksiyonlardır. Anahtarlar benzersiz olmalıdır.
    3. Demetler (Tuples): Değiştirilemez, sıralı koleksiyonlardır. Farklı türdeki öğeleri içerebilirler.
    4. Kümeler (Sets): Değiştirilebilir, sırasız koleksiyonlardır. Benzersiz öğeler içerirler.
    5. Sayılar (Numbers): int, float, complex gibi sayısal veri türlerini içerirler.
    6. Karakter Dizileri (Strings): str türünde metin verilerini depolarlar."""

# Karakter Dizilerinin Elemanlarına Erişmek

name = "Name"
name[0]
name[3]
name[0:3]

# String içerisinde karakter Sorgulamak


long_str

"veri" in long_str

# String Metodları

dir(int)
dir(str)

## len metodu: Karakter dizisinin uzunluğunu döndürür.

name = " John Doe"
type(name)
len(name)
type(len)



# Bir yapının method mu fonksiyon mu olduğunu nasıl anlarız
# methodlar bir yapıya bağlı olarak çalışır, fonksiyonlar ise bağımsız olarak çalışır. class yapısı içinde tanımlanmış fonksiyonlara method denir. methodlar bir nesneye bağlı olarak çalışır ve o nesnenin özelliklerine erişebilirler. fonksiyonlar ise herhangi bir nesneye bağlı olmadan çalışabilirler ve genellikle genel amaçlı işlemler için kullanılırlar. methodlar genellikle bir nesnenin davranışını tanımlarken, fonksiyonlar daha genel işlemleri gerçekleştirmek için kullanılırlar.
#methodlar class içinde tanımlanır fonksiyonlar ise bağımsız


"miul".isupper() # methodlar parantezle çağrılır
"miul".upper() # methodlar parantezle çağrılır
"MIUL".isupper() # methodlar parantezle çağrılır        

# type(upper) # fonksiyonlar parantezsiz çağrılır

# replace metodu: Bir karakter dizisindeki belirli bir alt dizeyi başka bir alt dizeyle değiştirmek için kullanılır.

sentence = "The quick brown fox jumps over the lazy dog."
new_sentence = sentence.replace("fox", "cat")
print(new_sentence)  # Output: The quick brown cat jumps over the lazy dog.

#split metodu: Bir karakter dizisini belirli bir ayırıcıya göre bölmek için kullanılır.     
sentence = "The quick brown fox jumps over the lazy dog."
words = sentence.split(" ")
print(words)  # Output: ['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog.']    

# Listeler (Lists): Değiştirilebilir, sıralı koleksiyonlardır. Farklı türdeki öğeleri içerebilirler.    
my_list = [1, 2, 3, "four", 5.0]
type(my_list)
notes = [1,2,3,4,5]
type(notes)
not_nam = ["Ali", "Veli",1,2,3, 4.5,True,[1,2,3,], "Ayşe", "Fatma"]
len(not_nam)
not_nam[0]
not_nam[7][1]
not_nam[0] = "Ahmet"
not_nam[0]



# Liste Metodları list methods:
dir(not_nam)
 
len(not_nam)
#append metodu: Bir listeye yeni bir öğe eklemek için kullanılır.
not_nam.append("Mehmet")
len(not_nam)
#insert metodu: Bir listeye belirli bir konumda yeni bir öğe eklemek için kullanılır.
not_nam.insert(2, "Ayşe")
not_nam


#sözlükler (dictionaries): Anahtar-değer çiftlerini depolayan değiştirilebilir koleksiyonlardır. Anahtarlar benzersiz olmalıdır. sırasızdırlar 3.7 sürümünden sonra sıralı hale gelmiştirler kapsayıcıdırlar
my_dict = {"name": "Alice", "age": 30, "city": "New York"}
type(my_dict)
my_dict["name"]
my_dict["age"]      


# key sorgulama
"name" in my_dict #true
"country" in my_dict #false
my_dict["country"] = "USA"              
my_dict.keys()
my_dict.values()
my_dict.items()
my_dict["name"] = "Bob" # value güncelleme
my_dict["country"] = "Canada" # value güncelleme
my_dict


# Demetler (Tuples): Değiştirilemez, sıralı koleksiyonlardır. Farklı türdeki öğeleri içerebilirler. listelerle benzer ama değiştirilemezler
my_tuple = (1, 2, 3, "four", 5.0)
type(my_tuple)
my_tuple[0]
my_tuple[3]
my_tuple[0] = 10 # hata verir çünkü demetler değiştirilemez         

# Kümeler (Sets): Değiştirilebilir, sırasız koleksiyonlardır. Benzersiz öğeler içerirler. sırasızdırlar
my_set = {1, 2, 3, "four", 5.0}
type(my_set)
my_set.add("six") # kümeye yeni bir öğe eklemek için kullanılır
my_set.remove(2) # kümeden bir öğeyi kaldırmak için kullanılır
my_set 


# difference(): iki kümenin farkı
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}
set_a.difference(set_b)  # Output: {1, 2}
difference = set_a.difference(set_b)
print(difference)  # Output: {1, 2}

#symmetric_difference(): iki kümenin simetrik farkı
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}        

set_a.symmetric_difference(set_b)  # Output: {1, 2, 5, 6}
symmetric_difference = set_a.symmetric_difference(set_b)
print(symmetric_difference)  # Output: {1, 2, 5,

# intersection(): iki kümenin kesişimi
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}
set_a.intersection(set_b)  # Output: {3, 4}

# union(): iki kümenin birleşimi
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}
set_a.union(set_b)  # Output: {1, 2, 3, 4, 5, 6}

# isdisjoint(): iki kümenin kesişimi boş mu
set_a = {1, 2, 3, 4}
set_b = {5, 6, 7, 8}    
set_a.isdisjoint(set_b)  # Output: True

# issubset(): bir kümenin diğer bir kümenin alt kümesi mi           
set_a = {1, 2, 3}
set_b = {1, 2, 3, 4, 5}
set_a.issubset(set_b)  # Output: True       
set_b.issubset(set_a)  # Output: False

# issuperset(): bir kümenin diğer bir kümenin kapsayıcısı       
set_a = {1, 2, 3, 4, 5}
set_b = {1, 2, 3}
superset = set_a.issuperset(set_b)  # Output: True 