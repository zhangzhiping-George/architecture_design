def streamHasher(stream, alogrithm, chunksize=4096):
    #stream = stream.read(chunksize)
    shhash = alogrithm()
    for chunk in iter(stream.read(chunksize)): 
        shhash.update(chunk.encode('utf-8'))
    print(shhash.hexdigest())
    return  shhash.hexdigest()



from hashlib import md5, sha1

#with open('bash_history') as stream:
#    streamHasher(stream, md5)
#
#with open('bash_history') as stream:
#    streamHasher(stream, sha1)
#
    
class cstreamHasher:
    def __init__(self, alogrithm, chunksize=4096):
        self.hash= alogrithm()
        self.chunksize= chunksize 

    def __call__(self, stream):
        '''
        func(args) <==> func.__call__(args)
        '''
        for chunk in iter(stream.read(self.chunksize)):
            self.hash.update(chunk.encode('utf-8'))
        print(self.hash.hexdigest())
        return self.hash.hexdigest()


with open('bash_history') as stream:
    m = cstreamHasher(md5)
    m(stream)

with open('bash_history') as stream:
    s = cstreamHasher(sha1)
    s(stream)

