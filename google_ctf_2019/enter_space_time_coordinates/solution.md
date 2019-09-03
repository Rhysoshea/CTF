### Invitation
You are a simple life form, exiled from your home planet and in search of a new place to call home. The ruling came fast. Your taste in music was deemed to be far too "out-there-man" for anyone to possibly associate with you anymore. You were given 60 revolutions of Xenon around Fir to leave and never return. Gather whatever possessions and leave. You find your parents music collection, oddly in it is a golden disc labelled "Property of NASA, if lost please return to: EVNJAKL 1600 Ampitheatre Parkway Mountain View California." The music on the disc was uncovered a while back and was not very interesting. This weird language that said something about "Peace, love and rock and roll. Also we're having a really cool party tonight, so for whoever is out there, bring a friend and come along! Co-ordinates enclosed." On the back the words "Draft, do not distribute or load onto probe" written in big red letters. That could mean anything.

You'll go, since you have nowhere else to go. But you'll be careful. You well know to learn all you can about alien beings before making contact. They could be hostile, or listen to boring music. Time is slipping away fast, you race aboard the nearest ObarPool Spaceship. But you've never driven one... what next genius?

### Enter Space-Time Coordinates
Ok well done. The console is on. It's asking for coordinates. Beating heavily on the console yields little results, but the only time anything changes on your display is when you put in numbers.. So what numbers are you going to go for?  You see the starship's logs, but is there a manual? Or should you just keep beating the console?


Two downloadable files are made available, **log.txt** and **rand2**.
Inspecting the rand2 file reveals it is a binary file that says ELF at the top.

What is and ELF file?
ELF is short for Executable and Linkable Format. In other words, it describes how it can be used for binaries and libraries on Linux and other Unix-based systems.

## Solution
We need to see the output of this executable. Executing in a linux environment and inputting the coordinates from log.txt shows the message

*Arrived somewhere, but not where the flag is. Sorry, try again.*

Instead we can use the command `strings rand2`, which shows the text items that are present in a binary file. Resulting in the following output, which also contains our first flag:

- /lib64/ld-linux-x86-64.so.2
- 0SF/
- libc.so.6
- __isoc99_scanf
- puts
- time
- printf
- __cxa_finalize
- strcmp
- __libc_start_main
- GLIBC_2.7
- GLIBC_2.2.5
- _ITM_deregisterTMCloneTable
- __gmon_start__
- _ITM_registerTMCloneTable
- []A\A]A^A_
- AC+79 3888
- Pliamas Sos
- Ophiuchus
- Pax Memor -ne4456 Hi Pro
- Camion Gyrin
- Travel coordinator
- %zu: %s -
- <REDACTED>
- %zu, %zu
- Enter your destination's x coordinate:
- >>>
- Enter your destination's y coordinate:
- >>>
- Arrived at the flag. Congrats, your flag is: CTF{welcome_to_googlectf}
- Arrived somewhere, but not where the flag is. Sorry, try again.
- ;*3$"
- GCC: (Debian 7.3.0-18) 7.3.0
- crtstuff.c
- deregister_tm_clones
- __do_global_dtors_aux
- completed.7011
- __do_global_dtors_aux_fini_array_entry
- frame_dummy
- __frame_dummy_init_array_entry
- rand2.c
- seed
- __FRAME_END__
- __init_array_end
- _DYNAMIC
- __init_array_start
- __GNU_EH_FRAME_HDR
- _GLOBAL_OFFSET_TABLE_
- __libc_csu_fini
- _ITM_deregisterTMCloneTable
- puts@@GLIBC_2.2.5
- _edata
- printf@@GLIBC_2.2.5
- __libc_start_main@@GLIBC_2.2.5
- __data_start
- strcmp@@GLIBC_2.2.5
- __gmon_start__
- __dso_handle
- _IO_stdin_used
- time@@GLIBC_2.2.5
- __libc_csu_init
- destinations
- __bss_start
- main
- next_destination
- __isoc99_scanf@@GLIBC_2.7
- __TMC_END__
- _ITM_registerTMCloneTable
- __cxa_finalize@@GLIBC_2.2.5
- .symtab
- .strtab
- .shstrtab
- .interp
- .note.ABI-tag
- .note.gnu.build-id
- .gnu.hash
- .dynsym
- .dynstr
- .gnu.version
- .gnu.version_r
- .rela.dyn
- .rela.plt
- .init
- .plt.got
- .text
- .fini
- .rodata
- .eh_frame_hdr
- .eh_frame
- .init_array
- .fini_array
- .dynamic
- .got.plt
- .data
- .bss
- .comment
