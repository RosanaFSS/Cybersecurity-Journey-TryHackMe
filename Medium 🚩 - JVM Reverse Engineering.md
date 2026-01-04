Medium 🚩 - JVM Reverse Engineering



<h2>Task 1 . Introduction</h2>
<br>

<p><em>Answer the questions below</em></p>

<p>1.1. <em>Read the above text</em><br>
<code>No answer needed</code></p

<br>
<p>1.2. <em>Consider the following bytecode:</em><br>
LDC 0<br>
LDC 3<br>
SWAP<br>
POP<br>
INEG<br>
<em>Which value is now at the top of the stack?</em><br>
<code>No answer needed</code></p>

<br>
<p>1.3. <em>Which opcode is used to get the XOR of two longs? (answer in lowercase)</em><br>
<code>lxor</code></p>

<br>
<p>1.4. <em>What does the -v flag on javap stand for? (answer in lowercase)</em><br>
<code>verbose</code></p>

<br>
<h2>Task 2 . Simple Hello World</h2>
<p>Complete the follow challenges.</p>


<p><em>Answer the questions below</em></p>

<p>2.1. <em>Find the name of the file that this class was compiled from (AKA Source File)</em> HInt : Javap is a useful tool to find information about compiled classes<br>
<code>SecretSourceFile.java</code></p>

<p>

- <strong>Source File</strong>: Identified via the <strong>SourceFile</strong> attribute as <strong>SecretSourceFile.java</strong>.</p>

```bash
:~$ javap -v -p Main.class
Classfile /home/cyberlaser/Main.class
  Last modified Jan 4, 2026; size 438 bytes
  SHA-256 checksum 0cbf8b75eb0083b8929cd20b5544791be35321ec707655fa036b149be55a49cd
  Compiled from "SecretSourceFile.java"
class Main
  minor version: 0
  major version: 52
  flags: (0x0020) ACC_SUPER
  this_class: #5                          // Main
  super_class: #6                         // java/lang/Object
  interfaces: 0, fields: 0, methods: 2, attributes: 1
Constant pool:
   #1 = Methodref          #6.#15         // java/lang/Object."<init>":()V
   #2 = Fieldref           #16.#17        // java/lang/System.out:Ljava/io/PrintStream;
   #3 = String             #18            // Hello World
   #4 = Methodref          #19.#20        // java/io/PrintStream.println:(Ljava/lang/String;)V
   #5 = Class              #21            // Main
   #6 = Class              #22            // java/lang/Object
   #7 = Utf8               <init>
   #8 = Utf8               ()V
   #9 = Utf8               Code
  #10 = Utf8               LineNumberTable
  #11 = Utf8               main
  #12 = Utf8               ([Ljava/lang/String;)V
  #13 = Utf8               SourceFile
  #14 = Utf8               SecretSourceFile.java
  #15 = NameAndType        #7:#8          // "<init>":()V
  #16 = Class              #23            // java/lang/System
  #17 = NameAndType        #24:#25        // out:Ljava/io/PrintStream;
  #18 = Utf8               Hello World
  #19 = Class              #26            // java/io/PrintStream
  #20 = NameAndType        #27:#28        // println:(Ljava/lang/String;)V
  #21 = Utf8               Main
  #22 = Utf8               java/lang/Object
  #23 = Utf8               java/lang/System
  #24 = Utf8               out
  #25 = Utf8               Ljava/io/PrintStream;
  #26 = Utf8               java/io/PrintStream
  #27 = Utf8               println
  #28 = Utf8               (Ljava/lang/String;)V
{
  Main();
    descriptor: ()V
    flags: (0x0000)
    Code:
      stack=1, locals=1, args_size=1
         0: aload_0
         1: invokespecial #1                  // Method java/lang/Object."<init>":()V
         4: return
      LineNumberTable:
        line 3: 0

  public static void main(java.lang.String[]);
    descriptor: ([Ljava/lang/String;)V
    flags: (0x0009) ACC_PUBLIC, ACC_STATIC
    Code:
      stack=2, locals=2, args_size=1
         0: iconst_0
         1: istore_1
         2: getstatic     #2                  // Field java/lang/System.out:Ljava/io/PrintStream;
         5: ldc           #3                  // String Hello World
         7: invokevirtual #4                  // Method java/io/PrintStream.println:(Ljava/lang/String;)V
        10: iinc          1, 2
        13: return
      LineNumberTable:
        line 5: 0
        line 6: 2
        line 7: 10
        line 8: 13
}
SourceFile: "SecretSourceFile.java"
```

<br>
<p>2.2. <em>What is the super class of the Main class? (Using internal name format, i.e. /)</em> Hint : Adding flags like -c to javap allow you to see the bytecode of methods. The constructor of a method always calls the constructor of its super class<br>
<code>java/lang/Object</code></p>
<p>
  
- <strong>Super Class</strong>: The class extends <strong>java/lang/Object</strong>, which is the default root class for all Java objects.</p>

```bash
...
  super_class: #6                         // java/lang/Object
...
```

<br>
<p>2.3. <em>What is the value of the local variable in slot 1 when the method returns? (In decimal format)</em><br>
<code>java/lang/Object</code></p>

<p>
  
- <strong>Bytecode Logic (Slot 1)</strong>:<br>The instruction <strong>iconst_0</strong> followed by <strong>istore_1</strong> initialized the local variable in slot 1 with the value 0.<br>The instruction <strong>iinc 1, 2</strong> performed an atomic increment, adding 2 to the value in slot 1.</p

```bash
...
stack=2, locals=2, args_size=1
         0: iconst_0
         1: istore_1
...
        10: iinc          1, 2
...
```

<br>
<h2>Task 3 . Cracking a password protected application</h2>
<p>The given class file takes a password as a parameter. You need to find the correct one. Tools like javap will be sufficient.</p>

<p><em>Answer the question below</em></p>

<p>3.1. <em>What is the correct password</em> Hint: The -v tag on javap will print the constant pool, containing utf8 encoded strings<br>
<code>yxvF2ho95ANJVCX</code></p>


```bash
...
Constant pool:
   #1 = Methodref          #10.#21        // java/lang/Object."<init>":()V
   #2 = String             #22            // yxvF2ho95ANJVCX
...
```

```bash
:~$ javap -v -p PPApp.class
Classfile /home/cyberlaser/PPApp.class
  Last modified Jan 4, 2026; size 735 bytes
  SHA-256 checksum 650f14b41f40d0209461c3e9dcc342d7bb6746f2485d4cc5cccb6a0b881a2d63
  Compiled from "PasswordProtectedApplication.java"
public class PasswordProtectedApplication
  minor version: 0
  major version: 52
  flags: (0x0021) ACC_PUBLIC, ACC_SUPER
  this_class: #9                          // PasswordProtectedApplication
  super_class: #10                        // java/lang/Object
  interfaces: 0, fields: 0, methods: 2, attributes: 1
Constant pool:
   #1 = Methodref          #10.#21        // java/lang/Object."<init>":()V
   #2 = String             #22            // yxvF2ho95ANJVCX
   #3 = Methodref          #23.#24        // java/lang/String.equals:(Ljava/lang/Object;)Z
   #4 = Fieldref           #25.#26        // java/lang/System.out:Ljava/io/PrintStream;
   #5 = String             #27            // You guessed the correct password
   #6 = Methodref          #28.#29        // java/io/PrintStream.println:(Ljava/lang/String;)V
   #7 = String             #30            // You guessed the wrong password
   #8 = String             #31            // Please supply a password
   #9 = Class              #32            // PasswordProtectedApplication
  #10 = Class              #33            // java/lang/Object
  #11 = Utf8               <init>
  #12 = Utf8               ()V
  #13 = Utf8               Code
  #14 = Utf8               LineNumberTable
  #15 = Utf8               main
  #16 = Utf8               ([Ljava/lang/String;)V
  #17 = Utf8               StackMapTable
  #18 = Class              #34            // java/lang/String
  #19 = Utf8               SourceFile
  #20 = Utf8               PasswordProtectedApplication.java
  #21 = NameAndType        #11:#12        // "<init>":()V
  #22 = Utf8               yxvF2ho95ANJVCX
  #23 = Class              #34            // java/lang/String
  #24 = NameAndType        #35:#36        // equals:(Ljava/lang/Object;)Z
  #25 = Class              #37            // java/lang/System
  #26 = NameAndType        #38:#39        // out:Ljava/io/PrintStream;
  #27 = Utf8               You guessed the correct password
  #28 = Class              #40            // java/io/PrintStream
  #29 = NameAndType        #41:#42        // println:(Ljava/lang/String;)V
  #30 = Utf8               You guessed the wrong password
  #31 = Utf8               Please supply a password
  #32 = Utf8               PasswordProtectedApplication
  #33 = Utf8               java/lang/Object
  #34 = Utf8               java/lang/String
  #35 = Utf8               equals
  #36 = Utf8               (Ljava/lang/Object;)Z
  #37 = Utf8               java/lang/System
  #38 = Utf8               out
  #39 = Utf8               Ljava/io/PrintStream;
  #40 = Utf8               java/io/PrintStream
  #41 = Utf8               println
  #42 = Utf8               (Ljava/lang/String;)V
{
  public PasswordProtectedApplication();
    descriptor: ()V
    flags: (0x0001) ACC_PUBLIC
    Code:
      stack=1, locals=1, args_size=1
         0: aload_0
         1: invokespecial #1                  // Method java/lang/Object."<init>":()V
         4: return
      LineNumberTable:
        line 1: 0

  public static void main(java.lang.String[]);
    descriptor: ([Ljava/lang/String;)V
    flags: (0x0009) ACC_PUBLIC, ACC_STATIC
    Code:
      stack=2, locals=2, args_size=1
         0: aload_0
         1: arraylength
         2: iconst_1
         3: if_icmplt     37
         6: aload_0
         7: iconst_0
         8: aaload
         9: astore_1
        10: aload_1
        11: ldc           #2                  // String yxvF2ho95ANJVCX
        13: invokevirtual #3                  // Method java/lang/String.equals:(Ljava/lang/Object;)Z
        16: ifeq          28
        19: getstatic     #4                  // Field java/lang/System.out:Ljava/io/PrintStream;
        22: ldc           #5                  // String You guessed the correct password
        24: invokevirtual #6                  // Method java/io/PrintStream.println:(Ljava/lang/String;)V
        27: return
        28: getstatic     #4                  // Field java/lang/System.out:Ljava/io/PrintStream;
        31: ldc           #7                  // String You guessed the wrong password
        33: invokevirtual #6                  // Method java/io/PrintStream.println:(Ljava/lang/String;)V
        36: return
        37: getstatic     #4                  // Field java/lang/System.out:Ljava/io/PrintStream;
        40: ldc           #8                  // String Please supply a password
        42: invokevirtual #6                  // Method java/io/PrintStream.println:(Ljava/lang/String;)V
        45: return
      LineNumberTable:
        line 3: 0
        line 4: 6
        line 6: 10
        line 7: 19
        line 8: 27
        line 10: 28
        line 11: 36
        line 14: 37
        line 15: 45
      StackMapTable: number_of_entries = 2
        frame_type = 252 /* append */
          offset_delta = 28
          locals = [ class java/lang/String ]
        frame_type = 250 /* chop */
          offset_delta = 8
}
SourceFile: "PasswordProtectedApplication.java"
```

<br>
<h2>Task 4 . Basic String Obfuscation</h2>
<p>Like the previous task, this program takes a password as an argument, and outputs whether or not it is correct. This time the string is not directly present in the class file, and you will need to use either a decompiler, bytecode analysis or virtualisation to find it.</p>

<p><em>Answer the question below</em></p>

<p>4.1. <em>What is the correct password</em> Hint: You will need to use either a decompiler, bytecode analysis or virtualisation to find it.</em><br>
<code>aSc2mRT7C6fKql6RD</code></p>

```bash
...
10: ldc #3 // String aRa2lPT6A6gIqm4RE
...
12: invokestatic #4 // Method xor:(Ljava/lang/String;)Ljava/lang/String;
...
28: iconst_3
29: irem
30: ixor
```

```bash
:~$ javap -v -p BasicStringObfuscation.class
Classfile /home/cyberlaser/BasicStringObfuscation.class
  Last modified Jan 4, 2026; size 999 bytes
  SHA-256 checksum 0868dfabf683accd771dca787394579024c66e3f1c83e36c8b5c4a5b8db4f177
  Compiled from "BasicStringObfuscation.java"
public class BasicStringObfuscation
  minor version: 0
  major version: 52
  flags: (0x0021) ACC_PUBLIC, ACC_SUPER
  this_class: #2                          // BasicStringObfuscation
  super_class: #14                        // java/lang/Object
  interfaces: 0, fields: 1, methods: 3, attributes: 1
Constant pool:
   #1 = Methodref          #14.#31        // java/lang/Object."<init>":()V
   #2 = Class              #32            // BasicStringObfuscation
   #3 = String             #33            // aRa2lPT6A6gIqm4RE
   #4 = Methodref          #2.#34         // BasicStringObfuscation.xor:(Ljava/lang/String;)Ljava/lang/String;
   #5 = Methodref          #12.#35        // java/lang/String.equals:(Ljava/lang/Object;)Z
   #6 = Fieldref           #36.#37        // java/lang/System.out:Ljava/io/PrintStream;
   #7 = String             #38            // Correct!
   #8 = Methodref          #39.#40        // java/io/PrintStream.println:(Ljava/lang/String;)V
   #9 = String             #41            // Incorrect
  #10 = String             #42            // Please provide a password
  #11 = Methodref          #12.#43        // java/lang/String.toCharArray:()[C
  #12 = Class              #44            // java/lang/String
  #13 = Methodref          #12.#45        // java/lang/String."<init>":([C)V
  #14 = Class              #46            // java/lang/Object
  #15 = Utf8               correctPassword
  #16 = Utf8               Ljava/lang/String;
  #17 = Utf8               ConstantValue
  #18 = Utf8               <init>
  #19 = Utf8               ()V
  #20 = Utf8               Code
  #21 = Utf8               LineNumberTable
  #22 = Utf8               main
  #23 = Utf8               ([Ljava/lang/String;)V
  #24 = Utf8               StackMapTable
  #25 = Class              #44            // java/lang/String
  #26 = Utf8               xor
  #27 = Utf8               (Ljava/lang/String;)Ljava/lang/String;
  #28 = Class              #47            // "[C"
  #29 = Utf8               SourceFile
  #30 = Utf8               BasicStringObfuscation.java
  #31 = NameAndType        #18:#19        // "<init>":()V
  #32 = Utf8               BasicStringObfuscation
  #33 = Utf8               aRa2lPT6A6gIqm4RE
  #34 = NameAndType        #26:#27        // xor:(Ljava/lang/String;)Ljava/lang/String;
  #35 = NameAndType        #48:#49        // equals:(Ljava/lang/Object;)Z
  #36 = Class              #50            // java/lang/System
  #37 = NameAndType        #51:#52        // out:Ljava/io/PrintStream;
  #38 = Utf8               Correct!
  #39 = Class              #53            // java/io/PrintStream
  #40 = NameAndType        #54:#55        // println:(Ljava/lang/String;)V
  #41 = Utf8               Incorrect
  #42 = Utf8               Please provide a password
  #43 = NameAndType        #56:#57        // toCharArray:()[C
  #44 = Utf8               java/lang/String
  #45 = NameAndType        #18:#58        // "<init>":([C)V
  #46 = Utf8               java/lang/Object
  #47 = Utf8               [C
  #48 = Utf8               equals
  #49 = Utf8               (Ljava/lang/Object;)Z
  #50 = Utf8               java/lang/System
  #51 = Utf8               out
  #52 = Utf8               Ljava/io/PrintStream;
  #53 = Utf8               java/io/PrintStream
  #54 = Utf8               println
  #55 = Utf8               (Ljava/lang/String;)V
  #56 = Utf8               toCharArray
  #57 = Utf8               ()[C
  #58 = Utf8               ([C)V
{
  private static final java.lang.String correctPassword;
    descriptor: Ljava/lang/String;
    flags: (0x001a) ACC_PRIVATE, ACC_STATIC, ACC_FINAL
    ConstantValue: String aRa2lPT6A6gIqm4RE

  public BasicStringObfuscation();
    descriptor: ()V
    flags: (0x0001) ACC_PUBLIC
    Code:
      stack=1, locals=1, args_size=1
         0: aload_0
         1: invokespecial #1                  // Method java/lang/Object."<init>":()V
         4: return
      LineNumberTable:
        line 1: 0

  public static void main(java.lang.String[]);
    descriptor: ([Ljava/lang/String;)V
    flags: (0x0009) ACC_PUBLIC, ACC_STATIC
    Code:
      stack=2, locals=2, args_size=1
         0: aload_0
         1: arraylength
         2: iconst_1
         3: if_icmplt     42
         6: aload_0
         7: iconst_0
         8: aaload
         9: astore_1
        10: ldc           #3                  // String aRa2lPT6A6gIqm4RE
        12: invokestatic  #4                  // Method xor:(Ljava/lang/String;)Ljava/lang/String;
        15: aload_1
        16: invokevirtual #5                  // Method java/lang/String.equals:(Ljava/lang/Object;)Z
        19: ifeq          33
        22: getstatic     #6                  // Field java/lang/System.out:Ljava/io/PrintStream;
        25: ldc           #7                  // String Correct!
        27: invokevirtual #8                  // Method java/io/PrintStream.println:(Ljava/lang/String;)V
        30: goto          41
        33: getstatic     #6                  // Field java/lang/System.out:Ljava/io/PrintStream;
        36: ldc           #9                  // String Incorrect
        38: invokevirtual #8                  // Method java/io/PrintStream.println:(Ljava/lang/String;)V
        41: return
        42: getstatic     #6                  // Field java/lang/System.out:Ljava/io/PrintStream;
        45: ldc           #10                 // String Please provide a password
        47: invokevirtual #8                  // Method java/io/PrintStream.println:(Ljava/lang/String;)V
        50: return
      LineNumberTable:
        line 5: 0
        line 6: 6
        line 8: 10
        line 9: 22
        line 11: 33
        line 13: 41
        line 15: 42
        line 16: 50
      StackMapTable: number_of_entries = 3
        frame_type = 252 /* append */
          offset_delta = 33
          locals = [ class java/lang/String ]
        frame_type = 7 /* same */
        frame_type = 250 /* chop */
          offset_delta = 0

  private static java.lang.String xor(java.lang.String);
    descriptor: (Ljava/lang/String;)Ljava/lang/String;
    flags: (0x000a) ACC_PRIVATE, ACC_STATIC
    Code:
      stack=5, locals=5, args_size=1
         0: aload_0
         1: invokevirtual #11                 // Method java/lang/String.toCharArray:()[C
         4: astore_1
         5: aload_1
         6: arraylength
         7: newarray       char
         9: astore_2
        10: iconst_0
        11: istore_3
        12: iload_3
        13: aload_2
        14: arraylength
        15: if_icmpge     39
        18: aload_1
        19: iload_3
        20: caload
        21: istore        4
        23: aload_2
        24: iload_3
        25: iload         4
        27: iload_3
        28: iconst_3
        29: irem
        30: ixor
        31: i2c
        32: castore
        33: iinc          3, 1
        36: goto          12
        39: new           #12                 // class java/lang/String
        42: dup
        43: aload_2
        44: invokespecial #13                 // Method java/lang/String."<init>":([C)V
        47: areturn
      LineNumberTable:
        line 19: 0
        line 20: 5
        line 22: 10
        line 23: 18
        line 24: 23
        line 22: 33
        line 26: 39
      StackMapTable: number_of_entries = 2
        frame_type = 254 /* append */
          offset_delta = 12
          locals = [ class "[C", class "[C", int ]
        frame_type = 250 /* chop */
          offset_delta = 26
}
SourceFile: "BasicStringObfuscation.java"
```

<p>

- javadecompilers.com</p>

<img width="1455" height="856" alt="image" src="https://github.com/user-attachments/assets/a3bacd06-da5d-4a7d-94e9-b54af98d9c68" />

<p>

- procyon</p>

```bash
$ procyon BasicStringObfuscation.class
//
// Decompiled by Procyon v0.6.0
//

public class BasicStringObfuscation
{
    private static final String correctPassword = "aRa2lPT6A6gIqm4RE";

    public static void main(final String[] array) {
        if (array.length >= 1) {
            if (xor("aRa2lPT6A6gIqm4RE").equals(array[0])) {
                System.out.println("Correct!");
            }
            else {
                System.out.println("Incorrect");
            }
            return;
        }
        System.out.println("Please provide a password");
    }

    private static String xor(final String s) {
        final char[] charArray = s.toCharArray();
        final char[] value = new char[charArray.length];
        for (int i = 0; i < value.length; ++i) {
            value[i] = (char)(charArray[i] ^ i % 3);
        }
        return new String(value);
    }
}
```


<img width="1348" height="466" alt="image" src="https://github.com/user-attachments/assets/3d4f2316-d1b0-4f74-a280-57e38b83e332" />

<br>
<br>
<br>
<p>

- solution.java</p>

```bash
public class solution {
    public static void main(String[] args) {
        String text = "aRa2lPT6A6gIqm4RE";
        char[] chars = text.toCharArray();
        char[] result = new char[chars.length];
        for (int i = 0; i < result.length; i++) {
            result[i] = (char)(chars[i] ^ (i % 3));
        }
        System.out.println("Password is: " + new String(result));
    }
}
```

```bash
:~/JVMReverseEngineering# nano solution.java
```

```bash
:~/JVMReverseEngineering# javac solution.java && java solution
Password is: aSc2mRT7C6fKql6RD
```


<img width="1221" height="90" alt="image" src="https://github.com/user-attachments/assets/c44351b9-7739-476f-b7ab-1dd6e0e08156" />

<br>
<br>
<br>
<h2>Task 5 . Advanced bytecode manipulation</h2>
<p>ASM is a powerful open source library for manipulating bytecode. It gives a high level representation of bytecode that is easy to parse and modify.

You can use asm to programmatically remove obfuscation in java applications. Java Deobfuscator is an open source project that aims to use ASM to remove common obfuscation. They provide already implemented transformers, as well as the ability to make your own. A simple way to solve advanced crackmes like the one below is to virtualise method calls, for example the method calls to decrypt the strings. Java deobfuscator provides the necessary tools to do this, and there are prewritten examples that you can adapt to any program.
<p><em>Answer the question below</em></p>

<p>5.1. <em>Read the above</em><br>
<code>NO answer needed</code></p>


<br>
<h2>Task 6 . Advanced String Obfuscation</h2>
<p>This program follows the same logic as the previous task, however it has a custom obfuscation layered on top. You might require a decompiler for this, as well as custom tools. This uses anti virtualisation techniques as well, so be warned.
  
<p><em>Answer the question below</em></p>

<p>6.1. <em>Find the correct password</em> Hint: You will either need to statically reverse engineer the string deobfuscation functions or use some kind of custom made virtualisation tool<br>
<code>NO answer needed</code></p>

```bash
:~$ file BasicStringObfuscation-obf.zip
BasicStringObfuscation-obf.zip: Java archive data (JAR)
```

```bash
:~$ unzip BasicStringObfuscation-obf.zip
Archive:  BasicStringObfuscation-obf.zip
  inflating: META-INF/MANIFEST.MF
  inflating: 0.class
  inflating: 1.class
  inflating: c.class
```

```bash
:~$ procyon c.class
//
// Decompiled by Procyon v0.6.0
//

public final class c
{
    public static int c = 1068985474;
    public static int 0 = 813209166;
    public static int 1 = 1849073100;
    public static int 2 = 636875190;
    public static int 3 = 918493662;

    static {
        c.3 = 0;
        c.2 = 1;
        c.1 = 1;
        c.0 = -1;
        c.c = -1;
    }
}
```

<p>

- value[i] = (char)(charArray[i] ^ (i & 15));<br>
- for (int i = (int)1072331622L ^ 0x3FEA7B66; i < value.length; ++i) {<br>
- value[i] = (char)(charArray[i] ^ (i & ((int)(-1108647316L) ^ 0xBDEB626E)));</p>

```bash
:~$ procyon 0.class > 0.java
```

```bash
:~$ cat 0.java
//
// Decompiled by Procyon v0.6.0
//

public class 0
{
    public static String c;

    static {
        0.c = 1.a(5, 78);
    }

    public static void main(final String[] array) {
        if (array.length >= ((int)1506594314L ^ 0x59CCCE0B)) {
            1.a(0, 100);
            String anObject;
            try {
                anObject = array[(int)(-753045066L) ^ 0xD31D71B6];
            }
            catch (final IndexOutOfBoundsException ex) {
                throw ex;
            }
            if (c(1.a(1, 95)).equals(anObject)) {
                System.out.println(1.a(2, 2));
            }
            else {
                System.out.println(1.a(3, 38));
            }
            return;
        }
        System.out.println(1.a(4, 87));
    }

    public static String c(final String s) {
        final char[] charArray = s.toCharArray();
        final char[] value = new char[charArray.length];
        for (int i = (int)1072331622L ^ 0x3FEA7B66; i < value.length; ++i) {
            value[i] = (char)(charArray[i] ^ (i & ((int)(-1108647316L) ^ 0xBDEB626E)));
        }
        return new String(value);
    }
}
```

<img width="1216" height="713" alt="image" src="https://github.com/user-attachments/assets/b14fc474-f2a2-4716-a14d-ba36e4240db9" />

<br>
<br>

```bash
/
// Decompiled by Procyon v0.6.0
//

public class 0
{
    public static String c;

    static {
        0.c = 1.a(5, 78);
    }

    public static void main(final String[] array) {
        if (array.length >= ((int)1506594314L ^ 0x59CCCE0B)) {
            1.a(0, 100);
            String anObject;
            try {
                anObject = array[(int)(-753045066L) ^ 0xD31D71B6];
            }
            catch (final IndexOutOfBoundsException ex) {
                throw ex;
            }
            String realpass = c(1.a(1, 95));
            System.out.println("A senha que o programa calculou e: " + realpass);
            if (realpass.equals(anObject)) {
                System.out.println(1.a(2, 2));
            }
            else {
                System.out.println(1.a(3, 38));
            }
            return;
        }
        System.out.println(1.a(4, 87));
    }

    public static String c(final String s) {
        final char[] charArray = s.toCharArray();
        final char[] value = new char[charArray.length];
        for (int i = (int)1072331622L ^ 0x3FEA7B66; i < value.length; ++i) {
            value[i] = (char)(charArray[i] ^ (i & ((int)(-1108647316L) ^ 0xBDEB626E)));
        }
        return new String(value);
    }
}
```

<img width="1219" height="710" alt="image" src="https://github.com/user-attachments/assets/0aedbfc8-4891-4aa5-a3d4-92e743bab776" />

<br>
<br>
<br>


```bash
:~$ strings 1.class | grep -E "^.{15,}"
Protected by Binscure
java/lang/Object
[Ljava/lang/String;
java/lang/String
(II)Ljava/lang/String;
java/lang/YourMum
java/lang/Thread
()Ljava/lang/Thread;
java/lang/StackTraceElement
()Ljava/lang/String;
 ()[Ljava/lang/StackTraceElement;
[Ljava/lang/StackTraceElement;
java/lang/Throwable
```

```bash
:~$ procyon 1.class
//
// Decompiled by Procyon v0.6.0
//

public final class 1
{
    private static final String[] a;

    static {
        (a = new String[12])[0] = "";
        1.a[2] = "[>T\u05f7\u05885\t\u0006\u05d4\u05d968\u0001\u05da\u05deRh\u0003\u05cc\u0580G0\u0006\u058d\u05d00\u001a";
        1.a[4] = "AmB\u05cb\u058cav\u0011";
        1.a[6] = "KHS\u05d6\u059bpCS\u05cd";
        1.a[8] = "R;U\u05d8\u059agw@\u05cb\u0586t>T\u05dc\u05c9cw@\u05d8\u059aq _\u05cb\u058d";
        1.a[10] = "[/T\u0ee7\u0eb85\u0018\u0006\u0ec4\u0ee96)\u0001\u0eca\u0eeeRy\u0003\u0edc\u0eb0G!\u0006\u0e9d\u0ee00\u000b";
    }

    public static String a(final int n, final int n2) {
        if (c.3 != 0) {
            throw null;
        }
        Thread currentThread = null;
        StackTraceElement[] stackTrace = null;
        int hashCode = 0;
        int hashCode2 = 0;
        char[] charArray = null;
        char[] value = null;
        char c = '\0';
        int n3 = 0;
    Label_0019_Outer:
        while (true) {
        Label_0008_Outer:
            while (true) {
                switch (n3) {
                    default: {
                        final YourMum yourMum = null;
                        break;
                    }
                    case 2: {
                        currentThread = Thread.currentThread();
                        n3 = 3;
                        continue Label_0019_Outer;
                    }
                    case 7: {
                        charArray = 1.a[n * 2].toCharArray();
                        value = new char[charArray.length];
                        n3 = 8;
                        continue Label_0019_Outer;
                    }
                    case 8: {
                        c = '\0';
                        break Label_0019;
                    }
                    case 1: {
                        return 1.a[n * 2 + 1] = new String(value);
                    }
                    case 5: {
                        hashCode2 = stackTrace[2].getMethodName().hashCode();
                        n3 = 7;
                        continue Label_0019_Outer;
                    }
                    case 0:
                    case 6: {
                        final String s = 1.a[n * 2 + 1];
                        if (s != null) {
                            return s;
                        }
                        n3 = 2;
                        continue Label_0019_Outer;
                    }
                    case 3: {
                        stackTrace = currentThread.getStackTrace();
                        n3 = 4;
                        continue Label_0019_Outer;
                    }
                    case 4: {
                        hashCode = stackTrace[2].getClassName().hashCode();
                        n3 = 5;
                        continue Label_0019_Outer;
                    }
                }
                int n4 = 0;
            Label_0141:
                while (true) {
                    n4 = (charArray[c] ^ c);
                    break Label_0141;
                    if (c >= charArray.length) {
                        n3 = 1;
                        continue Label_0019_Outer;
                    }
                    switch (c % '\u0005') {
                        case 5: {
                            continue;
                        }
                        case 3: {
                            n4 = (charArray[c] ^ hashCode2);
                            break;
                        }
                        case 0: {
                            n4 = (charArray[c] ^ '\u0002');
                            break;
                        }
                        case 4: {
                            n4 = (charArray[c] ^ hashCode2 + hashCode);
                            break;
                        }
                        case 2: {
                            n4 = (charArray[c] ^ hashCode);
                            break;
                        }
                        case 1: {
                            n4 = (charArray[c] ^ n2);
                            break;
                        }
                        default: {
                            throw null;
                        }
                    }
                    break;
                }
                value[c] = (char)n4;
                ++c;
                continue Label_0008_Outer;
            }
        }
    }
}
```

```bash

```
