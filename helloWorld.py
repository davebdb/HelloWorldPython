#!/usr/bin/env python3
# #Day1 of the #100DaysofCode
# This is my first attempt at writing python code and using GitHub as well
# information on main() and __name__ == "__main__" at the following URI
# https://www.guru99.com/learn-python-main-function-with-examples-understand-main.html

def main():
	message='Hello World'
	print(message)
	messageUPPER=message.upper()
	print(messageUPPER)
	messageREPLACED=message.replace('World','Earth')	
	print(messageREPLACED)




if __name__ == "__main__":
    # execute only if run as a script
    main()


