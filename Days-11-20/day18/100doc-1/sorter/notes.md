# File system notes from before and after running the script

## Before script ran

node ➜ /workspaces/Nodejs/100doc-1/sorter $ ls -lah

total 8.0K

drwxr-xr-x 6 node node  192 Feb 21 01:58 .

drwxr-xr-x 3 node node   96 Feb 21 01:26 ..

drwxr-xr-x 6 node node  192 Feb 21 01:38 example

-rw-r--r-- 1 node node    0 Feb 21 01:58 notes.md

-rw-r--r-- 1 node node  301 Feb 21 01:31 package.json

-rw-r--r-- 1 node node 1.2K Feb 21 01:57 sorter.js



node ➜ /workspaces/Nodejs/100doc-1/sorter $ ls -lah example/

total 0

drwxr-xr-x 6 node node 192 Feb 21 01:38 .

drwxr-xr-x 6 node node 192 Feb 21 01:58 ..

-rw-r--r-- 1 node node   0 Feb 21 01:37 empty.exe

-rw-r--r-- 1 node node   0 Feb 21 01:37 empty.mp3

-rw-r--r-- 1 node node   0 Feb 21 01:38 empty.pdf

-rw-r--r-- 1 node node   0 Feb 21 01:38 empty.png

## After script ran

node ➜ /workspaces/Nodejs/100doc-1/sorter $ npm run start -- example

> sorter@1.0.0 start
> node sorter.js "example"



node ➜ /workspaces/Nodejs/100doc-1/sorter $ ls -lah 

total 8.0K

drwxr-xr-x 6 node node  192 Feb 21 01:58 .

drwxr-xr-x 3 node node   96 Feb 21 01:26 ..

drwxr-xr-x 6 node node  192 Feb 21 02:03 example

-rw-r--r-- 1 node node    0 Feb 21 01:58 notes.md

-rw-r--r-- 1 node node  327 Feb 21 02:03 package.json

-rw-r--r-- 1 node node 1.2K Feb 21 02:03 sorter.js



node ➜ /workspaces/Nodejs/100doc-1/sorter $ ls -lah example/

total 0

drwxr-xr-x 6 node node 192 Feb 21 02:03 .

drwxr-xr-x 6 node node 192 Feb 21 01:58 ..

drwxr-xr-x 3 node node  96 Feb 21 02:03 documents

drwxr-xr-x 3 node node  96 Feb 21 02:03 images

drwxr-xr-x 3 node node  96 Feb 21 02:03 music

drwxr-xr-x 3 node node  96 Feb 21 02:03 other



node ➜ /workspaces/Nodejs/100doc-1/sorter $ ls -lah example/documents/

total 0

drwxr-xr-x 3 node node  96 Feb 21 02:03 .

drwxr-xr-x 6 node node 192 Feb 21 02:03 ..

-rw-r--r-- 1 node node   0 Feb 21 01:38 empty.pdf



node ➜ /workspaces/Nodejs/100doc-1/sorter $ ls -lah example/images/

total 0

drwxr-xr-x 3 node node  96 Feb 21 02:03 .

drwxr-xr-x 6 node node 192 Feb 21 02:03 ..

-rw-r--r-- 1 node node   0 Feb 21 01:38 empty.png



node ➜ /workspaces/Nodejs/100doc-1/sorter $ ls -lah example/music

total 0

drwxr-xr-x 3 node node  96 Feb 21 02:03 .

drwxr-xr-x 6 node node 192 Feb 21 02:03 ..

-rw-r--r-- 1 node node   0 Feb 21 01:37 empty.mp3



node ➜ /workspaces/Nodejs/100doc-1/sorter $ ls -lah example/other

total 0

drwxr-xr-x 3 node node  96 Feb 21 02:03 .

drwxr-xr-x 6 node node 192 Feb 21 02:03 ..

-rw-r--r-- 1 node node   0 Feb 21 01:37 empty.exe