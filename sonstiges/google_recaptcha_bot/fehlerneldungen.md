#Fehlermeldungen und umgang

#### `SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape`
meint das die `\` in 
`browser = webdriver.Chrome("C:\Users\danie\AppData\Local\Programs\Python\chromedriver_win32\chromedriver.exe")`

3 Methoden sind möglich:

1. convert normal string to raw string:
`webdriver.Chrome(r"C:\Users\danie\AppData\Local\Programs\Python\chromedriver_win32\chromedriver.exe")`

[]()

2. `\` zu `/`
`webdriver.Chrome("C:/Users/danie/AppData/Local/Programs/Python/chromedriver_win32/chromedriver.exe")`

[]()

3. `\` escapen
`webdriver.Chrome("C:\\Users\\danie\\AppData\\Local\\Programs\\Python\\chromedriver_win32\\chromedriver.exe")`
