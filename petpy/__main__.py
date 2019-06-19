import sys

from .petpy import gardner

def main():
    vp = sys.argv[1]
    print(gardner(float(vp)))
    return


if __name__ == "__main__":
    main()
