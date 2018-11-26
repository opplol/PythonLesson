import glob
import zipfile

with zipfile.ZipFile('test.zip', 'w') as z:
    # z.write('tar_test_dir')
    # z.write('tar_test_dir/tar_test.txt')
    for f in glob.glob('tar_test_dir/**', recursive=True):
        print(f)
        z.write(f)

with zipfile.ZipFile('test.zip', 'r') as z:
    z.extractall('zzz2')
    with z.open('tar_test_dir/tar_test.txt') as f:
        print(f.read())
