array = []
array.append("#include <AaaaOriginalSample.h>")
array.append("#include <BbbbOriginalSample.h>")
array.append("#include <CcccSSample.h>")
array.append("#include <DdddSample.h>")
array.append("#include <EeeeOriginalSample.h>")
array.append("#include <Fffff.h>")
array.append("#include <Gggg.h>")


#[strip]で終端の改行を削除
lines_strip = [line.strip() for line in array]
#print(lines_strip)

print("\r\n[all]")
for line in lines_strip:
    print(line)

#指定文字を含む行を抽出
#startswith()（特定の文字で始まる）
#endswith()（特定の文字で終わる）
#正規表現re.match()

print("\r\n[*Sample.h]")
lines_grep = [line for line in lines_strip if 'Sample.h' in line]
for line in lines_grep:
    print(line)


print("\r\n[exclude OriginalSample.h]")
for line in lines_grep:
    if "OriginalSample.h" not in line:
        print(line)
