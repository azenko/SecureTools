# SecureTools
Some Security Tools i Develop for need

In that Git you gonna found some file to help you in Security for now here is the following tools list :
- generateMd5List.py - Generate a list of the MD5 file in a folder and his subfolder
- integrityChecker.py - Return a list of file who haven't their Hash in a Hash list (Actually support only MD5)
- phpBackdoorRegexChecker.py - Check and return a list of file infected with the Backdoor PHP Small.M (https://www.microsoft.com/security/portal/threat/encyclopedia/Entry.aspx?Name=Backdoor:PHP/Small.M)

# Usage :
[generateMd5List.py]
root@debian:~# python generateMd5List.py <folderToScan>
[integrityChecker.py]
root@debian:~# integrityChecker.py  <folderToScan> <hashList> <hashType>
or if you want to show FileName and MD5 :
root@debian:~# integrityChecker.py  <folderToScan> <hashList> <hashType> true
[phpBackdoorRegexChecker.py]
root@debian:~# python phpBackdoorRegexChecker.py <folderToScan>

# Like this
If you like this you can send me a coffee via BitCoin :D
Here my address : 13e1gqXHQ2yje2FPh21cQ8Mc3RCKXqay93
