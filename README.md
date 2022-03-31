Validator for checking files with electrical circuits

This program cheque files with electrical cirtuist. I use three kind of tools. 
*Scanner which cut file for tokens
*Parser cheque tokens with rules
*Validator has debugger(cleaner) which cut off white spaces and everything after "#"

To cheque test file write: py validator.py --input test.net

If you want see file after debuger(clenaer) without comments write: py validator.py --input test.net --clean