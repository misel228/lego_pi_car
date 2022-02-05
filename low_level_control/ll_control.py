def init():
    print("Initializing motors")
    talkto(M1)
    setleft()
    on()
    setpower(0)
    talkto(M3)
    on()
    setpower(0)
    print("Done")


def forward(power):
    talkto(M1)
    setleft()
    on()
    setpower(power)
    talkto(M3)
    setright()
    on()
    setpower(power)

def backward(power):
    talkto(M1)
    setright()
    on()
    setpower(power)
    talkto(M3)
    setleft()
    on()
    setpower(power)

def f(): 
    while True:
        print(read(A1))
        forward(read(A1))
        time.sleep(1)

def sd():
    talkto(M1)
    off()
    talkto(M3)
    off()

def s():
    talkto(M1)
    setpower(0)
    talkto(M3)
    setpower(0)
    
init()
