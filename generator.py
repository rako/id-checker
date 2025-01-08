import random, string, unicodedata

# 入力値が数字かどうか
def number_check(input_data):
    if input_data.isdigit():
        return True
    return False

# ユーザ名の長さが1~15の間かどうか
def length_check(input_data):
    if 1 <= int(input_data) <= 15:
        return True
    return False

# 入力値が半角数字のみで1~15の間に入っているかどうか
def validate_input(input_data):
    if number_check(input_data) == True and length_check(input_data) == True:
        return True
    return False

# ユーザ名の長さを入力させ、バリデーションチェックが通らなければ再度入力させる。英数字は半角、カタカナは全角に変換する。環境依存文字も変換しておく。
username_length = "" #バリデーションチェックのために空文字列を代入
while(validate_input(username_length) == False):
    print("1~15までの好きな長さの数字を入力してください。")
    input_data = input()
    username_length = unicodedata.normalize('NFKC',input_data)
username_length = int(username_length)

# ユーザ名を生成する関数。
def generate_username(username_length):
    username_list = random.choices(string.ascii_lowercase, k=username_length)
    username = ''.join(username_list) #ここをusername = "".join(username)にすると、メソッドが呼ばれたままになる
    return username

username = generate_username(username_length)
print(username)