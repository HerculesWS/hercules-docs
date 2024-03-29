# Coding style

**WORK IN PROGRESS**


Every developer has their own code style conventions and opinions, but
in a collaborative project it's a good idea if every contributor follows
the same principles and guidelines.

Hercules follows the same guidelines as the Linux Kernel (because Linus
is pretty much always right, and he doubtlessly knows what he's doing),
with some small modifications.  The original, unmodified, document can
be found at: https://www.kernel.org/doc/html/latest/process/coding-style.html

## Linux kernel coding style (Hercules version)

This is a short document describing the preferred coding style for the
linux kernel.  Coding style is very personal, and I won't _force_ my
views on anybody, but this is what goes for anything that I have to be
able to maintain, and I'd prefer it for most other things too.  Please
at least consider the points made here.

First off, I'd suggest printing out a copy of the GNU coding standards,
and NOT read it.  Burn them, it's a great symbolic gesture.

### Chapter 1: Indentation

Tabs are 8 characters, and thus indentations are also 8 characters.
There are heretic movements that try to make indentations 4 (or even 2!)
characters deep, and that is akin to trying to define the value of PI to
be 3.

_Hercules clarification: Use hard tabs, don't use spaces. That way, you
can still reduce the tab width in your own editor if you wish, without
imposing your settings to everyone else. Use spaces for alignment (but
keep hard tabs for indentation)._

**Rationale**: The whole idea behind indentation is to clearly define
where a block of control starts and ends.  Especially when you've been
looking at your screen for 20 straight hours, you'll find it a lot
easier to see how the indentation works if you have large indentations.

Now, some people will claim that having 8-character indentations makes
the code move too far to the right, and makes it hard to read on a
80-character terminal screen.  The answer to that is that if you need
more than 3 levels of indentation, you're screwed anyway, and should fix
your program.

In short, 8-char indents make things easier to read, and have the added
benefit of warning you when you're nesting your functions too deep.
Heed that warning.

The preferred way to ease multiple indentation levels in a switch
statement is to align the "switch" and its subordinate "case" labels in
the same column instead of "double-indenting" the "case" labels.  E.g.:

```c
	switch (suffix) {
	case 'G':
	case 'g':
		mem <<= 30;
		break;
	case 'M':
	case 'm':
		mem <<= 20;
		break;
	case 'K':
	case 'k':
		mem <<= 10;
		/* fall through */
	default:
		break;
	}
```

Don't put multiple statements on a single line unless you have something
to hide:

```c
	if (condition) do_this_once();
		do_that_everytime();
```

Don't put multiple assignments on a single line either.  Kernel coding
style is super simple.  Avoid tricky expressions.

Outside of comments or documentation, spaces are never used for
indentation, and the above example is deliberately broken.

Get a decent editor and don't leave whitespace at the end of lines.

### Chapter 2: Breaking long lines and strings

Coding style is all about readability and maintainability using commonly available tools.

The limit on the length of lines is 120 columns and this is a preferred limit (not a hard limit).

_Hercules change: This was originally 80, we change it to 120 and make it less strict._

Statements longer than 120 columns will be broken into sensible chunks,
unless exceeding 120 columns significantly increases readability and
does not hide information. Descendants are always substantially shorter
than the parent and are placed substantially to the right. The same
applies to function headers/calls with a long parameter/argument list
and long conditions of if-statements.
* Long function headers and calls are broken after a comma.
```c
static void do_this(int parameter1, int parameter2,
		    int parameter3)
{
	do_that(argument1, argument2,
		argument3);
}
```
* When breaking conditions of an if-statement, break before the logical operator.
```c
	if ((condition1 && condition2)
	    || condition3) {
		do_this();
	}
```
* A calculation should not be broken. Split it into logical chunks by creating variables for partial results instead.
* However, never break user-visible strings such as `ShowMessage` messages, because that breaks the ability to grep for them.

### Chapter 3: Placing Braces and Spaces

#### 3.1: Braces

The other issue that always comes up in C styling is the placement of
braces.  Unlike the indent size, there are few technical reasons to
choose one placement strategy over the other, but the preferred way, as
shown to us by the prophets Kernighan and Ritchie, is to put the opening
brace last on the line, and put the closing brace first, thusly:

```c
	if (condition) {
		do_this();
	}
```

This applies to all non-function statement blocks (`if`, `switch`, `for`,
`while`, `do`).  E.g.:

```c
	switch (action) {
	case KOBJ_ADD:
		return "add";
	case KOBJ_REMOVE:
		return "remove";
	case KOBJ_CHANGE:
		return "change";
	default:
		return NULL;
	}
```

However, there is one special case, namely functions: they have the
opening brace at the beginning of the next line, thus:

```c
static void do_this()
{
	do_that();
}
```

Heretic people all over the world have claimed that this inconsistency
is ...  well ...  inconsistent, but all right-thinking people know that
(a) K&R are _right_ and (b) K&R are right.  Besides, functions are
special anyway (you can't nest them in C).

Note that the closing brace is empty on a line of its own, _except_ in
the cases where it is followed by a continuation of the same statement,
ie a `while` in a `do`-statement or an `else` in an `if`-statement, like
this:

```c
	do {
		do_this();
	} while (condition);
```

and

```c
	if (x == y) {
		do_this();
	} else if (x > y) {
		do_that();
	} else {
		otherwise();
	}
```

**Rationale**: K&R.

Also, note that this brace-placement also minimizes the number of empty
(or almost empty) lines, without any loss of readability.  Thus, as the
supply of new-lines on your screen is not a renewable resource (think
25-line terminal screens or small laptops here), you have more empty
lines to put comments on.

Do not unnecessarily use braces where a single statement will do.

```c
	if (condition)
		do_this();
```

and

```c
	if (condition)
		do_this();
	else
		do_that();
```

This does not apply if only one branch of a conditional statement is a
single statement; in the latter case use braces in both branches:

```c
	if (condition) {
		do_this();
		do_that();
	} else {
		otherwise();
	}
```

If the condition is broken into multiple lines use braces, too:

```c
	if (condition1
	    && condition2) {
		do_this();
	} else {
		otherwise();
	}
```

#### 3.2: Spaces

Linux kernel style for use of spaces depends (mostly) on
function-versus-keyword usage.  Use a space after (most) keywords.  The
notable exceptions are `sizeof`, `typeof`, `alignof`, and
`__attribute__`, which look somewhat like functions (and are usually
used with parentheses in Linux, although they are not required in the
language, as in: `sizeof info` after `struct fileinfo info;` is
declared).

So use a space after these keywords:

```c
	if, switch, case, for, do, while
```

but not with `sizeof`, `typeof`, `alignof`, or `__attribute__`.  E.g.,

```c
	s = sizeof(struct file);
```

Do not add spaces around (inside) parenthesized expressions.  This
example is *bad*:

```c
	s = sizeof( struct file );
```

When declaring pointer data or a function that returns a pointer type,
the preferred use of `*` is adjacent to the data name or function name
and not adjacent to the type name.  Examples:

```c
	char *linux_banner;
	unsigned long long memparse(char *ptr, char **retptr);
	char *match_strdup(substring_t *s);
```

Use one space around (on each side of) most binary and ternary operators,
such as any of these:

```c
	=  +  -  <  >  *  /  %  |  &  ^  <=  >=  ==  !=  ?  :
```

but no space after unary operators:

```c
	&  *  +  -  ~  !  sizeof  typeof  alignof  __attribute__  defined
```

no space before the postfix increment & decrement unary operators:

```c
	++  --
```

no space after the prefix increment & decrement unary operators:

```c
	++  --
```

and no space around the `.` and `->` structure member operators.

Do not leave trailing whitespace at the ends of lines.  Some editors
with "smart" indentation will insert whitespace at the beginning of new
lines as appropriate, so you can start typing the next line of code
right away.  However, some such editors do not remove the whitespace if
you end up not putting a line of code there, such as if you leave a
blank line.  As a result, you end up with lines containing trailing
whitespace.

Git will warn you about patches that introduce trailing whitespace, and
can optionally strip the trailing whitespace for you; however, if
applying a series of patches, this may make later patches in the series
fail by changing their context lines.

### Chapter 4: Naming

C is a Spartan language, and so should your naming be.  Unlike Modula-2
and Pascal programmers, C programmers do not use cute names like
`ThisVariableIsATemporaryCounter`.  A C programmer would call that
variable `tmp`, which is much easier to write, and not the least more
difficult to understand.

HOWEVER, while mixed-case names are frowned upon, descriptive names for
global variables are a must.  To call a global function `foo` is a
shooting offense.

GLOBAL variables (to be used only if you _really_ need them) need to
have descriptive names, as do global functions.  If you have a function
that counts the number of active users, you should call that
`count_active_users()` or similar, you should _not_ call it `cntusr()`.

Encoding the type of a function into the name (so-called Hungarian
notation) is brain damaged - the compiler knows the types anyway and can
check those, and it only confuses the programmer.  No wonder MicroSoft
makes buggy programs.

LOCAL variable names should be short, and to the point.  If you have
some random integer loop counter, it should probably be called `i`.
Calling it `loop_counter` is non-productive, if there is no chance of it
being mis-understood.  Similarly, `tmp` can be just about any type of
variable that is used to hold a temporary value.

If you are afraid to mix up your local variable names, you have another
problem, which is called the function-growth-hormone-imbalance syndrome.
See chapter 6 (Functions).

### Chapter 5: Typedefs

Please don't use things like `vps_t`.  
It's a _mistake_ to use `typedef` for structures and pointers. When you
see a

```c
	vps_t a;
```

in the source, what does it mean?  
In contrast, if it says

```c
	struct virtual_container *a;
```

you can actually tell what `a` is.

Lots of people think that typedefs "help readability". Not so. They are
useful only for:

a. totally opaque objects (where the typedef is actively used to
   _hide_ what the object is).

   Example: `pte_t` etc. opaque objects that you can only access using
   the proper accessor functions.

   NOTE! Opaqueness and "accessor functions" are not good in themselves.
   The reason we have them for things like `pte_t` etc. is that there
   really is absolutely _zero_ portably accessible information there.

b. Clear integer types, where the abstraction _helps_ avoid confusion
   whether it is `int` or `long`.

   `uint8` / `uint16` / `uint32` are perfectly fine typedefs, although
   they fit into category (d) better than here.

   NOTE! Again - there needs to be a _reason_ for this. If something is
   `unsigned long`, then there's no reason to do

   ```c
   	typedef unsigned long myflags_t;
   ```

   but if there is a clear reason for why it under certain circumstances
   might be an `unsigned int` and under other configurations might be
   `unsigned long`, then by all means go ahead and use a typedef.

c. when you use sparse to literally create a _new_ type for
   type-checking.

d. New types which are identical to standard C99 types, in certain
   exceptional circumstances.

   Although it would only take a short amount of time for the eyes and
   brain to become accustomed to the standard types like `uint32_t`,
   some people object to their use anyway.

   Therefore, the Hercules-specific `uint8` / `uint16` / `uint32` /
   `uint64` types and their signed equivalents which are identical to
   standard types are permitted.

_Hercules note: removed an use case too specific to the linux kernel._

Maybe there are other cases too, but the rule should basically be to
NEVER EVER use a typedef unless you can clearly match one of those
rules.

In general, a pointer, or a `struct` that has elements that can
reasonably be directly accessed should _never_ be a typedef.

### Chapter 6: Functions

Functions should be short and sweet, and do just one thing.  They should
fit on one or two screenfuls of text (the ISO/ANSI screen size is 80x24,
as we all know), and do one thing and do that well.

The maximum length of a function is inversely proportional to the
complexity and indentation level of that function.  So, if you have a
conceptually simple function that is just one long (but simple)
case-statement, where you have to do lots of small things for a lot of
different cases, it's OK to have a longer function.

However, if you have a complex function, and you suspect that a
less-than-gifted first-year high-school student might not even
understand what the function is all about, you should adhere to the
maximum limits all the more closely.  Use helper functions with
descriptive names (you can ask the compiler to in-line them if you think
it's performance-critical, and it will probably do a better job of it
than you would have done).

Another measure of the function is the number of local variables.  They
shouldn't exceed 5-10, or you're doing something wrong.  Re-think the
function, and split it into smaller pieces.  A human brain can generally
easily keep track of about 7 different things, anything more and it gets
confused.  You know you're brilliant, but maybe you'd like to understand
what you did 2 weeks from now.

In source files, separate functions with one blank line.

_Hercules note: Removed a linux-specific remark_

In function prototypes, include parameter names with their data types.
Although this is not required by the C language, it is preferred in Linux
because it is a simple way to add valuable information for the reader.

### Chapter 7: Centralized exiting of functions

_Hercules comment: What follows is quite controversial. Don't just start
adding goto everywhere, if you can avoid it. If there is a real need,
use it wisely._

Albeit deprecated by some people, the equivalent of the goto statement
is used frequently by compilers in form of the unconditional jump
instruction.

The goto statement comes in handy when a function exits from multiple
locations and some common work such as cleanup has to be done.  If there
is no cleanup needed then just return directly.

Choose label names which say what the goto does or why the goto exists.
An example of a good name could be `out_buffer:` if the goto frees
`buffer`.  Avoid using GW-BASIC names like `err1:` and `err2:`.  Also
don't name them after the goto location like `err_kmalloc_failed:`

The rationale for using gotos is:

- unconditional statements are easier to understand and follow
- nesting is reduced
- errors by not updating individual exit points when making
  modifications are prevented
- saves the compiler work to optimize redundant code away ;)

```c
static int do_this(int a)
{
	int result = 0;
	char *buffer = kmalloc(SIZE, GFP_KERNEL);

	if (buffer == NULL)
		return -ENOMEM;

	if (condition1) {
		while (condition2)
			do_that();

		result = 1;
		goto out_buffer;
	}

out_buffer:
	kfree(buffer);
	return result;
}
```

A common type of bug to be aware of it "one err bugs" which look like
this:

```c
err:
	kfree(foo->bar);
	kfree(foo);
	return ret;
```

The bug in this code is that on some exit paths `foo` is NULL.  Normally
the fix for this is to split it up into two error labels `err_bar:` and
`err_foo:`.

### Chapter 8: Commenting

Comments are good, but there is also a danger of over-commenting.  NEVER
try to explain HOW your code works in a comment: it's much better to
write the code so that the _working_ is obvious, and it's a waste of
time to explain badly written code.

Generally, you want your comments to tell WHAT your code does, not HOW.
Also, try to avoid putting comments inside a function body: if the
function is so complex that you need to separately comment parts of it,
you should probably go back to chapter 6 for a while.  You can make
small comments to note or warn about something particularly clever (or
ugly), but try to avoid excess.  Instead, put the comments at the head
of the function, telling people what it does, and possibly WHY it does
it.

When commenting Hercules functions, please use the Doxygen format. See
existing commented code as well as the Doxygen manual.

_Hercules note: We use Doxygen for documentation. The above paragraph
was edited accordingly._

_Hercules note: C99-style comments are perfectly acceptable. A paragraph
was omitted._

The preferred style for long (multi-line) comments is:

```c
/* 
 * This is the preferred style for multi-line
 * comments in the Linux kernel source code.
 * Please use it consistently.
 *
 * Description:  A column of asterisks on the left side,
 * with beginning and ending almost-blank lines.
 *  
 */
```
To allow Dyoxygen to associate your comment with a specific block of code, use /** at the beginning of your comment block instead.

_Hercules note: Linux-specific information removed._

It's also important to comment data, whether they are basic types or
derived types.  To this end, use just one data declaration per line (no
commas for multiple data declarations).  This leaves you room for a
small comment on each item, explaining its use.

### Chapter 9: You've made a mess of it

That's OK, we all do.  You've probably been told by your long-time Unix
user helper that "GNU emacs" automatically formats the C sources for
you, and you've noticed that yes, it does do that, but the defaults it
uses are less than desirable (in fact, they are worse than random typing
- an infinite number of monkeys typing into GNU emacs would never make a
good program).

So, you can either get rid of GNU emacs, or change it to use saner
values.  To do the latter, you can stick the following in your .emacs
file:

```vim
(defun c-lineup-arglist-tabs-only (ignored)
  "Line up argument lists by tabs, not spaces"
  (let* ((anchor (c-langelem-pos c-syntactic-element))
         (column (c-langelem-2nd-pos c-syntactic-element))
         (offset (- (1+ column) anchor))
         (steps (floor offset c-basic-offset)))
    (* (max steps 1)
       c-basic-offset)))

(add-hook 'c-mode-common-hook
          (lambda ()
            ;; Add kernel style
            (c-add-style
             "linux-tabs-only"
             '("linux" (c-offsets-alist
                        (arglist-cont-nonempty
                         c-lineup-gcc-asm-reg
                         c-lineup-arglist-tabs-only))))))

(add-hook 'c-mode-hook
          (lambda ()
            (let ((filename (buffer-file-name)))
              ;; Enable kernel mode for the appropriate files
              (when (and filename
                         (string-match (expand-file-name "~/src/Hercules")
                                       filename))
                (setq indent-tabs-mode t)
                (setq show-trailing-whitespace t)
                (c-set-style "linux-tabs-only")))))
```

This will make emacs go better with the Hercules coding style for C
files below ~/src/Hercules.

But even if you fail in getting emacs to do sane formatting, not
everything is lost: use "indent".

Now, again, GNU indent has the same brain-dead settings that GNU emacs
has, which is why you need to give it a few command line options.
However, that's not too bad, because even the makers of GNU indent
recognize the authority of K&R (the GNU people aren't evil, they are
just severely misguided in this matter), so you just give indent the
options `-kr -i8` (stands for "K&R, 8 character indents"), or use
"scripts/Lindent", which indents in the latest style.

"indent" has a lot of options, and especially when it comes to comment
re-formatting you may want to take a look at the man page.  But
remember: "indent" is not a fix for bad programming.

### Chapter 10: (empty)

_Hercules note: This chapter has been intentionally left blank, to
preserve chapter numbers.  It may get re-used at a later time._

### Chapter 11: (empty)

_Hercules note: This chapter has been intentionally left blank, to
preserve chapter numbers.  It may get re-used at a later time._

### Chapter 12: Macros, Enums and RTL

Names of macros defining constants and labels in enums are capitalized.

```c
#define CONSTANT 0x12345
```

Enums are preferred when defining several related constants.

CAPITALIZED macro names are appreciated but macros resembling functions
may be named in lower case.

Generally, inline functions are preferable to macros resembling
functions.

Macros with multiple statements should be enclosed in a `do - while`
block:

```c
#define do_this_macro(a, b, c)         \
	do {                           \
		if (a == 5)            \
			do_this(b, c); \
	} while (0)
```

Things to avoid when using macros:

1. macros that affect control flow:

   ```c
   #define DO_THIS_MACRO(x)                   \
   	do {                               \
   		if (do_this(x) < 0)        \
   			return -EBUGGERED; \
   	} while (0)
   ```

   is a _very_ bad idea.  It looks like a function call but exits the
   "calling" function; don't break the internal parsers of those who
   will read the code.

   _Hercules note: The only exception are the `nullpo_ret` and
   `Assert_ret` families of macros, which are expected to alter control
   flow._

2. macros that depend on having a local variable with a magic name:

   ```c
   #define DO_THIS_MACRO(val) do_this(index, val)
   ```

   might look like a good thing, but it's confusing as hell when one
   reads the code and it's prone to breakage from seemingly innocent
   changes.

3. macros with arguments that are used as l-values: `FOO(x) = y;` will
   bite you if somebody e.g. turns `FOO` into an inline function.

4. forgetting about precedence: macros defining constants using
   expressions must enclose the expression in parentheses. Beware of
   similar issues with macros using parameters.

   ```c
   #define CONSTANT 0x4000
   #define CONSTEXP (CONSTANT | 3)
   ```

5. namespace collisions when defining local variables in macros
   resembling functions:

   ```c
   #define DO_THIS_MACRO(x)              \
   	do {                          \
   		int ret = do_this(x); \
   		do_that(ret);         \
   	} while (0)
   ```

   `ret` is a common name for a local variable - `__foo_ret` is less
   likely to collide with an existing variable.

### Chapter 13: Printing Hercules messages

Kernel developers like to be seen as literate. Do mind the spelling of
Hercules messages to make a good impression. Do not use crippled words
like "dont"; use "do not" or "don't" instead.  Make the messages
concise, clear, and unambiguous.

Printing numbers in parentheses `(%d)` adds no value and should be
avoided.

_Hercules note: Removed a lot of linux-specific information._

### Chapter 14: Allocating memory

Hercules provides the following general purpose memory allocators:
`aMalloc()`, `aCalloc()`, `aRealloc()`, `aReallocz()`, `CREATE()`,
`RECREATE()`. Please refer to their documentation for further
information about them.

The preferred form for passing a size of a struct is the following:

```c
	p = aMalloc(sizeof(*p));
```

The alternative form where struct name is spelled out hurts readability
and introduces an opportunity for a bug when the pointer variable type
is changed but the corresponding sizeof that is passed to a memory
allocator is not.

Casting the return value which is a void pointer is redundant. The
conversion from void pointer to any other pointer type is guaranteed by
the C programming language.

The preferred form for allocating an array is the following:

```c
	p = aMalloc(n * sizeof(...));
```

The preferred form for allocating a zeroed array is the following:

```c
	p = aCalloc(n, sizeof(...));
```

_Hercules note: Replaced with Hercules-specific information._

### Chapter 15: The inline disease

There appears to be a common misperception that gcc has a magic "make me
faster" speedup option called `inline`. While the use of inlines can be
appropriate (for example as a means of replacing macros, see Chapter
12), it very often is not. Abundant use of the inline keyword leads to a
much bigger executable, which may run slower and be harder to cache.

A reasonable rule of thumb is to not put inline at functions that have
more than 3 lines of code in them. An exception to this rule are the
cases where a parameter is known to be a compiletime constant, and as a
result of this constantness you *know* the compiler will be able to
optimize most of your function away at compile time.

Often people argue that adding inline to functions that are static and
used only once is always a win since there is no space tradeoff. While
this is technically correct, gcc is capable of inlining these
automatically without help, and the maintenance issue of removing the
inline when a second user appears outweighs the potential value of the
hint that tells gcc to do something it would have done anyway.

_Hercules remark: Please take note that inline functions can't be part
of interfaces, and as such, can't be overridden or hooked into by
plugins._

### Chapter 16: Function return values and names

Functions can return values of many different kinds, and one of the most
common is a value indicating whether the function succeeded or failed.
Such a value can be represented as an error-code integer (nonzero =
failure, 0 = success) or a "succeeded" boolean (false = failure, true =
success).

Mixing up these two sorts of representations is a fertile source of
difficult-to-find bugs.  If the C language included a strong distinction
between integers and booleans then the compiler would find these
mistakes for us... but it doesn't.  To help prevent such bugs, always
follow this convention:

> If the name of a function is an action or an imperative command, the
> function should return an error-code integer.  If the name is a
> predicate, the function should return a "succeeded" boolean.

For example, "add work" is a command, and the `add_work()` function
returns `0` for success or `-EBUSY` for failure.  In the same way, "PCI
device present" is a predicate, and the `pci_dev_present()` function
returns `true` if it succeeds in finding a matching device or `false` if
it doesn't.

All interfaced functions must respect this convention, and so should all
public functions.  Private (static) functions need not, but it is
recommended that they do.

Functions whose return value is the actual result of a computation,
rather than an indication of whether the computation succeeded, are not
subject to this rule.  Generally they indicate failure by returning some
out-of-range result.  Typical examples would be functions that return
pointers; they use `NULL` to report failure.

_Hercules note: Minor Hercules-specific edits_

### Chapter 17: (empty)

_Hercules note: This chapter has been intentionally left blank, to
preserve chapter numbers.  It may get re-used at a later time._

### Chapter 18: Don't re-invent the Hercules macros

The header files `common/cbasetypes.h`, `common/utils.h` and
`common/db.h` contain a number of macros that you should use, rather
than explicitly coding some variant of them yourself.  For example, if
you need to calculate the length of an array, take advantage of the
macro

```c
#define ARRAYLENGTH(A) ( (int)(sizeof(A)/sizeof((A)[0])) )
```

Similarly, if you need to find an element in an array, use

```c
#define ARR_FIND(_start, _end, _var, _cmp)                         \
	do {                                                       \
		for ((_var) = (_start); (_var) < (_end); ++(_var)) \
			if (_cmp)                                  \
				break;                             \
	} while(false)
```

_Hercules note: Edited with Hercules-specific information._

### Chapter 19: Editor modelines and other cruft

Some editors can interpret configuration information embedded in source
files, indicated with special markers.  For example, emacs interprets
lines marked like this:

```vim
-*- mode: c -*-
```

Or like this:

```vim
/*
Local Variables:
compile-command: "gcc -DMAGIC_DEBUG_FLAG foo.c"
End:
*/
```

Vim interprets markers that look like this:

```vim
/* vim:set sw=8 noet */
```

Do not include any of these in source files.  People have their own
personal editor configurations, and your source files should not
override them.  This includes markers for indentation and mode
configuration.  People may use their own custom mode, or may have some
other magic method for making indentation work correctly.

### Chapter 20: (empty)

_Hercules note: This chapter has been intentionally left blank, to
preserve chapter numbers.  It may get re-used at a later time._

### Chapter 21: (empty)

_Hercules note: This chapter has been intentionally left blank, to
preserve chapter numbers.  It may get re-used at a later time._

### Appendix I: References

- The C Programming Language, Second Edition  
  by Brian W. Kernighan and Dennis M. Ritchie.  
  Prentice Hall, Inc., 1988.  
  ISBN 0-13-110362-8 (paperback), 0-13-110370-9 (hardback).

- The Practice of Programming  
  by Brian W. Kernighan and Rob Pike.  
  Addison-Wesley, Inc., 1999.  
  ISBN 0-201-61586-X.  

- GNU manuals - where in compliance with K&R and this text - for cpp,
  gcc, gcc internals and indent, all available from
  http://www.gnu.org/manual/

- WG14 is the international standardization working group for the
  programming language C, URL: http://www.open-std.org/JTC1/SC22/WG14/

- Kernel CodingStyle, by greg@kroah.com at OLS 2002:
  http://www.kroah.com/linux/talks/ols_2002_kernel_codingstyle_talk/html/
