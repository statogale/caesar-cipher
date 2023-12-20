## Preserving History Through Code- Julius Caesar's Shift Cipher

### Gaius Julius Caesar
From Wikipedia, the free encyclopedia
In cryptography, a Caesar cipher, also known as Caesar's cipher, the shift cipher, Caesar's code, or Caesar shift, is one of the simplest and most widely known encryption techniques. It is a type of substitution cipher in which each letter in the plaintext is replaced by a letter some fixed number of positions down the alphabet. For example, with a left shift of 3, D would be replaced by A, E would become B, and so on. The method is named after Julius Caesar, who used it in his private correspondence.

<div align="center">
    <img src="/images/julius_caesar.png"
         width="400"
         align="center"
         margin="100"
         alt="The Caesar cipher is named for Julius Caesar, who used an alphabet where decrypting would shift three letters to the left.." 
         caption="Gaius Julius Caesar"
    />    
    <div align="center">Julius Caesar (100-44 BCE)</div>
</div>
Source: <a href="https://en.wikipedia.org/wiki/File:Bust_of_Julius_Caesar_from_History_of_the_World_(1902).png">Wikipedia</a>


### Caesar cipher using a left rotation of three places
#### Expectations

Plain : ABCDEFGHIJKLMNOPQRSTUVWXYZ <br/>
Cipher: XYZABCDEFGHIJKLMNOPQRSTUVW <br/>

Plaintext : THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG <br/>
Ciphertext: QEB NRFZH YOLTK CLU GRJMP LSBO QEB IXWV ALD <br/>  
<br/>

<div align="center">
    <img src="/images/caesar_cipher_left_shift_of_3.png"
         width="400"
         align="center"
         margin="100"
         alt="The action of a Caesar cipher is to replace each plaintext letter with a different one a fixed number of places down the alphabet. The cipher illustrated here uses a left shift of three, so that (for example) each occurrence of E in the plaintext becomes B in the ciphertext." 
         caption="The action of a Caesar cipher"
    />    
    <div align="center">The action of a Caesar cipher</div>
</div>
Source: <a href="https://upload.wikimedia.org/wikipedia/commons/thumb/4/4a/Caesar_cipher_left_shift_of_3.svg/220px-Caesar_cipher_left_shift_of_3.svg.png">Wikipedia</a>


### Caesar cipher disk was invented over a millemium after Julius Caesar
#### But we would borrow Alberti's disc to also visualize the Caesar's Cipher

<br />
<div align="center">
    <img src="/images/alberti_cipher_disk.png" 
         width="400"
         align="center"
         margin="100"
         alt="CipherDisk2000" 
         caption="Cipher disc for substitution cipher, manufacturer: Linge, Pleidelsheim (Germany)"
    />    
    <div align="center"><br>CipherDisk2000 invented by <a href="https://en.wikipedia.org/wiki/Leon_Battista_Alberti">Leon Battista Alberti</a>&nbsp<i>1404 - 1472</i></div>
</div>
 
Source: <a href="https://upload.wikimedia.org/wikipedia/commons/b/b5/CipherDisk2000.jpg">Wikipedia</a>


### Caesar cipher using a left rotation of three places
##### With a left shift of 3, D would be replaced by A, E would become B, and so on. 
#### The cipher disk illustration was inspired by Alberti's cipher disk, although his disk had the outer disk as the rotating disk and it was also in the reverse order compared to the inner disk.

<div align="center">
    <br>
    <img src="/images/cipher_disk_shift_0.png"
         width="300"
         align="center"
         margin="100"
         alt="CipherDisk in 0 position 0 Shift" 
         caption="Cipher disc default position"
    />
    <div align="center">CipherDisk in 0 position 0 Shift</div>
    <br>
    <img src="/images/cipher_disk_shift_3.png"
         width="300"
         align="center"
         margin="100"
         alt="CipherDisk with 3 left rotations or -3 Shift" 
         caption="Cipher disc 3 left rotations"
    />
    <div align="center">Cipher disc 3 left rotations</div>
</div>

# Focus
### This caesar cipher program encrypts only uppercase letters and no other characters. Modelled closely to the caesar cipher used before common era.
### Although it can be modified to include lower case letters as explained in the alphabets module in the caesar_cipher package