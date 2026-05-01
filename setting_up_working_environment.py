print("Helo World")

#####################
# Numbers and Strings
#####################

print(2 + 3)

type(9)
type(9.0)


# Assignment & Variables

a = 9
a
b = "hello ai era"
b

# Virtual Environments ve Package Management

# Sanal ortamların listelenmesi için:
# conda env list
# Yeni bir sanal ortam oluşturmak için:
# conda create -n myenv python=3.8
# Sanal ortamı etkinleştirmek için:
# conda activate myenv
# Sanal ortamı devre dışı bırakmak için:
# conda deactivate
# Sanal ortamı silmek için:
# conda remove -n myenv --all   
#Yüklü paketlerin listelenmesi
# conda list

# aynı anda birden fazla paket yüklemek için:
# conda install numpy pandas matplotlib
# paket silmek için:
# conda remove numpy    
# belirli bir paketin belirli bir sürümünü yüklemek için:
# conda install numpy=1.19.2
# paketi güncellemek için: 
# conda update numpy
# conda upgrade -all

# pip install pake_adi



# requirements.txt dosyası ya da yaml file olustuma
# conda env export > envinronment.yaml