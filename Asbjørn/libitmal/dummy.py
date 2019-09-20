#!/opt/anaconda3/bin/python
#Points to correct interpreter

def DumDef():
    print("Dumly defined function")

def DumDum():
    DumDef()
    print("Dummy complete")

if __name__ == '__main__':
    DumDum()