// skyOS 3.0
/*
Copyright (c) 2024 Alter-Net Codes

Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
*/
/*
The next evolution of skyOS, skyOS 3 is a single .class file
that runs in the JVM.
It is pretty useful, and it can also run apps as .class files as well.
*/

package com.alternet.skyOS.Kernel;

import java.util.Scanner;

class Kernel {
  public static void print(String text) {
    System.out.println(text);
  }
  public static void main(String[] args) {
    Scanner scanner = new Scanner(System.in);

    File appClass = null;
    URL url = null;
    String command = null;
    String pwd = System.getProperty("user.dir");
    String echo = null;
    String appClassPath = null;
    URL[] urls = null
    ClassLoader classVar = null;
    Class<?> cls = null;
    String appPackageName = null;
    while (True) {
      print("Welcome to skyOS!");
      print("skyOS v3.0");
      print("skyOS> ");
      command = scanner.nextLine();
      if (command == "help") {
        print("help - Show this help list.");
        print("app - Load an app (com.example.test is the package name for the test app and TestApp for the test app name).");
        print("echo - Echo some text.")
      }
      if (command == "app") {
        print("Enter the app name> ");
        appClassPath = scanner.nextLine();
        print("Enter the class file's package name> ");
        appPackageName = scanner.nextLine();
        file = new File(pwd + appClassPath + ".class");
        url = file.toURI().toURL();
        urls = new URL[]{url};
        classVar = new URLClassLoader(urls);
        cls = classVar.loadClass(appPackageName + appClassPath);
        Object classMethod = cls.getDeclaredMethod("appMain");
        classMethod.appMain();
        file = null;
        url = null;
        urls = null;
        classVar = null;
        cls = null;
        appClassPath = null;
      if (command == "echo") {
        print("What to echo> ");
        echo = scanner.nextLine();
        print(echo);
      }
      else:
        print("Invalid command. Type 'help' for help.");
      }
    }
  }
}
