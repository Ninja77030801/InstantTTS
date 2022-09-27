# InstantTTS
![Badge](https://badgen.net/badge/instanttts/v1.0.0/blue?icon=github) <br>
A Text to speech machine that also utilizes special commands<br><br>
In this software, all you need to do is type what you need to say. Once you open it, this will come on the console: <br>
`Enter something to say: ` <br>
And you can type something like this: <br>
`Enter something to say: This is so awesome!` <br>

**But wait! That's not all!** <br>
Did you know that there's also a special command? It's known as `*cal`, and it's used to perform mathematical operations! Here's and example below: <br>
```
   Enter something to say: *cal 43 * 23
   989
```
If you want to use mathematical functions like _cos_, then you need to add the `math.` prefix, like this: <br>

```
Enter something to say: *cal math.cos(math.pi / 6)
0.5
```
## If you want to use the .py file directly....
### Using [poetry](https://python-poetry.org/)
If you want to use the source file directly, then what you can do is:
1. Clone the repository directly
2. Access it via your console and type: <br>
`poetry install`<br>
In order to install the dependencies.
3. Then, type in the console: <br>
`poetry run main.py`
   
### Using [pip](https://pip.pypa.io/en/stable/)
1. Clone the repository
2. Access it via the console
3. Type in the console: <br>
`pip install -r requirements.txt` <br>
This will install the dependencies on your computer.
4. Finally, execute it via the command: <br>
`python main.py`
*Voila!* It's finally running on your computer!