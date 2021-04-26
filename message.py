hello_word_different_languages = [
    u'👩‍💻 ALGOL \n\n'
            u'BEGIN DISPLAY("HELLO WORLD!") END',
    u'👩‍💻 AppleScript \n\n'
        u'say "Hello, world!"',
    u'👩‍💻 Assembly language \n\n'
        u'global  _main \n'
        u'extern  _printf \n \n'
        u'  section .text\n'
        u'_main:\n'
        u'  push    message\n'
        u'  call    _printf\n'
        u'  add     esp, 4\n'
        u'  ret\n'
        u'message:\n    '
        u'  db  "Hello, World", 10, 0',
    u'👩‍💻 Bash (Unix Shell) \n\n'
        u'#!/bin/bash \n'
        u'STR="Hello World!"'
        u'echo $STR',
    u'👩‍💻 BASIC \n\n'
        u'10 PRINT "Hello, World!" \n20 END',
    u'👩‍💻 C \n\n'
        u'#include <stdio.h> \n\n'
        u'int main(void) \n'
        u'{ \n'
        u'    printf("hello, world\\n");\n'
        u'} \n',
    u'👩‍💻 C++ \n\n'
        u'#include <iostream> \n\n'
        u'int main(void) \n'
        u'{ \n'
        u'  std::cout << "Hello, world!\\n";\n'
        u'  return 0;\n'
        u'} \n',
    u'👩‍💻 C# \n\n'
        u'using System;\n\n'
        u'class Program\n'
        u'{\n'
        u'  static void Main(string[] args)\n'
        u'      {\n'
        u'          Console.WriteLine("Hello, world!");\n'
        u'      }\n'
        u'}',
    u'👩‍💻 Caml (Ocaml) \n\n'
        u'print_endline "Hello, world!";;',
    u'👩‍💻 Clojure (ClojureScript) \n\n'
        u'(println "Hello world!")',
    u'👩‍💻 COBOL \n\n'
        u'  IDENTIFICATION DIVISION.\n'
        u'  PROGRAM-ID. hello-world.\n'
        u'  PROCEDURE DIVISION.\n'
        u'      DISPLAY "Hello, world!"\n'
        u'      .',
    u'👩‍💻 CoffeeScript \n\n'
        u'console.log "Hello, World!"',
    u'👩‍💻 Dart \n\n'
        u'main() {\n'
        u'  print(\'Hello World!\');\n'
        u'}',
    u'👩‍💻 dBase (FoxPro) \n\n'
        u'? "Hello World"',
    u'👩‍💻 Delphi (Object Pascal) \n\n'
        u'procedure TForm1.ShowAMessage;\n'
        u'begin\n'
        u'  ShowMessage(\'Hello World!\');\n'
        u'end;',
    u'👩‍💻 Erlang \n\n'
        u' -module(hello).\n'
        u'-export([hello_world/0]).\n'
        u'hello_world() -> io:fwrite("hello, world\\n").',
    u'👩‍💻 Elixir \n\n'
        u'IO.puts "Hello World!"',
    u'👩‍💻 F# \n\n'
        u'open System\n'
        u'Console.WriteLine("Hello World!")',
    u'👩‍💻 Fortran \n\n'
        u'program helloworld\n'
        u'  print *, "Hello world!"\n'
        u'end program helloworld',
    u'👩‍💻 Go \n\n'
        u'package main\n\n'
        u'import "fmt"\n\n'
        u'func main() {\n'
        u'    fmt.Println("Hello, World")\n'
        u'}',
    u'👩‍💻 Ruby \n\n'
        u'puts \'Hello World!\'',
    u'👩‍💻 Haskell \n\n'
        u'module Main where\n\n'
        u'main :: IO ()\n'
        u'main = putStrLn "Hello, World!"',
    u'👩‍💻 Python \n\n'
        u'print("Hello World")',
    u'👩‍💻 Java \n\n'
        u'class HelloWorldApp {\n'
        u'  public static void main(String[] args) {\n'
        u'      System.out.println("Hello World!");\n'
        u'  }\n'
        u'}',
    u'👩‍💻 JavaScript (ECMAScript) \n\n'
        u'console.log("Hello World");',
    u'👩‍💻 R \n\n'
        u'cat("Hello world\\n")',
    u'👩‍💻 PHP \n\n'
        u'<?php echo "Hello, World"; ?>',
    u'👩‍💻 Machine code \n\n'
        u'b8    21 0a 00 00   #moving "!\\n" into eax\n'
        u'a3    0c 10 00 06   #moving eax into first memory location\n'
        u'b8    6f 72 6c 64   #moving "orld" into eax\n'
        u'a3    08 10 00 06   #moving eax into next memory location\n'
        u'b8    6f 2c 20 57   #moving "o, W" into eax\n'
        u'a3    04 10 00 06   #moving eax into next memory location\n'
        u'b8    48 65 6c 6c   #moving "Hell" into eax\n'
        u'a3    00 10 00 06   #moving eax into next memory location\n'
        u'b9    00 10 00 06   #moving pointer to start of memory location into ecx\n'
        u'ba    10 00 00 00   #moving string size into edx\n'
        u'bb    01 00 00 00   #moving "stdout" number to ebx\n'
        u'b8    04 00 00 00   #moving "print out" syscall number to eax\n'
        u'cd    80            #calling the linux kernel to execute our print to stdout\n'
        u'b8    01 00 00 00   #moving "sys_exit" call number to eax\n'
        u'cd    80            #executing it via linux sys_call',
]

messages = {
    'welcome':
        u'Bienvenido a La Comunidad HackTzi, {name}!\n'
        u'¿Cuál carrera de tech estás haciendo y de dónde vienes? 😁🙌🏻\n\n'
        u'Te invitamos a consular las reglas y proyectos usando /reglas /proyectos\n\n'
        u'Ingresa el server de discord de HackTzi: {discord}',
    'rules':
        u'Reglas\n'
        u'▪️Respetar a sus comapañeros\n'
        u'▪️No hablar de temas que vayas más allá del mundo tech\n'
        u'▪️No aceptamos acoso de ningún tipo\n\n'
        u'🚨 Si incumple con alguna de las reglas será baneado del grupo',
    'projects':
        u'Si estás interesado en hacer algún proyecto puedes encontrar toda '
        u'la información al respecto aquí 👇 \n\n'
        u'http://notion.so/Proyectos-Doc-HackTzi-d1e9d4d49d3f4cb7a8c88452ddecc383',
    'current_projects': [
        u'🏬 Proyecto Tienda Platzi\n'
        u'Canal de discord: #p1-tienda-platzi\n'
        u'Tecnologías:  React.js, Python, Sass, Node.js\n\n'
        u'Descripción:\n'
        u'Una tienda con productos de Platzi donde el usuario pueda tener una experiencia '
        u'satisfactoria, además de compartir su review del producto y publicar una foto con este.',
        u'📚 Proyecto Blog HackTzi\n'
        u'Canal de discord: #p2-blog-hacktzi\n'
        u'Tecnologías: React.js, Wordpress, Fontity, Python, Kotlin, PHP, copywriting.\n\n'
        u'Descripción:\n'
        u'Un sitio web tipo Blog para la comunidad de Platzi pueda compartir apuntes,'
        u'docs de proyectos y ayudas de código.\n\n'
        u'El sitio web va a ser hecho con Wordpress en el lado del backend, y con Frontity'
        u'(React Framework) del lado del Front-end. Además tenemos un mini proyecto con '
        u' Inteligencia artificial con Python al repositorio de WaveNet.\n\n'
        u'También, hacer una versión beta de blog en una App móvil con Kotlin.',
        u'💿 Proyecto App Desktop Platzi\n'
        u'Canal de discord: #p3-app-desktop-platzi\n'
        u'Tecnologías: Angular, Python, Javascript, Sass, eslint, Electron\n\n'
        u'Descripción:\n'
        u'App desktop de Platzi que sea multiplataforma, funcione en Linux, MACOS y Windows. '
        u'El público objetivo son los estudiantes de Platzi, que no tengan que abrir varias '
        u'pestañas para poder ver sus clases todo desde un aplicación escritorio.',
    ],
    'donations':
        u'Si quieres apoyar a la comunidad de forma monetaria, puedes donar por aquí:\n\n'
        u'Este método no está disponible para Latam\n'
        u'https://paypal.me/pools/c/8wq4DXcLDI',
    'discord':
        u'Ingresa el server de discord de HackTzi: {discord}',
    'bug':
        u'418 I\'m a teapot',
    'hello_world': hello_word_different_languages,
}