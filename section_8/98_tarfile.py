import tarfile

with tarfile.open('test.tar.gz', 'w:gz') as tr:
    tr.add('tar_test_dir')

with tarfile.open('test.tar.gz', 'r:gz') as tr:
    # tr.extractall(path='test_tar')
    with tr.extractfile('tar_test_dir/sub_dir/sub_test.txt') as f:
        print(f.read())