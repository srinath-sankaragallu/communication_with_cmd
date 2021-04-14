import subprocess
print("started .....")
p = subprocess.Popen(['python', 'contin.py'] , stdin = subprocess.PIPE,stdout = subprocess.PIPE , shell = True )
for i in [1,2,4,9,2,'e']:
    p.stdin.write(bytes(f"{i}\n",'utf-8'))
    p.stdin.flush() #helps in clearning the stdin buffer
    k = p.stdout.readline()
    print(k)
p.stdin.close()    
m = p.communicate()[0]
print(m)
