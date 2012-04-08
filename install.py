import urllib
import os
print "Downloading PIL library. please wait..."
urllib.urlretrieve ("http://effbot.org/media/downloads/PIL-1.1.7.tar.gz", "PIL-1.1.7.tar.gz")

os.system("""
tar xvf PIL-1.1.7.tar.gz
cd PIL-1.1.7
sudo env ARCHFLAGS="-arch i386" python setup.py install
defaults write com.apple.versioner.python Prefer-32-Bit -bool yes
""")

os.system("""
sudo rm -rf PIL-1.1.7
sudo rm -f PIL-1.1.7.tar.gz
""")