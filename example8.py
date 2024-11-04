# remember you can find multple python libraries on pippy.org

from pathlib import Path

# Create a Path object
path = Path()
for i in path.glob('*.*'):
    print(i)
