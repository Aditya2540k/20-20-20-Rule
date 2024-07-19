
# 20-20-20 Rule

It’s a handy tool you can use at work or at home to reduce eye strain. Designed to reduce eye strain, the 20-20-20 rule says that every 20 minutes of screen time, you should look away at something at least 20 feet away for 20 seconds. These regular screen breaks give your eyes some rest and helps to prevent eye strain. In this tool you can also change Work and Rest duration.


## 🛠️Installation
1. Before Downloading this program Make sure Python is installed on your system. You can download it from [python.org](https://www.python.org/).
2. [Download](https://codeload.github.com/Aditya2540k/20-20-20_Rule/zip/refs/tags/v1.0.0?token=AXKHIXAOPPXKG4FW7KKRHDLGS7MJS) The Letest 'Source Code' Zip File From Releases.

3. After Downloading the Zip file Extract This in your preferred folder.

4. To do it right click on the zip file and select 'Extract All' Then select the folder where you want to place it's files.

5. Locate the 20-20-20.py file's folder in Command prompt. 

6. Install the required dependencies: 

(Run this in Command Prompt)
```bash
pip install -r requirements.txt
```

(These steps are only necessary for the first time to run the program)
## 🚀Usages
### Execute The Code

#### 1. Using Command Prompt:
```bash
python 20-20-20.py
```

#### 2. Using File Explorer:
1. To do this Locate '20-20-20.py' file in your File Explorer.
2. Select the file. Then "RightClick", Some option will appear.
3. Move mouse cursor to 'Open with' option then select Python.
4. Now you can Execute this program just by double clicking on '20-20-20.py' file.

#### 3. Run This on Startup
1. To do this Locate 20-20-20.py file in your File Explorer.

2. Select the file. Then "RightClick" Some option will appear.

3. Click on "Show more options".

4. Click "Creat shortcut". This will creats '20-20-20.py-Shortcut' file.

5. Press Window+R on Keyboard. Then type "shell:startup" and Enter.This will open Startup folder. 
6. Move '20-20-20.py-Shortcut' file to this 'Startup' folder.
7. Now this program will run automatically when you turn on your computer.

## ⚙️Configure Work And Rest Duration
1. Open 'config.ini' file using any text editor. Which must be look like this(By Default)
👇👇👇👇
```bash
[Work]
Minutes = 20

[Rest]
Minutes = 0
Seconds = 20
```
2. If u want to change the work duration just change this work minutes value to any minutes. Like for example you want to change 20 minutes work duration to 40 minutes just replace 20 with 40 👇👇👇
```bash
[Work]
Minutes = 40

[Rest]
Minutes = 0
Seconds = 20
```
3. You can also change Rest duration. To do it just change Rest minutes value 0 to any minutes Also at a same time change Rest Seconds value to 0. For example if i want to change Rest duration to 5 minutes:
👇👇👇👇
 ```bash
[Work]
Minutes = 20

[Rest]
Minutes = 5
Seconds = 0
```
4. To change Rest duration to 30 Second. Replace Rest Seconds value with 30 also keep the Minutes value as 0.
👇👇👇👇
```bash
[Work]
Minutes = 20

[Rest]
Minutes = 0
Seconds = 30
```
