# Flagr
## Flag System for Text Based Command

Flagr is a Python flag system manager for text commands, 
either CLI, Discord bots or other.

- Some Assembly Required
- Easy to Start Using After
- 🔥 Have as many flags as you want 🔥

## Installation/Usage
There are two types of flags you can have when using a command, a single flag, or equals flag.

> __Very important note__:
The examples listed here don't have the code for the functions, remember you have to copy and paste them
into your file using the files in the [github repository](https://github.com/ktehllama/Flagr), choose your
method (more info below in `method` section), enter its corresponding file and 
paste the function somewhere in your code.

__Single Flag:__
In the single flag, all you do is declare a flag with its name and that's it, later in your
code you can do an action based on that flags declaration.
```bash
command: .sayhi -addemoji
return: "Hi! 💯"
```
In this example, the command itself only says hi but once you add the `-add100emoji` flag it will
add to the response. ([Discord.py](https://discordpy.readthedocs.io/) Bot Example Code)
```python
@bot.command()
async def sayhi(ctx, *, args=None):
    response = 'Hi!'
    if args:
        # This method uses the flagr_main_default way to parse, more info in methods section below
        flags = parse_flags(args)
        if 'add100emoji' in flags:
            response += f" {💯}"
    await ctx.send(response)
```

__Flags Storage Dictonary and Retrieving Values:__
_(These examples uses the flagr_main_default way to parse, more info in methods section below)_
Before we get to the equals flag example, I want to explain what happens to the flags' themselves,
where their names and values are stored.

I have this example code for a pseudo-command:
```python
# Example Command
command = ".waffles -withsyrup -amount=4 -nopickles"
flags = parse_flags(command)
print(flags)
```
We have 3 flags, `-withsyrup` which is a single flag,`-amount=4` which is an equals flag
which means you can assign a value to it to later retrive and `-nopickles` which is again
a single flag. We parse it with `parse_flags()` and print the result saved in the `flags`
variable, we get this dictonary it returns:
```json
{'withsyrup': None, 'amount': '4', 'nopickles': None}
```
As you can see, each flag brings its own value, unless it is an equals flag, the default is `None`,
if not it is saved with the corresponding value. So `withsyrup` was a single flag, so the dictonary
saves it as `None`, but since `amount` was equal to 4, it saves it as 4. You can retrieve these values
like so:
```python
# If I wanted to get the value of amount:
print(flags["amount"]) # 4
```
This is what the basic logic would look like for using a flag, you would check if it exists in the
dictonary and if it does, do something according to it:
```python
if "nopickles" in flags:
    # Do logic
```
So now you have a way to retrieve the information from any flag. In summary, all the flags and their values
(which are None if its a single flag) are stored in a dictonary you can then access for retrieving values
of an equals flag, or check if a certain flag exists and use it.

__Equals Flag:__
In the equals flag example, you declare a flag with its name but you can also add a `=` after it with
a value, this will save it's value in the flags dictonary and you can retrive that value later.
```bash
command: .hamburger -lettuce_amount=10
return: "You have ordered a hamburger (Lettuce amount 10)"
```
In this example, the command itself only says you ordered a hamburger but once you 
add the `-lettuce_amount=10` flag it will add to the response that you added _that_ amount of lettuce. 
([Discord.py](https://discordpy.readthedocs.io/) Bot Example Code)
```python
@bot.command()
async def hamburger(ctx, *, args=None):
    response = 'You have ordered a hamburger'
    if args:
        # This method uses the flagr_main_default way to parse, more info in methods section below
        flags = parse_flags(args)
        if 'lettuce_amount' in flags:
            response += f" {flags['lettuce_amount']}"
    await ctx.send(response)
```
Remember, the value doesn't always have to be a number it can be anything, you could make a 
flag such as `-hat_color=red`, if thats useful for you, of course. 

__Importance of placement of *Args:__
When using this in a Discord bot, remember always to add `*,args=None` to the parameters so
it can capture all flags, as a side note make sure you capture other important information
first such as if you want to capture a user.

Yes ✅
```python
@bot.command()
async def sayhi(ctx, user:discord.User, day, *, args=None):
```

No ❌
```python
@bot.command()
async def sayhi(ctx, *, args=None, user:discord.User, day):
```
Here, we must always place concrete parameters _before_ the *args, or it will be captured
as a string, treated like a flag and not serve its purpose. Basically, dont put a parameter
you _don't_ want to be flag after the *args. That's true for all of Python not just
Discord bots.

## Different Methods
There are two different methods you can use, it all depends on how you call the function
for parsing the flags, you have:
- Normal function (`flagr_main_default.py`)
- Wrapper/Decorator function (`flagr_main_wrapper.py`)

__Normal function method:__
This method works like a normal function where you would get your
command text string and call `parse_flags` on the command. All the code examples above
use this method so you can use them for inspiration. Though this method does require you to
write more code and more hands on as you have to manage writing the `parse_flags` function
manually and issuing a variable for it (`flags = parse_flags(command)`).

__Wrapper/Decorator function method:__
This method instead uses a [decorator function](https://www.geeksforgeeks.org/decorators-in-python/) to automatically return the flags and holds it as its own variable.
It might be a bit harder to understand but once you do, its fast and efficent.
Here is a code example for the same `sayhi` command we used before but using the wrapper method:

```python
@bot.command()
@parse_flags
async def sayhi(ctx, *, flags=None):
    response = 'Hi!'
    if flags:
        # Check for flags and customize the response accordingly
        if 'add100emoji' in flags:
            emoji = 💯
            response += f" {emoji}"
    await ctx.send(response)
```

As you can see we add the `@parse_flags` decorator to the function which automatically calls it for us,
and instead of being called args, we change the parameter to flags, and so the function saves
the flags in there by itself. This saves you the hassle of adding function declarations and adding
them to variables that could be messy looking for your code. 

__And finally..__
You can use any method you like, I personally would use the wrapper method as you can add it just like that
by adding the `@` decorator and declare the `flags=None` parameter, but it's up to you.
> __Very important reminder__:
The examples listed here don't have the code for the functions, remember you have to copy and paste them
into your code file, using the two method files in the [github repository](https://github.com/ktehllama/Flagr), choose your
method, enter its corresponding file and paste it's function somewhere in your code file.

## Afterword
Hopefully you can make some cool commands using flags and remember this isn't the only way to use them,
this readme just contains the basics of what you can do with this Flagr program. I invite you to
work out other things you can do with the code and experiment with the code of the functions themselves.
:)

## License
MIT 
_For real_
