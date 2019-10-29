with open('account.txt') as ff:
    for line in ff:
        if line.startswith('421234'):
            line = line.rstrip()
            a = line.split()
            current_amt = a[3]


record=""
with open('account.txt') as fh:
    data=fh.read()
    fh.seek(0)
    for line in fh:
        if line.startswith('421234'):
            line=line.replace(current_amt,'9999')
            record+=line
        else:
            record+=line

print(record)
