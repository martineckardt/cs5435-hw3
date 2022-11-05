import siphash

htsize = 2**16

def callhash(hashkey, inval):
    return siphash.SipHash_2_4(hashkey, inval).hash()


def ht_hash(hashkey, inval, htsize):
    return callhash(hashkey, inval) % htsize

#Put your collision-finding code here.
#Your function should output the colliding strings in a list.
def find_collisions(key, num_collisions = 20, htsize = 2**16):
    
    collisions_by_bucket = {}
    random_string = 0

    while (True):
        random_string += 1
        bucket = ht_hash(key,  str(random_string).encode("utf-8"), htsize)

        if bucket in collisions_by_bucket:
            collisions_by_bucket[bucket].append(random_string)
        else:
            collisions_by_bucket[bucket] = [random_string]

        if len(collisions_by_bucket[bucket]) >= num_collisions:
            return collisions_by_bucket[bucket]


#Implement this function, which takes the list of
#collisions and verifies they all have the same
#SipHash output under the given key.
def check_collisions(key, colls):
    pass

if __name__=='__main__':
    #Look in the source code of the app to
    #find the key used for hashing.
    key = b'\x00'*16
    colls = find_collisions(key, 20)
    print(colls)
