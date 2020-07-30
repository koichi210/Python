import difflib
#from difflib import SequenceMatcher

str_array = ["コンピューター", "コンピュータ", "コンビーフ", "コンビナート", "コンビ", "コンビニ", "コンビニエンスストア"]

d = difflib.Differ()
diff = d.compare(str_array(0), str_array(1))
print(diff)


# 総当たり
for (str_src, str_dst) in [
        (str_src, str_dst)
        for str_src in str_array
        for str_dst in str_array
        if str_src < str_dst]:
    print(str_src, "<~>", str_dst)

    r = difflib.SequenceMatcher(None, str_src, str_dst).ratio()
#    m = SequenceMatcher(None, str_src, str_dst)
#    r = m.ratio()
    print("match ratio:", r, "\n")
