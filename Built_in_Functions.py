abs(x) # 絶対値
all(iterable) # 全ての要素が真ならTrue(もしくは空なら)
any(iterable) # いずれの要素が真ならTrue
ascii(object) # asciiコードに変換
bin(x) # 整数を指定進数文字列に変換
bool([x]) # ブール値を返す
breakpoint(*args, **kws) # 呼び出された箇所からデバッガに移行
bytearray() # 新しいバイト配列を返す
bytes() # bytesオブジェクトを返す
callable() # 
chr(i) # Unicode コードポイントが整数iである文字を表す文字列を返す
@classmethod # メソッドをクラスメソッドへ変換
compile() # コードオブジェクト or ASTオブジェクトへ変換
complex() # 複素数を返す
delattr() # setattr()の親戚
dict(**kwargs) # 新しい辞書を作成
dir() # ローカルスコープにある名前のリストを返す
divmod() # 商と剰余を返す
enumerate() # enumerateオブジェクトを返す
eval() # 文字列とオプションの引数 globals, localsをとる
exec() # Pythonコードの動的な実行をサポート
filter() # iterableの要素の内functionが真で返すものでイテレータを構築
float(x) # 浮動小数点数を返す
format() # 書式化された表現に変換
frozenset() # 新しいfrozenset　オブジェクトを返す
getattr() # 指定された属性の値を返す
globals() # グローバルシンボルテーブルを表す辞書を返す
hasattr() # 文字列がオブジェクトの属性名の一つであった場合True
hash() # オブジェクトのハッシュ値を返す
help() # 組み込みヘルプシステムを起動
hex() # 整数を変換
id() # オブジェクトの識別値を返す
input() # 引数を指定すると末尾の改行を除いて標準出力→入力から1行読み込み文字列に変換(末尾の改行を除く)
int() # 整数型する、基数を変更可能
isinstance() # 引数が一定の条件ならTrueを返す？
issubclass() # 上記に似ている
iter() # イテレータオブジェクトを返す
len() # オブジェクトの長さ(要素を返す)
list() # リスト化
locals() # ローカルシンボルテーブルを表す辞書を更新して返す
map() # functionを結果を返しながらiterableの全ての要素に適応するイテレータを返す
max() # 最大値を返す keyを指定できる
memoryview() # 与えられたオブジェクトから作られた"メモリービュー"オブジェクトを返す
min() # 最小値を返す keyを指定できる
next() # iteratorメソッドを呼び出すことで、次の要素を取得
object() # 特徴を持たない新しいオブジェクト返す
oct(x) # 整数を8進数文字列に変換
open() # ファイルを開く
ord(c) # 1文字のUnicode文字を表す文字列に対して、Unicodeコードポイントを表す整数を返す
pow() # 対数関数とかに使う？
print() # 出力
property() # property属性を返す
range() # 回数など指定？
repr() # オブジェクトの印字可能な表現を含む文字列を返す
reversed() # 要素を逆順に取り出すイテレータを返す
round() # numberの小数部をndigists桁に丸めた値を返す
set() # 新しいsetオブジェクトを返す　集合
setattr() # getattr()の相方
slice() # スライスオブジェクトを返す
sorted() # 要素を並び変えた新たなリストを返す
@staticmethod # メソッドを静的メソッドに変換
str() # str型を返す
sum() # 合計値
super() # 継承
tuple() # タプル型を返す
type() # objectの型を返す
vars() # 属性を返す
zip() # イテラブルから要素を集めたイテレータを作る

