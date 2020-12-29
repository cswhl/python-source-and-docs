import pexpect

analyzer = pexpect.spawn('python')

for newWord in ['print(1)', 'print(2)']:
    index = analyzer.expect('>>> ')
    print(f'before:{analyzer.before}')
    print(f'after:{analyzer.after}')
    analyzer.sendline(newWord)
    print(analyzer.read())
