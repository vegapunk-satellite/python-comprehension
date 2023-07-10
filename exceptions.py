##Exceptions
##Handling errors and exceptions with 'try' and 'except' blocks
##Assume that user made a typo and wrote 'tes.txt' instead of 'test.txt'
##will return FileNotFoundError
f = open('tes.txt')
#-------------------------------------------------------------------------------------
try:
    f = open('test.txt')
    var = bad_var
except Exception:
    print('Sorry. This file does not exist.')
##Will return our exception instead of FileNotFoundError, but in this case our exception is vague.
##Even though we wrote the correct file name; the code above will return our exception again, caused by the bad variable
#-------------------------------------------------------------------------------------
##Users must be as specific as possible when catching exceptions, 'try except' blocks are meant to catch the errors we expect
try:
    f = open('test.txt')
except FileNotFoundError:
    print('Sorry. This file does not exist.')
#-------------------------------------------------------------------------------------
##Handling multiple exceptions
##Exception priority is always with first except block we wrote in our code. So more specific ones should be listed above
try:
    f = open('test.txt')
    var = bad_var
except FileNotFoundError:
    print('This file does not exist.')
except Exception:
    print('Something went wrong.')
#-------------------------------------------------------------------------------------
##Until now we have always printed out our custom messages
##If we want to just print out the exception they threw:
try:
    f = open('tes.txt')
except FileNotFoundError as e:
    print(e)
except Exception as e:
    print(e)
#-------------------------------------------------------------------------------------
##Else clause
try:
    f = open('test.txt')
except FileNotFoundError as e:
    print(e)
except Exception as e:
    print(e)
else:
    print(f.read())
    f.close()
#-------------------------------------------------------------------------------------
##Finally clause
##Even if our code will throw an exception; finally clause will still be executed.
##So if something must be done regardless of the code's success; we can execute it on finally clause
##like for example closing a database
try:
    f = open('tes.txt')
except FileNotFoundError as e:
    print(e)
except Exception as e:
    print(e)
else:
    print(f.read())
    f.close()
finally:
    print('Been there done that.')
#-------------------------------------------------------------------------------------
##If we want to create and throw our own exceptions:
try:
    f = open('corrupt_file.txt')
    if f.name == 'corrupt_file.txt':
        raise Exception
except FileNotFoundError as e:
    print(e)
except Exception as e:
    print('Check the file.')
else:
    print(f.read())
    f.close()
finally:
    print('Been there done that.')
