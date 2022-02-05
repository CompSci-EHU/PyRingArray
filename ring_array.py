class RingArray:
    def __init__(self, length: int, pad=None):
        self.__ring = [pad] * length
        self.__length = len(self.__ring)
        self.__pointer = 0  # head
        self.__iter_pointer = -1  # reset state = -1

    def __len__(self) -> int:
        return self.__length  # len(RingArray)

    def set(self, item):
        self.__ring[self.__pointer] = item
        self.__pointer = (self.__pointer + 1) % self.__length  # increment ring pointer

    def get(self, idx: int):
        return self.__ring[idx % self.__length]

    def update(self, item, idx: int):
        self.__ring[idx % self.__length] = item

    def insert(self, position: int, item):
        self.__ring.insert(position, item)
        self.__pointer += 1
        self.__length = len(self.__ring)

    def ring_gen(self, limit: int):
        while self.__iter_pointer < limit - 1:
            self.__iter_pointer += 1
            yield self.get(self.__iter_pointer)

    def reset_gen(self):
        self.__iter_pointer = -1


if __name__ == "__main__":
    print('Initialising 26 element RingArray')
    r = RingArray(26, pad="!")
    print(f"Length of ring is: {len(r)}")
    print('Setting elements as a - z')
    for _ in range(ord("a"), ord("z") + 1):
        r.set(chr(_))
    r.reset_gen()
    print('Iterating though elements in ring array (2 * len)')
    for index, _ in enumerate(r.ring_gen(len(r) * 2)):
        print(f"{index}: {_}")

    print(f"Get element 2 of {len(r)}: {r.get(2)}")
    print(f"Get element 2238949272 of {len(r)}: {r.get(2238949272)}")
    
    print('\nNew ring!')
    r = RingArray(5, pad=0)

    print(f'{list(r.ring_gen(len(r)))} len: {len(r)}')
    r.reset_gen()
    print(f'Insert 1 into position 3')
    r.insert(3, 1)  # ring grows
    print(f'{list(r.ring_gen(len(r)))} len: {len(r)}')
    exit()
