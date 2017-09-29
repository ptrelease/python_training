import subprocess

# list the files in one column


def py_echo(ls_args):
    completed = subprocess.Popen(['ls', ls_args], stdout=subprocess.PIPE, )

    # Page 150 of the course notes imply the line below should work.
    # However, I needed to loop though the buffered reader.

    # print(completed.stdout.decode('utf8'))

    for line in completed.stdout:
        print(line.decode('utf8'))


ls_args = input('ls_args: ')
py_echo(ls_args)
