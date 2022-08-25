Python 3.10.6 (tags/v3.10.6:9c7b4bd, Aug  1 2022, 21:53:49) [MSC v.1932 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

================ RESTART: C:/Users/Designer Sneha/assiment 1.py ================
3.10.6 (tags/v3.10.6:9c7b4bd, Aug  1 2022, 21:53:49) [MSC v.1932 64 bit (AMD64)]

================ RESTART: C:/Users/Designer Sneha/assiment 1.py ================
3.10.6 (tags/v3.10.6:9c7b4bd, Aug  1 2022, 21:53:49) [MSC v.1932 64 bit (AMD64)]
hello,Python
## learning Python
print("learning python")
learning python
""" learning pythone
a
b
c
"""
' learning pythone\na\nb\nc\n'
a=5
b=6
c=7
print(a)
5
print(a,b,c sep='\n')
SyntaxError: invalid syntax
print(a,b,c, sep='\n')
5
6
7
a="like 35"
b= ture
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    b= ture
NameError: name 'ture' is not defined. Did you mean: 'tuple'?
c=("mysirG")
d=5.46
e=3+4j
type(a,b,c,d,e, sep='n\')
     
SyntaxError: unterminated string literal (detected at line 1)
type(a,b,c,d,e, sep'n\')
     
SyntaxError: unterminated string literal (detected at line 1)
type(a,b,c,d,e, sep"n\")
     
SyntaxError: unterminated string literal (detected at line 1)
type(a)
     
<class 'str'>
type(a,b,c,d,e)
     
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    type(a,b,c,d,e)
TypeError: type() takes 1 or 3 arguments
type(a,b,c)
     
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    type(a,b,c)
TypeError: type.__new__() argument 2 must be tuple, not int
type(a)
     
<class 'str'>
type(b)
     
<class 'int'>
type(c)
     
<class 'str'>
type(d)
     
<class 'float'>
type(e)
     
<class 'complex'>
a=5
     
b=5
     
id(a)
     
2433356071280
id(b)
     
2433356071280
a="neha singh"
     
b=6.55
     
c=3+4j
     
d=5
     
type(a)
     
<class 'str'>
id(a)
     
2433362125616
type(b)
     
<class 'float'>
id(b)
     
2433391750416
type(c)
     
<class 'complex'>
id(c)
     
2433391753904
type(d)
     
<class 'int'>
id(d)
     
2433356071280

============================================================== RESTART: C:/Users/Designer Sneha/A2.py =============================================================
Traceback (most recent call last):
  File "C:/Users/Designer Sneha/A2.py", line 2, in <module>
    print(x)
NameError: name 'x' is not defined

============================================================== RESTART: C:/Users/Designer Sneha/A2.py =============================================================
Traceback (most recent call last):
  File "C:/Users/Designer Sneha/A2.py", line 2, in <module>
    print(x.A1)
NameError: name 'x' is not defined

============================================================== RESTART: C:/Users/Designer Sneha/A2.py =============================================================
Traceback (most recent call last):
  File "C:/Users/Designer Sneha/A2.py", line 2, in <module>
    print(A1.x)
AttributeError: module 'A1' has no attribute 'x'

============================================================== RESTART: C:/Users/Designer Sneha/A2.py =============================================================
Traceback (most recent call last):
  File "C:/Users/Designer Sneha/A2.py", line 2, in <module>
    print(A1.x)
AttributeError: module 'A1' has no attribute 'x'

============================================================== RESTART: C:/Users/Designer Sneha/A2.py =============================================================
Traceback (most recent call last):
  File "C:/Users/Designer Sneha/A2.py", line 2, in <module>
    print(A1.x)
AttributeError: module 'A1' has no attribute 'x'

============================================================== RESTART: C:/Users/Designer Sneha/A2.py =============================================================
Traceback (most recent call last):
  File "C:/Users/Designer Sneha/A2.py", line 2, in <module>
    print(A1.x)
AttributeError: module 'A1' has no attribute 'x'

==================== RESTART: C:/Users/Designer Sneha/A2.py ====================
Traceback (most recent call last):
  File "C:/Users/Designer Sneha/A2.py", line 1, in <module>
    importA1
NameError: name 'importA1' is not defined

==================== RESTART: C:/Users/Designer Sneha/A1.py ====================
Traceback (most recent call last):
  File "C:/Users/Designer Sneha/A1.py", line 1, in <module>
    import A1
  File "C:\Users/Designer Sneha\A1.py", line 2, in <module>
    print(A1.kwlist)
AttributeError: partially initialized module 'A1' has no attribute 'kwlist' (most likely due to a circular import)

==================== RESTART: C:/Users/Designer Sneha/A1.py ====================
Traceback (most recent call last):
  File "C:/Users/Designer Sneha/A1.py", line 1, in <module>
    import A2
  File "C:\Users/Designer Sneha\A2.py", line 1, in <module>
    importA1
NameError: name 'importA1' is not defined

==================== RESTART: C:/Users/Designer Sneha/A1.py ====================
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
help()

Welcome to Python 3.10's help utility!

If this is your first time using Python, you should definitely check out
the tutorial on the internet at https://docs.python.org/3.10/tutorial/.

Enter the name of any module, keyword, or topic to get help on writing
Python programs and using Python modules.  To quit this help utility and
return to the interpreter, just type "quit".

To get a list of available modules, keywords, symbols, or topics, type
"modules", "keywords", "symbols", or "topics".  Each module also comes
with a one-line summary of what it does; to list the modules whose name
or summary contain a given string such as "spam", type "modules spam".

help> keywords

Here is a list of the Python keywords.  Enter any keyword to get more help.

False               class               from                or
None                continue            global              pass
True                def                 if                  raise
and                 del                 import              return
as                  elif                in                  try
assert              else                is                  while
async               except              lambda              with
await               finally             nonlocal            yield
break               for                 not                 

help> variables
No Python documentation found for 'variables'.
Use help() to get the interactive help utility.
Use help(str) for help on the str class.

help> function
No Python documentation found for 'function'.
Use help() to get the interactive help utility.
Use help(str) for help on the str class.

help> version
No Python documentation found for 'version'.
Use help() to get the interactive help utility.
Use help(str) for help on the str class.

help> modules

Please wait a moment while I gather a list of all available modules...


Warning (from warnings module):
  File "C:\Program Files\Python310\lib\site-packages\_distutils_hack\__init__.py", line 33
    warnings.warn("Setuptools is replacing distutils.")
UserWarning: Setuptools is replacing distutils.
A1                  antigravity         heapq               runscript
A2                  argparse            help                sched
__future__          array               help_about          scrolledlist
__main__            assiment 1          history             search
_abc                ast                 hmac                searchbase
_aix_support        asynchat            html                searchengine
_ast                asyncio             http                secrets
_asyncio            asyncore            hyperparser         select
_bisect             atexit              idle                selectors
_blake2             audioop             idle_test           setuptools
_bootsubprocess     autocomplete        idlelib             shelve
_bz2                autocomplete_w      imaplib             shlex
_codecs             autoexpand          imghdr              shutil
_codecs_cn          base64              imp                 sidebar
_codecs_hk          bdb                 importlib           signal
_codecs_iso2022     binascii            inspect             site
_codecs_jp          binhex              io                  smtpd
_codecs_kr          bisect              iomenu              smtplib
_codecs_tw          browser             ipaddress           sndhdr
_collections        builtins            itertools           socket
_collections_abc    bz2                 json                socketserver
_compat_pickle      cProfile            keyword             sqlite3
_compression        calendar            lib2to3             squeezer
_contextvars        calltip             linecache           sre_compile
_csv                calltip_w           locale              sre_constants
_ctypes             cgi                 logging             sre_parse
_ctypes_test        cgitb               lzma                ssl
_datetime           chunk               macosx              stackviewer
_decimal            cmath               mailbox             stat
_distutils_hack     cmd                 mailcap             statistics
_elementtree        code                mainmenu            statusbar
_functools          codecontext         marshal             string
_hashlib            codecs              math                stringprep
_heapq              codeop              mimetypes           struct
_imp                collections         mmap                subprocess
_io                 colorizer           modulefinder        sunau
_json               colorsys            msilib              symtable
_locale             compileall          msvcrt              sys
_lsprof             concurrent          multicall           sysconfig
_lzma               config              multiprocessing     tabnanny
_markupbase         config_key          neha                tarfile
_md5                configdialog        netrc               telnetlib
_msi                configparser        nntplib             tempfile
_multibytecodec     contextlib          nt                  test
_multiprocessing    contextvars         ntpath              textview
_opcode             copy                nturl2path          textwrap
_operator           copyreg             numbers             this
_osx_support        crypt               opcode              threading
_overlapped         csv                 operator            time
_pickle             ctypes              optparse            timeit
_py_abc             curses              os                  tkinter
_pydecimal          dataclasses         outwin              token
_pyio               datetime            parenmatch          tokenize
_queue              dbm                 pathbrowser         tooltip
_random             debugger            pathlib             trace
_sha1               debugger_r          pdb                 traceback
_sha256             debugobj            percolator          tracemalloc
_sha3               debugobj_r          pickle              tree
_sha512             decimal             pickletools         tty
_signal             delegator           pip                 turtle
_sitebuiltins       difflib             pipes               turtledemo
_socket             dis                 pkg_resources       types
_sqlite3            distutils           pkgutil             typing
_sre                doctest             platform            undo
_ssl                dynoption           plistlib            unicodedata
_stat               editor              poplib              unittest
_statistics         email               posixpath           urllib
_string             encodings           pprint              util
_strptime           ensurepip           profile             uu
_struct             enum                pstats              uuid
_symtable           errno               pty                 venv
_testbuffer         faulthandler        py_compile          warnings
_testcapi           filecmp             pyclbr              wave
_testconsole        fileinput           pydoc               weakref
_testimportmultiple filelist            pydoc_data          webbrowser
_testinternalcapi   fnmatch             pyexpat             window
_testmultiphase     format              pyparse             winreg
_thread             fractions           pyshell             winsound
_threading_local    ftplib              query               wsgiref
_tkinter            functools           queue               xdrlib
_tracemalloc        gc                  quopri              xml
_uuid               genericpath         random              xmlrpc
_warnings           getopt              re                  xxsubtype
_weakref            getpass             redirector          zipapp
_weakrefset         gettext             replace             zipfile
_winapi             glob                reprlib             zipimport
_xxsubinterpreters  graphlib            rlcompleter         zlib
_zoneinfo           grep                rpc                 zoneinfo
abc                 gzip                run                 zoomheight
aifc                hashlib             runpy               zzdummy

Enter any module name to get more help.  Or, type "modules spam" to search
for modules whose name or summary contain the string "spam".

help> 

You are now leaving help and returning to the Python interpreter.
If you want to ask for help on a particular object directly from the
interpreter, you can type "help(object)".  Executing "help('string')"
has the same effect as typing a particular string at the help> prompt.

help()

Welcome to Python 3.10's help utility!

If this is your first time using Python, you should definitely check out
the tutorial on the internet at https://docs.python.org/3.10/tutorial/.

Enter the name of any module, keyword, or topic to get help on writing
Python programs and using Python modules.  To quit this help utility and
return to the interpreter, just type "quit".

To get a list of available modules, keywords, symbols, or topics, type
"modules", "keywords", "symbols", or "topics".  Each module also comes
with a one-line summary of what it does; to list the modules whose name
or summary contain a given string such as "spam", type "modules spam".

help> modules

Please wait a moment while I gather a list of all available modules...

A1                  antigravity         heapq               runscript
A2                  argparse            help                sched
__future__          array               help_about          scrolledlist
__main__            assiment 1          history             search
_abc                ast                 hmac                searchbase
_aix_support        asynchat            html                searchengine
_ast                asyncio             http                secrets
_asyncio            asyncore            hyperparser         select
_bisect             atexit              idle                selectors
_blake2             audioop             idle_test           setuptools
_bootsubprocess     autocomplete        idlelib             shelve
_bz2                autocomplete_w      imaplib             shlex
_codecs             autoexpand          imghdr              shutil
_codecs_cn          base64              imp                 sidebar
_codecs_hk          bdb                 importlib           signal
_codecs_iso2022     binascii            inspect             site
_codecs_jp          binhex              io                  smtpd
_codecs_kr          bisect              iomenu              smtplib
_codecs_tw          browser             ipaddress           sndhdr
_collections        builtins            itertools           socket
_collections_abc    bz2                 json                socketserver
_compat_pickle      cProfile            keyword             sqlite3
_compression        calendar            lib2to3             squeezer
_contextvars        calltip             linecache           sre_compile
_csv                calltip_w           locale              sre_constants
_ctypes             cgi                 logging             sre_parse
_ctypes_test        cgitb               lzma                ssl
_datetime           chunk               macosx              stackviewer
_decimal            cmath               mailbox             stat
_distutils_hack     cmd                 mailcap             statistics
_elementtree        code                mainmenu            statusbar
_functools          codecontext         marshal             string
_hashlib            codecs              math                stringprep
_heapq              codeop              mimetypes           struct
_imp                collections         mmap                subprocess
_io                 colorizer           modulefinder        sunau
_json               colorsys            msilib              symtable
_locale             compileall          msvcrt              sys
_lsprof             concurrent          multicall           sysconfig
_lzma               config              multiprocessing     tabnanny
_markupbase         config_key          neha                tarfile
_md5                configdialog        netrc               telnetlib
_msi                configparser        nntplib             tempfile
_multibytecodec     contextlib          nt                  test
_multiprocessing    contextvars         ntpath              textview
_opcode             copy                nturl2path          textwrap
_operator           copyreg             numbers             this
_osx_support        crypt               opcode              threading
_overlapped         csv                 operator            time
_pickle             ctypes              optparse            timeit
_py_abc             curses              os                  tkinter
_pydecimal          dataclasses         outwin              token
_pyio               datetime            parenmatch          tokenize
_queue              dbm                 pathbrowser         tooltip
_random             debugger            pathlib             trace
_sha1               debugger_r          pdb                 traceback
_sha256             debugobj            percolator          tracemalloc
_sha3               debugobj_r          pickle              tree
_sha512             decimal             pickletools         tty
_signal             delegator           pip                 turtle
_sitebuiltins       difflib             pipes               turtledemo
_socket             dis                 pkg_resources       types
_sqlite3            distutils           pkgutil             typing
_sre                doctest             platform            undo
_ssl                dynoption           plistlib            unicodedata
_stat               editor              poplib              unittest
_statistics         email               posixpath           urllib
_string             encodings           pprint              util
_strptime           ensurepip           profile             uu
_struct             enum                pstats              uuid
_symtable           errno               pty                 venv
_testbuffer         faulthandler        py_compile          warnings
_testcapi           filecmp             pyclbr              wave
_testconsole        fileinput           pydoc               weakref
_testimportmultiple filelist            pydoc_data          webbrowser
_testinternalcapi   fnmatch             pyexpat             window
_testmultiphase     format              pyparse             winreg
_thread             fractions           pyshell             winsound
_threading_local    ftplib              query               wsgiref
_tkinter            functools           queue               xdrlib
_tracemalloc        gc                  quopri              xml
_uuid               genericpath         random              xmlrpc
_warnings           getopt              re                  xxsubtype
_weakref            getpass             redirector          zipapp
_weakrefset         gettext             replace             zipfile
_winapi             glob                reprlib             zipimport
_xxsubinterpreters  graphlib            rlcompleter         zlib
_zoneinfo           grep                rpc                 zoneinfo
abc                 gzip                run                 zoomheight
aifc                hashlib             runpy               zzdummy

Enter any module name to get more help.  Or, type "modules spam" to search
for modules whose name or summary contain the string "spam".

help> modules

Please wait a moment while I gather a list of all available modules...

A1                  antigravity         heapq               runscript
A2                  argparse            help                sched
__future__          array               help_about          scrolledlist
__main__            assiment 1          history             search
_abc                ast                 hmac                searchbase
_aix_support        asynchat            html                searchengine
_ast                asyncio             http                secrets
_asyncio            asyncore            hyperparser         select
_bisect             atexit              idle                selectors
_blake2             audioop             idle_test           setuptools
_bootsubprocess     autocomplete        idlelib             shelve
_bz2                autocomplete_w      imaplib             shlex
_codecs             autoexpand          imghdr              shutil
_codecs_cn          base64              imp                 sidebar
_codecs_hk          bdb                 importlib           signal
_codecs_iso2022     binascii            inspect             site
_codecs_jp          binhex              io                  smtpd
_codecs_kr          bisect              iomenu              smtplib
_codecs_tw          browser             ipaddress           sndhdr
_collections        builtins            itertools           socket
_collections_abc    bz2                 json                socketserver
_compat_pickle      cProfile            keyword             sqlite3
_compression        calendar            lib2to3             squeezer
_contextvars        calltip             linecache           sre_compile
_csv                calltip_w           locale              sre_constants
_ctypes             cgi                 logging             sre_parse
_ctypes_test        cgitb               lzma                ssl
_datetime           chunk               macosx              stackviewer
_decimal            cmath               mailbox             stat
_distutils_hack     cmd                 mailcap             statistics
_elementtree        code                mainmenu            statusbar
_functools          codecontext         marshal             string
_hashlib            codecs              math                stringprep
_heapq              codeop              mimetypes           struct
_imp                collections         mmap                subprocess
_io                 colorizer           modulefinder        sunau
_json               colorsys            msilib              symtable
_locale             compileall          msvcrt              sys
_lsprof             concurrent          multicall           sysconfig
_lzma               config              multiprocessing     tabnanny
_markupbase         config_key          neha                tarfile
_md5                configdialog        netrc               telnetlib
_msi                configparser        nntplib             tempfile
_multibytecodec     contextlib          nt                  test
_multiprocessing    contextvars         ntpath              textview
_opcode             copy                nturl2path          textwrap
_operator           copyreg             numbers             this
_osx_support        crypt               opcode              threading
_overlapped         csv                 operator            time
_pickle             ctypes              optparse            timeit
_py_abc             curses              os                  tkinter
_pydecimal          dataclasses         outwin              token
_pyio               datetime            parenmatch          tokenize
_queue              dbm                 pathbrowser         tooltip
_random             debugger            pathlib             trace
_sha1               debugger_r          pdb                 traceback
_sha256             debugobj            percolator          tracemalloc
_sha3               debugobj_r          pickle              tree
_sha512             decimal             pickletools         tty
_signal             delegator           pip                 turtle
_sitebuiltins       difflib             pipes               turtledemo
_socket             dis                 pkg_resources       types
_sqlite3            distutils           pkgutil             typing
_sre                doctest             platform            undo
_ssl                dynoption           plistlib            unicodedata
_stat               editor              poplib              unittest
_statistics         email               posixpath           urllib
_string             encodings           pprint              util
_strptime           ensurepip           profile             uu
_struct             enum                pstats              uuid
_symtable           errno               pty                 venv
_testbuffer         faulthandler        py_compile          warnings
_testcapi           filecmp             pyclbr              wave
_testconsole        fileinput           pydoc               weakref
_testimportmultiple filelist            pydoc_data          webbrowser
_testinternalcapi   fnmatch             pyexpat             window
_testmultiphase     format              pyparse             winreg
_thread             fractions           pyshell             winsound
_threading_local    ftplib              query               wsgiref
_tkinter            functools           queue               xdrlib
_tracemalloc        gc                  quopri              xml
_uuid               genericpath         random              xmlrpc
_warnings           getopt              re                  xxsubtype
_weakref            getpass             redirector          zipapp
_weakrefset         gettext             replace             zipfile
_winapi             glob                reprlib             zipimport
_xxsubinterpreters  graphlib            rlcompleter         zlib
_zoneinfo           grep                rpc                 zoneinfo
abc                 gzip                run                 zoomheight
aifc                hashlib             runpy               zzdummy

Enter any module name to get more help.  Or, type "modules spam" to search
for modules whose name or summary contain the string "spam".

help> 

You are now leaving help and returning to the Python interpreter.
If you want to ask for help on a particular object directly from the
interpreter, you can type "help(object)".  Executing "help('string')"
has the same effect as typing a particular string at the help> prompt.
help(keywords)
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    help(keywords)
NameError: name 'keywords' is not defined. Did you mean: 'keyword'?
help("keywords)
     
SyntaxError: unterminated string literal (detected at line 1)
help("keywords")
     

Here is a list of the Python keywords.  Enter any keyword to get more help.

False               class               from                or
None                continue            global              pass
True                def                 if                  raise
and                 del                 import              return
as                  elif                in                  try
assert              else                is                  while
async               except              lambda              with
await               finally             nonlocal            yield
break               for                 not                 


============================================================== RESTART: C:/Users/Designer Sneha/A0.py =============================================================
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
Traceback (most recent call last):
  File "C:/Users/Designer Sneha/A0.py", line 2, in <module>
    print(A1.x)
AttributeError: module 'A1' has no attribute 'x'

============================================================== RESTART: C:/Users/Designer Sneha/A1.py =============================================================

============================================================== RESTART: C:/Users/Designer Sneha/A0.py =============================================================
Traceback (most recent call last):
  File "C:/Users/Designer Sneha/A0.py", line 2, in <module>
    print(A1.x)
AttributeError: module 'A1' has no attribute 'x'

============================================================== RESTART: C:/Users/Designer Sneha/A0.py =============================================================
Traceback (most recent call last):
  File "C:/Users/Designer Sneha/A0.py", line 1, in <module>
    import a1
ModuleNotFoundError: No module named 'a1'

============================================================= RESTART: C:/Users/Designer Sneha/abc.py =============================================================
Traceback (most recent call last):
  File "C:/Users/Designer Sneha/abc.py", line 2, in <module>
    print(abcd.x)
AttributeError: module 'abcd' has no attribute 'x'

============================================================= RESTART: C:/Users/Designer Sneha/abc.py =============================================================
Traceback (most recent call last):
  File "C:/Users/Designer Sneha/abc.py", line 2, in <module>
    print(abcd.a)
AttributeError: module 'abcd' has no attribute 'a'

============================================================= RESTART: C:/Users/Designer Sneha/abcd.py ============================================================

============================================================= RESTART: C:/Users/Designer Sneha/abc.py =============================================================
5

============================================================== RESTART: C:/Users/Designer Sneha/A0.py =============================================================
neha singh
neha singh
SyntaxError: invalid syntax
from datetime import datetime

============================================================== RESTART: C:/Users/Designer Sneha/A0.py =============================================================
2022-08-25 00:33:03.656640
