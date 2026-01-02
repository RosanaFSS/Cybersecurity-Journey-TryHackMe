<h1 align="center">Learn Rust</h1>
<p align="center">22026, January 2 &nbsp; .  &nbsp; Hey! I´m <a href="https://www.linkedin.com/in/rosanafssantos/">Rosana</a> Let´s learn Rust for someone who knows programming but doesn't know low level programming from <a href="https://tryhackme.com"> TryHackMe</a>. &nbsp;&nbsp;Access it <a href="https://tryhackme.com/room/rust">here</a>.<br><br><img width="1200px" src="https://github.com/user-attachments/assets/916278ee-2885-44bf-8991-0952a26fb956"></p>

<h2>Task 1 . What is Rust?</h2>
<p>Found an issue in this room? Leave a message in Discord and someone will tag me if I don't see it :)<br>

Reminder This is a walk through room with no extra points for first bloods. Please take your time, copy the copy and experiment with it.<br>

The attached file is this entire room, but as a PDF. If you are having accessibility issues with this room, refer to the PDF which may be much better interpreted.<br>

The Crab is Rust's mascot and is taken from here. All other images are taken from Undraw.</p>

<h3>Introduction</h3>
<p>Rust is a new programming language created in 2015 by a small team of people, and later adopted by Mozilla (the organisation that created & maintains Firefox).<br>

It is a compiled low level language, which aims (and succeeds) to be the same speed as C++, but while incorporating some higher level language features from fan-favorites such as Python or JavaScript.<br>

Rust has 3 goals:<br>

- Fast<br>
- Secure<br>
- Productive</p>

<h3>Fast</h3>
<p>Rust aims to be similar in terms of performance to C++.<br>

Rust is statically typed, which means the data type of a variable is known at compile time. This allows the compiler to optimise the code further than if we didn't know the types.<br>

Rust does not use garbage collection (despite being a low level programming language). Garbage collection is where the program attempts to reclaim memory from garbage. Garbage is memory occupied by objects that are no longer in use by the program.<br>

Go, a high level programming language similar syntactically to Python but is fast & compiled, uses garbage collection. This caused a massive overhead at Discord, which forced them to switch from Go to Rust. https://blog.discord.com/why-discord-is-switching-from-go-to-rust-a190bbca2b1f<br>

Something to note is that Python and JavaScript use garbage collection. These abstractions may cause issues (as in Discord's case), which is why many choose a low level programming language.</p>


<h3>Secure</h3>
<p>Rust is completely memory safe. This means that exploits involving memory aren't possible in Rust, unless you explicitly specify unsafe Rust code.<br>

The Microsoft Security Response Centre states that 70% of all CVE's MSRC assigns are memory safety issues. In Microsoft's own words:<br>

"This means that if that software had been written in Rust, 70% of these security issues would most likely have been eliminated. And we’re not the only company to have reported such findings."<br>

Sometimes programmers must perform unsafe operations. Rust provides tools to wrap these unsafe actions so unsafe code can be statically enforced by the Rust compiler.<br>

The memory safety is guaranteed by the concept of ownership. All Rust code follows these rules:<br>

- Each value has a variable, called an owner.<br>
- There can only be one owner at a time.<br>
- When the owner goes out of scope, the value will be dropped.<br>

Values can be moved or borrowed between variables, but no value can have more than 1 owner.<br>

Let's see an example of Python failing with this:<br>


```bash
squares = (val * val for val in range(100))
print(min(squares))
print(max(squares))
```

What we want is:<br>

```bash
0
9801
```

But what we get is:<br>

```bash
>>> print(min(squares))</ode>
0
>>> print(max(squares))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: max() arg is an empty sequence
```

<p>This is because min alters the variable squares. It's strange, because we just wanted the minimum — not to alter the whole variable!<br>
In Rust, the same code is:</p>


```bash
fn main()
   let squares = (0..100).map(|val| val * val);
   println!("{:?}", squares.min());  
   println!("{:?}", squares.max());     
}                                    
```

When we try to compile this, Rust tells us:<br>

```bash
error[E0382]: use of moved value: `squares`
 --> ownership.rs:4:21
  |
3 |    println!("{:?}", squares.min());
  |                     ------- value moved here
4 |    println!("{:?}", squares.max());
  |                     ^^^^^^^ value used here after move
  |
  = note: move occurs because `squares` has type `std::iter::Map<std::ops::Range<i32>, [closure@ownership.rs:2:31: 2:40]>`, which does not implement the `Copy` trait                              
```

I'll talk more about this in a later task, but the important part is that Python allows functions to alter variables they do not own, whereas Rust doesn't.<br>

PS: Notice how the Rust compiler explicitly points out the values, the lines, the exact characters, where the error occurred as well as a full error message explaining why it won't allow that code. Whereas Python simply said <code>max() arg is an empty sequence</code>.

<h3>Productivity</h3>
<p>Rust's 3rd largest goal is a strange one. Productivity!<br>

Rust provides all of the tools developers need to be productive, shipped with the platform itself.<br>

Note: The below list is read as:<br>

- Tool<br>

Explanation of the above tool.<br>

Some of these include:<br>

- Cargo<br>

Rust's version of NPM or PyPi. Download packages others have created.<br>

- Clippy<br>

Microsoft Clippy, but re-imagined for Rust to aid with development.<br>

- RusFmt<br>

Automatically formats Rust code<br>

- Cargo Test<br>

A built in testing application created by the Rust developers.<br>

- Cargo docs<br>

Automatically generate documentation for your code, using documentation comments (written in Markdown). This documentation is then sent to docs.rs upon publishing to Cargo. Not to mention that examples written in documentation are automatically tested for you. No more untested documentation examples!<br>

- Rust-Analyzer<br>

Think IDE but more intelligent. Rust Analyzer clearly labels what is wrong with your code, why it is wrong, the exact characters that conflict and cause the error, and 90% of the time it provides an "auto-fix" function that automatically fixes these errors for you.<br>

- The Rust Book & Docs<br>

Rust has a book, called The Book which details everything you could want to know about Rust. Neatly chaptered, easily searchable and at your disposal for free. If this isn't good enough, thanks to Rust's documentation comments almost every library you'll use will have extensive documentation online.<br>

With all of these tools at your disposal, it is incredibly rare to compile a Rust program and have bugs in it. In fact, I have only experienced this once. 99% of the time, the tooling and language will have picked up on it long before I hit compile.</p>

<h3>Conclusion</h3>
<p>If you are looking for something extremely fast and memory safe but while maintaining good productivity, Rust is the language for you.<br>

As Pentesters our job is offering solutions to developers. Telling Python developers that a low-level language is a good alternative sounds wacky at first.<br>

But Rust can hold your hand, as it supports calls from functions written in other languages (foreign function interfacing).<br>

We can use Rust to rewrite security or performance critical code which will cooperate with our existing codebase.<br>

Here's an example of calling C code</p>

```bash
extern "C" {
    fn abs(input: i32) -> i32;
}

fn main() {
    unsafe {
        println!("C believes that the absolute value of -3 is: {}", abs(-3));
    }
}
```

<p><em>Answer the questions below</em></p>

<p>1.1. <em>What other language is Rust similar to in terms of performance?</em><br>
<code>C++</code></p>

<br>
<p>1.2. <em>What famous company switched from Go to Rust, mentioned in this task?</em><br>
<code>Discord</code></p>

<br>
<p>1.3. <em>Microsoft Security Centre reports what percentage of CVE's they assign are memory safety issues? Include the % sign.</em><br>
<code>70%</code></p>

<br>
<p>1.4. What is Rust's version of NPM or PyPi?<br>
<code>Cargo</code></p>

```bash
:~/learnrust# curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
...
1) Proceed with standard installation (default - just press enter)
2) Customize installation
3) Cancel installation
>
...
  stable-x86_64-unknown-linux-gnu updated - rustc 1.92.0 (ded5c06cf 2025-12-08) (from rustc 1.87.0 (17067e9ac 2025-05-09))


Rust is installed now. Great!

To get started you may need to restart your current shell.
This would reload your PATH environment variable to include
Cargo's bin directory ($HOME/.cargo/bin).

To configure your current shell, you need to source
the corresponding env file under $HOME/.cargo.

This is usually done by running one of the following (note the leading DOT):
. "$HOME/.cargo/env"            # For sh/bash/zsh/ash/dash/pdksh
source "$HOME/.cargo/env.fish"  # For fish
source $"($nu.home-path)/.cargo/env.nu"  # For nushell
```

```bash
:~/learnrust# . "$HOME/.cargo/env" 
```

<br>
<h2>Task 2 . Installing & Tooling</h2>
<p>Before we dive into the language, let's install Rust.<br>

Rust recommends using the tool <code>rustup</code> to manage multiple versions of Rust. If you are familiar with Python, you may have used virtualenvs to achieve a similar result. That is, different versions of Python on the same machine.<br>

This is another great tool created by the Rust team for productivity.<br>

Install RustUp with this command:<br>

<code>curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh</code><br

This command can also be found on the Rust website https://www.rust-lang.org/tools/install<br>

This command will install the stable version of Rust for your OS.<br>

Rust comes in 3 flavours. Stable, Beta, and Nightly.<br>

Stable is the latest stable release of Rust (stable releases are usually shipped every 6 weeks). Beta updates periodically. Nightly updates when the language itself updates.<br>

Now, let's install some Rust tools to aid our development.<br>

The command we just ran also installs <code>Cargo</code>,<br>

Cargo is the package manager for Rust. All the packages get uploaded to https://crates.io and does a lot of cool things.<br><br>

The 3 core Cargo commands are:<br>

- <strong>Cargo install</strong<br>Install a package from Crates.io<br>
- <strong>Cargo publish</strong<br>Publish a package to crates.io<br>
- <strong>Cargo update</strong<br>Updates all of the local packages<br>

But, since we are developing RustCode there are 3 more important commands<br>

- <strong>Cargo test</strong<br>Run the tests for our code<br>
- <strong>Cargo fmt</strong<br>Runs the formatting tool. This tool automatically formats your code (apply the argument <code>--all</code> to format all code). Similar to Python's Black but built in.<br>
- <strong>Cargo clippy</strong<br>Microsoft Clippy but for Rust! Clippy will point out common errors in your code and help you correct them.<br>

<strong>Community tools</strong<br>

There is one tool, that is a community based tool — that is seen as absolutely essential to the Rust ecosystem.<br>

That tool is Rust-Analyzer. Imagine an IDE but smarter and more advanced. Rust-Analyzer will analyse your code as you write it, spot errors before you compile & provide an auto-fix option to automatically fix the errors.<br>

Rust-Analyzer states that their most supported version is VS Code, but they are available on many other platforms.<br>

Something cool to note is that the main tools of Rust are written by the Rust developers themselves. In languages like Python, we may argue over whether <code>setuptools</code> or <code>poetry</code> is right. Or whether <code>pytest</code> is better than <code>unittes</code>. Arguing over the right tool to use is procrastination. Rust says "these are the tools you will use" and that's it. This boosts productivity, as you don't have to worry about what tools to use but can impede development as the tool may not be fully complete</p>

<p><em>Answer the questions below</em></p>

<p>2.1. <em>What is the tool we used to install Rust called?</em><br>
<code>Rustup</code></p>

<br>
<p>2.2. <em>How do we install the package <code>rustscan</code>code> using cargo?</em><br>
<code>cargo install rustscan</code></p>

<br>
<p>2.3. <em>What command do we run to format our code?</em><br>
<code>cargo fmt</code></p>
                        
```bash
:~/learnrust# cargo install rustscan
```

<br>
<h2>Task 3 . Hello World!</h2>
<br>

<p><em>Answer the questions below</em></p>

<p>3.1. <em>How do we initialise a new Rust project?</em><br>
<code>cargo int</code></p>

<br>
<p>3.2. <em>What character represents a macro?</em><br>
<code>!</code></p>

<br>
<p>3.3. <em>What does every Rust project need as a file?</em><br>
<code>main.rs</code></p>

<br>
<p>3.4. <em>If we wanted to add a dependency to our Rust project, what file would we edit?</em><br>
<code>cargo.toml</code></p>

<br>
<p>3.5. <em>How do we run our Rust project?</em><br>
<code>cargo run</code></p>

<br>
<p>3.6. <em>How do we build the project RustScan with the release profile (most optimised)?</em><br>
<code>cargo build --release</code></p>

<br>
<p>3.7. <em>What folder are the release binaries stored in?</em> Hint: Hint: it is in the format x/y/. Don't forget the / on the end!<br>
<code>target/release/</code></p>

<br>
<p>3.8. <em>How many release profiles does Rust have using optimisation level?</em> Hint: inclusive<br>
<code>4</code></p>

```bash
:~/learnrust# cargo init
```

<img width="1339" height="109" alt="image" src="https://github.com/user-attachments/assets/c8b03238-97d6-4991-b211-17c9e5341891" />

```bash
:~/learnrust# ls
```

<img width="1345" height="91" alt="image" src="https://github.com/user-attachments/assets/77b93837-9547-4788-8dfc-22e78fc9b1ee" />

```bash
:~/learnrust/src# cat main.rs
```

<img width="1338" height="162" alt="image" src="https://github.com/user-attachments/assets/66cdc186-e1a1-4c34-a8f4-6cc73f05543b" />

```bash
:~/learnrust/src# cargo run
```

<img width="1343" height="142" alt="image" src="https://github.com/user-attachments/assets/aedf87e4-804e-4027-af68-a8f396f1f653" />


```bash
:~/learnrust/target# ls -l
```

```bash
:~/learnrust/target# cd debug
```

```bash
:~/learnrust/target/debug# ls -l
```

<img width="1340" height="286" alt="image" src="https://github.com/user-attachments/assets/021a503b-261d-4e8e-a0b6-f34d70b23681" />

```bash
:~/learnrust/target/debug# cargo build
```

<img width="1342" height="90" alt="image" src="https://github.com/user-attachments/assets/f6ac96fd-155e-4c63-a6c7-9f5693d5c6f2" />


```bash
:~/learnrust# ./target/debug/learnrust
```

<img width="1340" height="91" alt="image" src="https://github.com/user-attachments/assets/bd3ff8a9-fdd3-4dee-82a4-a965090332e7" />

```bash
:~/learnrust# cargo build --release
```

<img width="1336" height="107" alt="image" src="https://github.com/user-attachments/assets/dee7554b-1371-4474-9d26-9b150cc4ce45" />

```bash
:~/learnrust/target# ls
```

```bash
:~/learnrust/target# cd release
```

```bash
~/learnrust/target/release# ls
```

<img width="1340" height="143" alt="image" src="https://github.com/user-attachments/assets/2ed4e425-74ef-4804-b4f3-530ec20f1c4a" />


<br>
<h2>Task 4 . Variables</h2>
<p>All variables, by default, are immutable in Rust.<br>

This is a safety feature, but also a productivity feature. Variables that don't change mean you don't have to track down when the value changed, and immutable variables are great for concurrency<br>

Let's see this in action.</p>

```bash
fn main() {
    let x = 5;
    println!("The value of x is: {}", x);
    x = 1;
    println!("The value of x is: {}", x);
}
```

<p>This code does not compile**.** It returns with the error:</p>

```bash
error[E0384]: cannot assign twice to immutable variable x``
 --> src/main.rs:4:5
  |
2 |     let x = 5;
  |         -
  |         |
  |         first assignment to `x`
  |         help: make this binding mutable: `mut x`
3 |     println!("The value of x is: {}", x);
4 |     x = 1;
  |     ^^^^^ cannot assign twice to immutable variable
```

<p>The error tells us everything we need to know.</p>

```bash
cannot assign twice to immutable variable
```

<p>This is telling us that we are assigning a value to an immutable variable (a variable that cannot be changed), twice. Which cannot happen.<br>

It is important we get compile-time errors, as this can lead to bugs and undefined behaviour — which can lead to insecure code. In Rust, once an immutable variable is set Rust guarantees it will never change in its lifetime.<br>

To make a variable mutable, we place the mut keyword in front of it like so:</p>

```bash
fn main() {     let mut x = 9;     println!("The value of x is: {}", x);     let x = 4;     println!("The value of x is: {}", x); }
```

<p>This code compiles & runs correctly:</p>

```bash
➜ cargo run                               
   Compiling hello_world v0.1.0 (/tmp/hello_world)
    Finished dev [unoptimized + debuginfo] target(s) in 0.14s
     Running `target/debug/hello_world`
The value of x is: 9
The value of x is: 4
```

<p>Being unable to change the value of a variable might have reminded you of another programming concept that most other languages have: constants. Like immutable variables, constants are values that are bound to a name and are not allowed to change, but there are a few differences between constants and variables.<br>

Refer to this code for the tasks.</p>

<h4>Question 1</h4>

```bash
fn main() {
    let x: u32 = 5;
    println!("The value of x is: {}", x);
    x = "hello";
    println!("The value of x is: {}", x);
}
```

<h4>Question 2</h4>

```bash
fn main() {
    let x: u32 = 5;
    println!("The value of x is: {}", x);
    x = 5;
    println!("The value of x is: {}", x);
}
```

<p><em>Answer the questions below</em></p>

<p>4.1. <em>In question 1, does this code compile? T(rue) or F(alse)</em><br>
<code>F</code></p>

<br>
<p>4.2. <em>What is the error code returned by question 1?</em><br>
<code>E0308</code></p>

```bash
:~# mkdir question1
```

```bash
:~# cd question1
```

```bash
:~/question1# nano main.rs
```

```bash
:~/question1# cat main.rs
```

```bash
:~/question1# cargo init
```

```bash
:~/question1# ls
```

```bash
:~/question1# cargo run
```

<img width="1339" height="608" alt="image" src="https://github.com/user-attachments/assets/953bf644-e6fa-473c-81a0-7e44b7010dbe" />

<br>
<p>4.3. <em>Does the code in question 2 compile? T(rue) or F(alse)</em><br>
<code>F</code></p>

<br>
<p>4.4. <em>What is the error <strong>message</strong> returned?</em><br>
<code>cannot assign twice to immutable variable</code></p>

```bash
:~# mkdir question2
```

```bash
:~# cd question2
```

```bash
:~/question2# nano main.rs
```

```bash
:~/question2# cat main.rs
```

```bash
:~/question2# cargo init
```

```bash
:~/question2# ls
```

```bash
:~/question2# cargo run
```

<img width="1339" height="643" alt="image" src="https://github.com/user-attachments/assets/290320f3-292c-41ed-aa02-c39519544e99" />


<br>
<h2>Task 5 . Constant Variables</h2>
<p>Rust also has constants. These are values that aren't just immutable by default, but are always immutable.<br>

Constants can be declared in any scope, including the global scope. This means that we can use their value in any part of our code, or in multiple places at once.<br>

Constants can only be constant, they cannot be set to a function call or any other value that may change at runtime.<br>

We declare constants with the <code>const</code> keyword like so:</p>

```bash
const HUNDRED_THOUSAND: u32 = 100_000;
```

<p>Notice how in Rust, we can use the <code>_</code> character to denote a space in number without it affecting the value itself. This is purely for readability.<br>

Also note that it is tradition to name a constant in all uppercase.</p>

<h3>Shadowing</h3>
<p>I'm going to show you something that might not make sense at first.</p>

```bash
fn main(){
    let x = 6;
    let x = x + 1;
    println!("{}", x)
}
```

<p>This is called shadowing. Rustaceans (Rust programmers) say that:<br>

<em>"The first variable is shadowed by the second"</em><br>

Which means the second variables value appears when used. We can change the type of an immutable variable once it has been defined.<br>

Here's an explanation from the official Rust docs about this principle (edited to match the example)<br>

"This program first binds x to a value of 6. Then it shadows x by repeating let x =, taking the original value and adding 1 so the value of x is then 7."<br>

By using let, we can perform transformations on the variable but have the variable still be immutable after all the transformations have completed.<br>

We're effectively creating a new variable with the <code>let</code> keyword, which means we can change the type of the value.</p>


```bash
let word = "hello";
let word = word.len();
```

<p>Which is allowed.<br>

However, if we tried to use mut, it wouldn't be allowed — as mut cannot change types.</p>


```bash
let mut word = "hello";
word = word.len();
error[E0308]: mismatched types
 --> src/main.rs:3:12
  |
3 |     word = word.len();
  |            ^^^^^^^^^^ expected `&str`, found `usize`
```

<p><em>Answer the questions below</em></p>

<p>5.1. <em>I have read this task.</em><br>
<code>No answer needed</code></p>

<br>
<p>5.2. <em>How do we define a constant in Rust?</em><br>
<code>const</code></p>

<br>
<p>5.3. <em>Can we shadow a constant? T(rue) or F(alse)</em><br>
<code>F</code></p>

<br>
<p>5.4. <em>If we wanted to add a dependency to our Rust project, what file would we edit?</em><br>
<code>shadowed</code></p>

<br>
<p>5.5. <em>What do we use to change the type of an immutable variable once it has been defined?</em> Hint: "The first variable is <ANSWER> by the second".". adjective<br>
<code>F</code></p>

<br>
<p>5.6. <em>We have "let word = "hello"", how do we get the length of the variable?</em><br>
<code>word.len();</code></p>

```bash
:~# mkdir constantvariables
```

```bash
:~# cd constantvariables
```

```bash
:~/constantvariables# nano main.rs
```

```bash
:~/constantvariables# cat main.rs
fn main(){
    let x = 6;
    let x = x + 1;
    println!("{}", x)
}
```

```bash
:~/constantvariables# cargo init
```

```bash
:~/constantvariables# ls
```

```bash
~/constantvariables# cargo run
```

<img width="1346" height="285" alt="image" src="https://github.com/user-attachments/assets/99f5fa35-904f-41bf-9f85-d5f5af76e196" />


<br>
<h2>Task 6 . Data Structures</h2>
<p>In Rust we'll very often see the compiler complain that our variables and functions aren't type hinted. We saw type hints with <code>CONST</code> earlier. A type hint defines what the data type of a variable is at compile time.</p>

```bash
let ports: u32 = 65535
```

<p>The <code>: u32</code> states that the variable <code>ports</code> is of size <code>u32</code>.<br>

The <code>u</code> in the integer means unsigned, and the <code>32</code> is how many bits it has.<br>

Unsigned integers can only ever be positive, signed integers can be both positive and negative.<br>

Integers range from 16 bits up to 128 bits. Some operating systems can't use integers higher than u32, and using such large integer types may slow down the program on some systems.</p>


<h6 align="center"><img width="700px" src="https://github.com/user-attachments/assets/dadff924-4745-436e-9ab1-d5951d750d76"><br>This image and all the theoretical content of the present article is TryHackMe´s property.</h6>

<p>As you explore Rust, you will come across many, many different data types. It would be foolish for me to try and teach them all, so I have elected to teach only what I believe will help you understand Rust right now.<br>

We've seen how integers work, but what about strings?</p>

<h3>Strings</h3>
<p>There are two types of strings in Rust. String and <code>&str</code>.<br>

<code>String</code> is a growable allocated data structure whereas <code>str</code> is an immutable fixed-length string somewhere in memory.

<code>&str</code> is a <code>sring slice</code> of <code>string</code>.

Strings are confusing for beginners in Rust, but these are the core principles. Here's a list to the relevant Rust book page on Strings for more information.</p>

<p><em>Answer the questions below</em></p>

<p>6.1. <em>Given the number -6, is this signed or unsigned?</em><br>
<code>Signed</code></p>

<br>
<p>6.2. <em>Given the number 65536, what is the smallest unsigned datatype we can fit this into?</em><br>
<code>u32</code></p>

<br>
<p>6.3. <em>What's the smallest sized signed integer in rust?</em><br>
<code>i16</code></p>

<br>
<p>6.4. <em>Create a mutable u32 variable called "tryhackme" and assign it the number 9</em> Hint: u32 data type<br>
<code>let mut tryhackme: u32 = 9;</code></p>

<br>
<p>6.5. <em>What data type is used to represent a string slice?</em><br>
<code>&str</code></p>

<br>
<p>6.6. <em>Let's say you had a variable, X. You wanted to typehint the variable as a string. What would you write? Include X in the variable but not the <code>let</code>code> or <code>=</code> parts.</em><br>
<code>x: String</code></p>

<br>
<h2>Task 7 . Functions</h2>
<p>We've already seen a special kind of function earlier, the <code>main</code> function.<br>

The<code>main</code> function is the first function called of the <code>main</code> file, which is the first file called.<br>

Every binary file written in Rust needs a <code>main</code> file, and every main file needs a <code>main</code> function.<br>

Functions in Rust are defined as:</p>

```bash
fn hello() -> u16{
    println!("hello!");
    6
}
```

<p>The main function is the same as this, but in a binary file it doesn't return anything.</p>


```bash
fn main(){
    println!("I do not return!")
}
```

<p>Now, you might have noticed in the <code>hello</code> function that we have a 6 on the end.<br>

<em>"What???"</em> I can hear you saying.<br>


Well, Rust returns the final expression of the function.<br>

Alternatively, we can use the <code>return</code> statement to return earlier. However, it's not very nice to use it to return the value at the end of the function — Rustaceans and Clippy will dislike that 😢<br>

<code>6</code> is an expression that returns 6, so our <code>hello</code> function returns <code>6</code>.<br>

Our <code>main</code> function does not return anything, which is the way it should be.<br>

Let's add some arguments to our functions.</p>

```bash
fn print_name(name: String){
    println!("{}", name);
}
```

<p>Our function arguments have to include the type of each argument.<br>

Now let's try to make this function return something.</p>

```bash
fn print_name(name: String) -> u16{
    println!("{}", name);
    6;
}
```

<p>When we return data, we have to type hint the type of data that is being returned.<br>

This may seem annoying, but it makes writing clean code so much easier.<br>

Compare these two functions, one in Pythonic pseudocode and one in Rust. Note: we only have the definitions.</p>

```bash
def to_ip_address(ip):
```

<p>Now in Rust:</p>

```bash
fn to_ip_address(ip: String) -> IpAddr{
```

<p>By just adding the types we can clearly see we are taking in a string, and turning it into an IP address.<br>

With proper function naming and typehints, we can tell what most functions do just from their definitions. How's that for clean code 😜</p>

<h4>Question 1</h4>

```bash
fn hello(){
    8172192: u16;
}
```

<h4>Question 2</h4>

```bash
fn return(){
    6;
}
```

<h4>Question 3</h4>

```bash
fn test(name) {
    println!("{}", name);
}
test("bee");
```

<p><em>Answer the questions below</em></p>

<p>7.1. <em>Will question 1 return 8172192? T(rue) or F(alse)</em><br>
<code>F</code></p>

<img width="1334" height="560" alt="image" src="https://github.com/user-attachments/assets/e6f5ef31-ac85-4b92-9db5-0c6a3efa5cd5" />

<br>
<br>
<p>7.2. <em>Will example 2 run? T(rue) or F(alse)</em><br>
<code>F</code></p>

<img width="1342" height="197" alt="image" src="https://github.com/user-attachments/assets/c517b7db-1394-46af-bb54-3a2ca6d7e2cf" />

<br>
<br>

<img width="1338" height="428" alt="image" src="https://github.com/user-attachments/assets/c8abfc37-a26c-44ee-8801-fb5aee021aed" />


<br>
<br>

<p>7.3. <em>What type should we give to the argument for question 3?</em> Hint: "bee" is passed to the test function which makes the argument a &'static str<br>
<code>&str</code></p>

<img width="1336" height="772" alt="image" src="https://github.com/user-attachments/assets/d3bc9957-4662-4a73-90cb-717857210c05" />


<br>
<p>7.4. <em>The last expression in a function (the return) needs to have a semicolon. T(rue) or F(alse)</em> Hint: Since you can return values such as "42" without semicolons.<br>
<code>F</code></p>

<br>
<p>7.5. <em>Every function need to return something. T(rue) or F(alse)</em><br>
<code>F</code></p>

<img width="453" height="161" alt="image" src="https://github.com/user-attachments/assets/ac70dee8-2f94-4f66-a4ab-d44d8ced763a" />

<br>
<br>
<p>7.6. <em>Functions in Rust can be nested within other functions. T(rue) or F(alse)</em><br>
<code>T</code></p>

<br>
<p>7.7. <em>What keyword do we use to return early from a function?</em><br>
<code>return</code></p>

<img width="438" height="117" alt="image" src="https://github.com/user-attachments/assets/3cac6a47-48c4-4812-a233-907c6ed9d864" />

<br>
<br>
<p>7.8. <em>You nest a function named main, inside another function named main. Will this run? T(rue) or F(alse)</em><br>
<code>T</code></p>

<br>
<h2>Task 8 . Loops</h2>
<br>

<p><em>Answer the questions below</em></p>

<p>8.1. <em>How do we break out of a loop?</em><br>
<code>break</code></p>

<br>
<p>8.2. <em>Simplest keyword to make an infinite loop?</em><br>
<code>loop</code></p>

<br>
<p>8.3. <em>Turn <code>let a = [10, 20];</code>code> into something we can iterate over.</em><br>
<code>a.iter()</code></p>

<br>
<p>8.4. <em>While loops can also be infinite. T(rue) or F(alse).</em><br>
<code>T</code></p>

<br>
<h2>Task 9 . Zero Cost Abstractions</h2>

<p><em>Answer the questions below</em></p>

<p>9.1. <em>Read the above.</em><br>
<code>No answer needed</code></p>

<br>
<p>9.2. <em>Iterators are lazy. T(rue) or F(alse).</em><br>
<code>T</code></p>

<br>
<p>9.3. <em>For loops are explicitly mentioned in the Rust book as zero cost abstractions. T(rue) or F(alse).</em><br>
<code>F</code></p>

<br>
<p>9.4. <em>Zero Cost Abstractions are common in high level languages like Python or JavaScript T(rue) or F(alse).</em><br>
<code>F</code></p>


<br>
<h2>Task 10 . Rayon</h2>

<br>

<p><em>Answer the questions below</em></p>

<p>10.1. <em>What crate do we use to easily make an iter multi threaded?</em><br>
<code>Rayon</code></p>

<br>
<p>10.2. <em>SHow do we tell Rust to include an external crate into our program? What file do we place this information in?</em><br>
<code>cargo.toml</code></p>

<br>
<p>10.3. <em>Turn a.iter() into a multi threaded parallel iter using Rayon</em><br>
<code>a.par_iter()</code></p>

<br>
<p>10.4. <em>What website do we go to for Crates?</em><br>
<code>crates.io</code></p>


<br>
<h2>Task 11 . If Statements</h2>

<br>

<p><em>Answer the question below</em></p>

<p>11.1. <em>We can assign variables based on an if statement on one line T(rue) or F(alse)</em><br>
<code>T</code></p>


<br>
<h2>Task 12 . Error Handling</h2>

<br>

<p><em>Answer the questions below</em></p>

<p>12.1. <em>What is the data type returned from opening a file?</em><br>
<code>Result</code></p>

<br>
<p>12.2. <em>Write the datatype of a generic Result with type hints</em> Hint: Due to XSS protection, the answer replaces the "<" with a space.<br>
<code>Result T, E></code></p>

<br>
<p>12.3. <em>We're in a function and we get given a Result enum. If the Result is okay we want to continue working on it in this function. If the result is Err we want to return to the parent function with Err. What should we use?</em><br>
<code>?</code></p>

<br>
<p>12.4. <em>We're certain our result will always return Ok, what should we use?</em> Hint: no ()<br>
<code>unwrap</code></p>



<br>
<h2>Task 13 . Challenge</h2>
<p>Challenge file 1.<br>

"M3I6r2IbMzq9" is the text.<br>

The text is encrypted with:<br>

plaintext -> ROT13 -> base64 -> rot13<br>

Go the opposite way and decrypt the file.<br>

rot13 -> base64 -> ROT13 -> plaintext<br>

You'll notice it's the same order either way, so you don't have to worry about order. Just make sure ROT13 is on the inside.<br>

You might run into lifetime borrow checker issues.<br>

Here's some hints in case you do:<br>

1. Google is your friend.<br>

2. https://doc.rust-lang.org/book/ch04-02-references-and-borrowing.html<br>

3. Stop trying to do so many things at once. Break it down to the bare necessities and slowly build back up to see what causes the errors.</p>

<br>

<p><em>Answer the questions below</em></p>

<p>13.1. <em>Challenge 1</em><br>
<code>THM{Rust}</code></p>

<br>

<img width="1335" height="506" alt="image" src="https://github.com/user-attachments/assets/616d2af8-ef38-4210-85d1-ee92c138ea35" />

<br>
<br>

```bash
extern crate cipher_crypt;
extern crate base64;

use cipher_crypt::Rot13;
use base64::{engine::general_purpose, Engine as _};

fn main() {
    let enc = "M3I6r2IbMzq9";

    // ROT13 decryption
    let rot13a = Rot13::decrypt(enc);

    // Base64 decryption
    let b64a = general_purpose::STANDARD.decode(rot13a).unwrap();
    let b64b = String::from_utf8(b64a).unwrap();

    // ROT13 decryption again
    let challenge = Rot13::decrypt(&b64b);

    println!("Plaintext -> ROT13 -> Base64 -> ROT13: {}", challenge);
}
```

<img width="1341" height="428" alt="image" src="https://github.com/user-attachments/assets/c32af2ca-ada3-4b48-a67a-c6c3f6daeac5" />

<br>
<br>

<img width="1336" height="292" alt="image" src="https://github.com/user-attachments/assets/bf36fe81-0e81-4828-b43a-3297899c8d4e" />

<br>
<br>
<p>Google Gemini supported me on this one—I wouldn't have cracked it otherwise!</p>

```bash
:~/challenge# nano Cargo.toml
```

```bash
:~/challenge# cat Cargo.toml
[package]
name = "challenge"
version = "0.1.0"
edition = "2021"

[dependencies]
# Dependencies must be defined here, not inside [[bin]]
base64 = "0.22"

[[bin]]
name = "challenge"
path = "main.rs"
```


<img width="1352" height="315" alt="image" src="https://github.com/user-attachments/assets/32dc738a-b203-4382-88d6-e214f7546f7e" />

<br>
<br>

```bash
:~/challenge# cat main.rs
use base64::{engine::general_purpose, Engine as _};

fn main() {
    // The encrypted string from the challenge
    let ciphertext = "M3I6r2IbMzq9";

    // LOGIC: The prompt says the text was encrypted as: 
    // Plaintext -> ROT13 -> Base64 -> ROT13
    // To decrypt, we reverse the steps:
    // 1. ROT13 (reverses itself)
    // 2. Base64 Decode
    // 3. ROT13 (reverses itself)

    // Step 1: First ROT13
    let stage1 = rot13(ciphertext);

    // Step 2: Base64 Decode
    // We expect the result to be valid UTF-8 text
    let stage2_bytes = general_purpose::STANDARD
        .decode(&stage1)
        .expect("Failed to decode Base64. Check your input string.");
    
    let stage2_string = String::from_utf8(stage2_bytes)
        .expect("Base64 result was not valid text.");

    // Step 3: Final ROT13 to get the plaintext
    let plaintext = rot13(&stage2_string);

    println!("Success! The flag is: {}", plaintext);
}

// Helper function: ROT13 implementation
// This shifts a-z and A-Z by 13 spots, wrapping around.
fn rot13(input: &str) -> String {
    input.chars().map(|c| {
        match c {
            'a'..='m' | 'A'..='M' => ((c as u8) + 13) as char,
            'n'..='z' | 'N'..='Z' => ((c as u8) - 13) as char,
            _ => c,
        }
    }).collect()
}
```

<img width="1337" height="249" alt="image" src="https://github.com/user-attachments/assets/75d71d54-958f-429b-a890-b07c202e0fa8" />


<br>
<h2>Task 14 . Conclusion</h2>

<br>

<p><em>Answer the questions below</em></p>

<p>14.1. <em>Goodbye! <3</em><br>
<code>No answer needed</code></p>


<br>
<br>
<h1 align="center">Completed</h1>

<p align="center"><img width="1200px" src="https://github.com/user-attachments/assets/f065f545-e4ba-40fb-b268-7f353150d7ef"><br><br>
                  <img width="1200px" src="https://github.com/user-attachments/assets/97d98a1e-b9f2-4cf6-80c8-b21d4c12e81d"></p>


<h1 align="center">My TryHackMe Journey ・ 2026, January</h1>

<div align="center"><h6>

| Date<br><br>   | Room <br><br> |Streak<br><br>   |Global<br>All Time|Brazil<br>All Time|Global<br>Monthly|Brazil<br>Monthly|Points<br><br>|Rooms<br>Completed|Badges<br><br>|
|:------:|:--------------------------------------|:--------:|:------------:|:------------:|:------------:|:------------:|:------------:|:------------:|:------------:|
|2      |Easy 🔗 - Learn Rust           |1 |     96ᵗʰ  |     3ʳᵈ    |    5,152ⁿᵈ   |       67ᵗʰ     |    136,030  |    1,056    |    84     |


</h6></div><br>


<p align="center">Global All Time:    96ᵗʰ<br><img width="250px" src="https://github.com/user-attachments/assets/4e5bb853-6a00-4102-89a9-f182b98fd4f6"><br>
                                              <img width="1200px" src="https://github.com/user-attachments/assets/c4b95030-4ca6-43c3-9a5b-3888db9ad03b"><br><br>
                  Brazil All Time:      3ʳᵈ<br><img width="1200px" src="https://github.com/user-attachments/assets/225f6e72-0e28-472e-b92b-ac6e2c3f93e3"><br><br>
                  Global monthly:   5,152ⁿᵈ<br><img width="1200px" src="https://github.com/user-attachments/assets/ae069268-a793-4169-9c44-e194c1b8068a"><br><br>
                  Brazil monthly:      67ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/acf3c4ff-ef4a-4da6-943f-ade1bd903b92"></p>

<h1 align="center">Thanks for coming!</h1>
<p align="center">Follow me on <a href="https://medium.com/@RosanaFS">Medium</a>, here on <a href="https://github.com/RosanaFSS/TryHackMe">GitHub</a>, and on <a href="https://www.linkedin.com/in/rosanafssantos/">LinkedIN</a>.</p

